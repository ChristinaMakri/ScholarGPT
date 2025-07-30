from langchain.vectorstores import Chroma
from langchain.schema import Document
import os

def create_chroma_vectorstore(documents, embedding_function, persist_directory):
    vectordb = Chroma.from_documents(
        documents,
        embedding_function,
        persist_directory=persist_directory
    )
    return vectordb
