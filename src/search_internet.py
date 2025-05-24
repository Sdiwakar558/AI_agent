from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
tavily_search = TavilyClient(api_key=TAVILY_API_KEY)
def search_internet(query:str):
    response = tavily_search.search(query,max_results=2)
    return response['results'][0]['content']