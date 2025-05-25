from src.data_feeding_llm import rag_chain
from src.embed_new_data import read_n_embed_data
import os
def fetch_data_rag(user_input):
    if os.path.exists('./chroma_db'):
        pass
    else:
        read_n_embed_data()
    response = rag_chain().invoke({'question':user_input})
    return response

