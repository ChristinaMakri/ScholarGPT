from langchain.document_loaders import PyPDFLoader
import os

def load_pdfs_from_folder(folder_path):
    """
    Load all PDF files from the specified folder and return documents.
    """
    documents = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder_path, filename))
            docs = loader.load()
            documents.extend(docs)
    return documents
