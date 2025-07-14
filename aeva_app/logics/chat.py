import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv
import os
import requests

#constants and important 
chunk_size = 750
n_results = 1
url ="test_data/chapter1.pdf"
embedding_model = SentenceTransformer("multi-qa-MPNET-base-dot-v1")
client = chromadb.PersistentClient(path="./chroma_db")
embeddings_db = client.get_or_create_collection(name="embeddings")

load_dotenv()
MODEL = "llama3-8b-8192" 
GROQ_API_KEY= os.getenv("GROQ_API_KEY")  # Get the API key from environment variables




def parse_doc(url):
    doc = fitz.open(url)
    context = ""
    for page in doc:
        context += page.get_text()
    else:
        print("parsing successful")
    return context



def chunk_embed_store(chunk_size,context):
    chunk=""
    chunk_id=1
    for i in context:
        if(len(chunk)<chunk_size):
            chunk +=i
        else: # edge case to be solved last chunk will not be embedded and stored
            embeddings = embedding_model.encode(chunk).tolist()
            embeddings_db.add(documents=[chunk],ids=[str(chunk_id)],embeddings=embeddings)
            chunk = ""
            chunk_id +=1
    else:
        print("chunking , embedding and storing successful")
    
def embedder(input_chunk):
    return embedding_model.encode(input_chunk).tolist()

def relevent_chunks_querier(query_embedding,n_results):
    return embeddings_db.query(query_embeddings=[query_embedding],n_results=n_results)

# STORING OF EMBEDDINGS OF THE MANUALLY ADDED CONTEXT FILE (CHAPTER 1 OF CHEM CLASS 12TH NCERT AS OF NOW)

# context = parse_doc(url)
# chunk_embed_store(chunk_size,context)

def chatbot(input_query,relevent_chunks):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "you are a chatbot designed to answer queries of the user strictly based ont the context provided "}, 
            {"role": "user", "content": f" relevent chunks which you have to stick while answering :{relevent_chunks}"},
            {"role": "user", "content": input_query}
        ]
    }
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    reply = response.json()["choices"][0]["message"]["content"]
    return reply


input_text="what is molarity?"
query_embedding= embedder(input_text)
result = relevent_chunks_querier(query_embedding,n_results)
relevent_chunks= result["documents"]
reply= chatbot(input_text,relevent_chunks)
print(reply)
print(f"this is the chunk which was relevant in you database{relevent_chunks}")
