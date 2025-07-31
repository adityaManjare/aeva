import requests
from dotenv import load_dotenv
import os

load_dotenv()
search_url = "https://google.serper.dev/search"
X_API_KEY= os.getenv("X-API-KEY")


def web_search(query:str):
    headers = {"X-API-KEY":X_API_KEY}
    params ={"q":query}
    response = requests.get(search_url,json=params,headers=headers)
    results =response.json()
    return results