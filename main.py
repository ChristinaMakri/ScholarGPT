import os
from config.settings import OPENAI_API_KEY, PDFS_PATH, CHROMA_PERSIST_DIRECTORY
from utils.loader import load_pdfs_from_folder
from embeddings.embed_model import CustomEmbeddingModel
from vectorstore.chroma_store import create_chroma_vectorstore
from vectorstore.retriever import get_retriever
from memory.memory_manager import get_summary_memory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

def main():
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    print("Loading documents from PDFs...")
    documents = load_pdfs_from_folder(PDFS_PATH)

    print("Loading embedding model...")
    embedding_model = CustomEmbeddingModel()

    print("Creating vector store and embeddings...")
    vectordb = create_chroma_vectorstore(
        documents=documents,
        embedding_function=embedding_model.model.encode,  # Use sentence-transformers encode method
        persist_directory=CHROMA_PERSIST_DIRECTORY
    )

    print("Setting up retriever and conversation memory...")
    retriever = get_retriever(vectordb)
    memory = get_summary_memory()

    print("Loading chat model...")
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")

    print("Initializing conversational retrieval chain...")
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=False
    )

    print("Ready! Type your questions below (type 'exit' to quit).")

    while True:
        query = input("❓ Question: ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting.")
            break

        answer = qa_chain.run(query)
        print("🤖 Answer:", answer)

if __name__ == "__main__":
    main()
