from src.data_feeding_llm import rag_chain

def fetch_data_rag(user_input):
    response = rag_chain().invoke({'question':user_input})
    return response

