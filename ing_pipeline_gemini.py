"""
Ingestion pipeline using Google Gemini embeddings (no OpenAI).
Set GOOGLE_API_KEY or GEMINI_API_KEY in .env with your Gemini API key.
"""
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader, DirectoryLoader

load_dotenv()


def load_files(doc_path="docs"):
    """Load all text files from the docs directory."""
    print(f"Loading files from {doc_path}")

    if not os.path.exists(doc_path):
        raise FileNotFoundError(
            f"Directory {doc_path} does not exist. Please create it and add your company files."
        )

    loader = DirectoryLoader(doc_path, glob="*.txt", loader_cls=TextLoader)
    documents = loader.load()
    if len(documents) == 0:
        raise FileNotFoundError(
            f"No files found in {doc_path}. Please add your company files in the {doc_path} directory."
        )
    # for i, doc in enumerate(documents[:2]):
    #     print(f"\nDocument {i+1} : ")
    #     print(f" Source : {doc.metadata['source']}")
    #     print(f" Content Length : {len(doc.page_content)} characters")
    #     print(f" Content Preview : {doc.page_content[:100]}...")
    #     print(f" Metadata : {doc.metadata}")

    return documents


def split_documents(documents, chunk_size=800, chunk_overlap=0):
    """Split the documents into smaller chunks with overlap."""
    print("Splitting documents into chunks")
    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_documents(documents)

    # if chunks :
    #     for i, chunk in enumerate(chunks[:5]):
    #         print(f"\nChunk {i+1} : ")
    #         print(f" Source : {chunk.metadata['source']}")
    #         print(f" Content Length : {len(chunk.page_content)} characters")
    #         print(f" Content Preview : {chunk.page_content}")
    #         print("-" * 50)
    #     if len(chunks) > 5:
    #         print(f"\n... and {len(chunks)-5} more chunks")

    return chunks


def create_vector_store(chunks, persist_directory="db/chroma_gemini"):
    """Create a persistent ChromaDB vector store using Gemini embeddings."""
    print("Creating embeddings and storing in ChromaDB...")

    # Use Gemini API key from env (GOOGLE_API_KEY or GEMINI_API_KEY)
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "Set GOOGLE_API_KEY or GEMINI_API_KEY in your .env file (Gemini API key from Google AI Studio)."
        )

    embedding_model = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=api_key,
    )

    print("Creating ChromaDB vector store with Gemini embeddings")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space": "cosine"},
    )
    print("----finished creating vector store----")
    print(f"Vector store created and saved to {persist_directory}")
    return vectorstore


def main():
    print("Main Function")
    #1. Loading the files
    documents = load_files()
    #2. Splitting the files
    chunks = split_documents(documents)
    #3. Embedding the files and storing in ChromaDB
    vectorstore = create_vector_store(chunks)


if __name__ == "__main__":
    main()
