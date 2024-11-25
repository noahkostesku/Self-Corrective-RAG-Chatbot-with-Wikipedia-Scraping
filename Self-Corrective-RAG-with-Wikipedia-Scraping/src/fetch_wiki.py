import wikipedia
import json
import logging
from pathlib import Path
from retrying import retry

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

@retry(stop_max_attempt_number=3, wait_fixed=2000)
#fetch wiki page content, with a max length of 10 sentences
def fetch_content(title, sentences=10):
    try:
        return wikipedia.summary(title, sentences=sentences, auto_suggest=False, redirect=True)
    except wikipedia.DisambiguationError as e:
        logging.warning(f"DisambiguationError for '{title}': {e.options}")
    except wikipedia.PageError:
        logging.warning(f"PageError: The page '{title}' does not exist.")
    except Exception as e:
        logging.error(f"Error fetching '{title}': {e}")
    return None

#debugging function for faulty titles
def fetch_wikipedia_contents(titles, sentences=10):
    wiki_data = []
    for title in titles:
        logging.info(f"Fetching content for: {title}")
        content = fetch_content(title, sentences)
        if content:
            wiki_data.append({"title": title, "content": content})
        else:
            logging.warning(f"Skipping '{title}' due to missing content.")
    return wiki_data

def main():
    #retrieve wikipedia titles
    titles = [
        "OpenAI",
        "Artificial intelligence",
        "Natural language processing",
        "Deep learning",
        "Neural network",
        "Data science",
        "Reinforcement learning",
        "Generative adversarial network",
        "Transfer learning",
        "Support vector machine",
        "Artificial general intelligence",
        "Explainable artificial intelligence",
        "Ethics of artificial intelligence",
        "Transformer (machine learning model)",
        "Backpropagation",
        "Gradient descent",
        "Supervised learning",
        "Unsupervised learning",
        "Semi-supervised learning",
        "Federated learning",
        "AI safety",
        "Cognitive computing",
        "Expert system",
        "Bayesian network",
        "Robotics",
        "Fuzzy logic",
        "Swarm intelligence",
        "Evolutionary algorithm",
        "Big data",
        "Quantum machine learning",
        "Self-supervised learning",
        "Zero-shot learning",
        "One-shot learning",
        "Hyperparameter optimization",
        "Autonomous vehicle",
        "AI in healthcare",
        "Knowledge graph",
        "Meta-learning",
        "Adversarial machine learning",
        "Singularity (technological)",
        "AI alignment problem",
        "Machine translation",
        "Speech recognition",
        "Voice recognition",
        "AI art",
        "Algorithmic trading",
        "AI ethics",
        "AI policy",
        "AI regulation"
        # Add more titles as needed
    ]
    wiki_data = fetch_wikipedia_contents(titles, sentences=10)

    output_file = Path(__file__).parent / "../data/wiki_data.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(wiki_data, f, ensure_ascii=False, indent=4)
    
    logging.info(f"Saved Wikipedia data to {output_file.resolve()}")

if __name__ == "__main__":
    main()

