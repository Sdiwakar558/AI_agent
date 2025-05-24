from langchain import hub
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from src.embedidng_moddel import embedding_model
def search_query_db(user_input,v_path='./chroma_db'):
    v_db_path = v_path
    vector_db = Chroma(
        persist_directory=v_db_path,
        embedding_function= embedding_model())
    results = vector_db.similarity_search(user_input,k=3)
    return results