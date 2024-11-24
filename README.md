# Self-Corrective-RAG-with-Wikipedia-Scraping

## *Ongoing Project* ##

### Overview

This project focuses on building a Self-Corrective Reasoning Augmented Generative (RAG) system that integrates Wikipedia scraping and advanced reasoning capabilities. It uses a LangChain-powered framework to retrieve and process knowledge efficiently, enabling iterative improvements to generated content through self-correction. The goal is to create a dynamic, AI-driven system capable of producing accurate and contextually coherent results.

### Key Features

**Wikipedia Scraping**: The system scrapes and summarizes AI-related topics from Wikipedia using Python’s wikipedia library. Topics such as "Neural Networks" and "Reinforcement Learning" are pre-processed into a structured JSON format to build a knowledge base.

**Self-Correction**: Using LangChain’s pipelines, the system incorporates user feedback to iteratively refine outputs, ensuring accuracy and relevance.

**Full-Stack Application**: The project includes a Flask backend and a web-based UI for users to interact with the RAG system. Queries and feedback can be submitted directly through the interface.

**Generative AI Integration**: The OpenAI API is employed to handle the generative aspects of the project, leveraging models like GPT-4 to produce high-quality text outputs.

To install all dependencies, run:
```pip install -r requirements.txt```
To run the application:
```python app.py```

## Current Status

- The system currently performs the following tasks:

- Scraping Wikipedia: Collects and summarizes key AI topics, saving them in JSON format.

- Document Chunking: Splits documents into manageable chunks using LangChain’s text splitter for efficient retrieval.

- Retrieval Pipeline: Uses Chroma’s vector storage to retrieve relevant knowledge based on user queries.

- Self-Correction Workflow: Implements iterative refinements to generated answers based on feedback.

- Flask Integration: Hosts a user-friendly interface to input queries and view results.

## Future Enhancements

- Knowledge Base Expansion: Add more topics and sources to enrich the retrieval pipeline.

- Improved UI: Enhance user interface for better usability and aesthetics.

- Performance Metrics: Incorporate analytics to monitor accuracy and self-correction improvements.

- Cloud Deployment: Deploy the system using Docker for scalability.

*Advanced Retrieval Methods: Explore additional APIs, open-source models like LLaMA, and optimizations to refine the retrieval and generation process. Integrating these models can provide cost-effective alternatives to proprietary APIs while maintaining robust generative capabilities*


### Notes on the License Section:
1. **Custom Text**: The copyright text is tailored to attribute ownership to Noah Kostesku.
2. **Optional License**: You can choose any open-source license, such as MIT, GPL, or others, or simply keep the "All rights reserved" statement.
3. **Contact Information**: Adding contact details is optional but can clarify how to seek permissions or ask questions about usage.
4. **Hyperlinks**: The `[MIT License](https://opensource.org/licenses/MIT)` provides a clickable link for more information. Adjust based on the selected license.

