from fastapi import FastAPI
from .routers import doc_processor , chatbot

app = FastAPI()


app.include_router(doc_processor.router)
app.include_router(chatbot.router)