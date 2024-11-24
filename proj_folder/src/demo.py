

from dotenv import load_dotenv
import os
import json
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.schema import Document
from langchain import hub
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load .env vars (API KEY)
load_dotenv()

# Get OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment.")
os.environ["OPENAI_API_KEY"] = openai_api_key

# Convert scraped Wikipedia data from a JSON file
data_file = Path(__file__).parent / "../data/wiki_data.json"
with data_file.open("r", encoding="utf-8") as f:
    wiki_data = json.load(f)

# Prepare documents
docs = [Document(page_content=item["content"], metadata={"title": item["title"]}) for item in wiki_data]

# Split each document's content into smaller chunks for better retrieval
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# Create a vector store using Chroma, which organizes the chunks for efficient similarity-based retrieval
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Load a predefined prompt template for RAG from LangChain
rag_prompt = hub.pull("rlm/rag-prompt")

# Set up LLM
llm = ChatOpenAI(model="gpt-4")

# Define formatting function for retrieved documents
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Build RAG pipeline: retriever --> formatter --> LLM
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()} 
    | rag_prompt  # context
    | llm        # pass prompt for LLM generation
    | StrOutputParser()  # parse LLM response for usable format
)

# Self-correction prompt for improving answer on feedback
correction_prompt = PromptTemplate(
    input_variables=["original_question", "original_answer", "feedback"],
    template="""
    Original question: {original_question}
    Original answer: {original_answer}
    Feedback: {feedback}

    Please provide an improved answer based on the feedback:
    """
)

# Create a chain to perform self-correction using the LLM and the correction prompt
correction_chain = LLMChain(llm=llm, prompt=correction_prompt)

# Main function for the RAG system with self-correction capabilities
def self_corrective_rag(question, feedback=None, max_iterations=3):
    # Retrieve context documents based on the question
    context_docs = retriever.get_relevant_documents(question)
    context = format_docs(context_docs)

    # Initial answer generation based on the question and context
    answer = rag_chain.invoke(question)

    # If feedback is provided, refine the answer iteratively up to max_iterations
    if feedback:
        for i in range(max_iterations):
            corrected_answer = correction_chain.run(
                original_question=question,
                original_answer=answer,
                feedback=feedback
            )
            answer = corrected_answer

    return {"answer": answer, "context": context}  # Return both answer and context if needed




