from fastapi import APIRouter, status,HTTPException,UploadFile ,File
from .. import schemas
from .. logics import chat
router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post('/')
def upload_doc_router(query : schemas.Chat):
    if not query:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Please enter your query")
    
    return chat.final_reply(query.message,query.n_results)
        
