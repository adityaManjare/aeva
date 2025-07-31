from fastapi import FastAPI
from .backend import routers
from fastapi.middleware import CORSMiddleware

app = FastAPI()


app.include_router(routers.doc_processor.router)
app.include_router(routers.chatbot.router)

# setting up CORS such that my frontend can api call my backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://172.23.4.184:8080/"],
    allow_credentials=True,
    allow_methods=["*"],   # allow all HTTP methods: GET, POST...
    allow_headers=["*"],   # allow all headers


)