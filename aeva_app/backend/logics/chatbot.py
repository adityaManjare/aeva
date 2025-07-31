
from sentence_transformers import SentenceTransformer
import chromadb
from dotenv import load_dotenv
import os
import requests
from .. import schemas

#constants and important 

embedding_model = SentenceTransformer("multi-qa-MPNET-base-dot-v1")
client = chromadb.PersistentClient(path="../../../chroma_db")
embeddings_db = client.get_or_create_collection(name="embeddings")


load_dotenv()
MODEL = "llama3-8b-8192" 
GROQ_API_KEY= os.getenv("GROQ_API_KEY")  # Get the API key from environment variables


def chatbot(query:schemas.FinalChat):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": f"you are a chatbot designed to answer queries of the user strictly based on the context provided also print the metadata make sure to ans the question in presentable format "}, 
            {"role": "user", "content": f"relevnt chunks are from:{query.ans_mode}"},
            {"role": "user", "content": f" relevent chunks which you have to stick while answering :{query.context}"},
            {"role": "user", "content": f"metadatas :{query.metadata}"},
            {"role": "user", "content": query.original_query}
        ]
    }
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    reply = response.json()["choices"][0]["message"]["content"]
    return reply




