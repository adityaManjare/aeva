from fastapi import FastAPI
from .backend.routers import doc_processor, chatbot
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.include_router(doc_processor.router)
app.include_router(chatbot.router)

#setting up CORS such that my frontend can api call my backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://172.23.4.184:8080/"],
    allow_credentials=True,
    allow_methods=["*"],   # allow all HTTP methods: GET, POST...
    allow_headers=["*"],   # allow all headers


)