
from sentence_transformers import SentenceTransformer
import chromadb
from dotenv import load_dotenv
import os
import requests

#constants and important 

n_results = 2

embedding_model = SentenceTransformer("multi-qa-MPNET-base-dot-v1")
client = chromadb.PersistentClient(path="./chroma_db")
embeddings_db = client.get_or_create_collection(name="embeddings")


load_dotenv()
MODEL = "llama3-8b-8192" 
GROQ_API_KEY= os.getenv("GROQ_API_KEY")  # Get the API key from environment variables


def chatbot(input_query,relevent_chunks):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": f"you are a chatbot designed to answer queries of the user strictly based on the context provided also print the metadata (like page number and doc name)make sure to ans the question in presentable format and also print the context"}, 
            {"role": "user", "content": f" relevent chunks which you have to stick while answering :{relevent_chunks['documents']}"},
            {"role": "user", "content": f"metadatas :{relevent_chunks['metadatas']}"},
            {"role": "user", "content": input_query}
        ]
    }
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    reply = response.json()["choices"][0]["message"]["content"]
    print(relevent_chunks['documents'])
    return reply




