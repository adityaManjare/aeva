import chromadb
from sentence_transformers import SentenceTransformer
from . import chatbot , web_search
from .. import schemas

embedding_model = SentenceTransformer("multi-qa-MPNET-base-dot-v1")
client = chromadb.PersistentClient(path="./chroma_db")
embeddings_db = client.get_or_create_collection(name="embeddings") # this is the table for storing embeddings





def embedder(text:str):
    return embedding_model.encode(text).tolist()

def relevent_chunks_querier(query_embedding,n_results):
    return embeddings_db.query(query_embeddings=[query_embedding],n_results=n_results)

def final_reply(query:schemas.UserChat):
    if(query.search_mode == 'study_material'):
        result = relevent_chunks_querier(embedder(query.message),query.n_results)
        input_query = schemas.FinalChat(
            ans_mode=query.search_mode,
            original_query=query.message,
            context=result["documents"][0],
            metadata = result["metadatas"][0]
        )
        return chatbot.chatbot(input_query)
    if(query.search_mode =='web_search'):
        result = web_search.web_search(query.message)
        input_query = schemas.FinalChat(
            ans_mode=query.search_mode,
            original_query=query.message,
            context=[contxt["snippet"] for contxt in result["organic"][:query.n_results]],
            metadata = [{"title":meta["title"],"link":meta["link"]} for meta in result["organic"][query.n_results] ]
        )
        return chatbot.chatbot(input_query)
    else:
        return("invalid search mode please use either 'study_material' or 'web_search'")
