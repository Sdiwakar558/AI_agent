from langchain import hub
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader,WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import os
from src.embedidng_moddel import embedding_model

def read_n_embed_data(path):
    loaded_directory = DirectoryLoader(
            path= '.data/docs-pdf',
            glob='**/*.pdf*',
            loader_cls=PyPDFLoader)
    documents = loaded_directory.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    print("splitting documents")
    docs = text_splitter.split_documents(documents)

    embedding_model = embedding_model()
    print("vector_db step")
    vector_db = Chroma.from_documents(
        documents=docs,
        embedding=embedding_model,
        persist_directory='./chroma_db'
    )



