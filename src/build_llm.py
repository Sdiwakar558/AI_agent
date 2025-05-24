from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

GROQ_API_KEY =os.getenv("GROQ_API_KEY")
def llm_model(model='meta-llama/llama-4-scout-17b-16e-instruct',temperature=0):
    llm = ChatGroq(model=model,temperature=temperature)
    return llm