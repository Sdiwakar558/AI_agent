from fastapi import FastAPI,Request
from pydantic import BaseModel,Field
from typing import Annotated
from main import fetch_data_rag

app =FastAPI()

class User_input(BaseModel):
    question:Annotated[str,Field(description="user input should be in like",example="How are you?")]

@app.post('/')
async def ask_question(input:User_input):
    response=fetch_data_rag(input.question)
    return {'Answer':response}

