from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from src.fetch_data_vdb import search_query_db
from src.build_llm import llm_model

def custom_prompt():
    prompt = """
        You are an intelligent assistant answering questions based only on the provided context. Do not use any external knowledge.
        Context:{context}
        Question:{question}
        Answer:
        """
    rag_prompt = PromptTemplate(input_variables=["context", "question"],template=prompt)
    return rag_prompt
def formate_documents(docs):
    return '\n\n'.join(doc.page_content for doc in docs)
def rag_chain():
    rag_chain = (
        {
            "context": RunnableLambda(lambda x: formate_documents(search_query_db(x["question"]))),
            "question": RunnablePassthrough()
        }
        |custom_prompt()|llm_model()|StrOutputParser()
        )
    return rag_chain

