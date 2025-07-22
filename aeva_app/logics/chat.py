import chromadb
from sentence_transformers import SentenceTransformer
from . import chatbot

embedding_model = SentenceTransformer("multi-qa-MPNET-base-dot-v1")
client = chromadb.PersistentClient(path="./chroma_db")
embeddings_db = client.get_or_create_collection(name="embeddings") # this is the table for storing embeddings





def embedder(input_chunk):
    return embedding_model.encode(input_chunk).tolist()

def relevent_chunks_querier(query_embedding,n_results):
    return embeddings_db.query(query_embeddings=[query_embedding],n_results=n_results)

def final_reply(input_chunk,n_results):
    return chatbot.chatbot(input_chunk,relevent_chunks_querier(embedder(input_chunk),n_results))

