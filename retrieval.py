from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

db = Chroma(
    embedding_function=embedding_model, 
    persist_directory="db/chroma_gemini",
    collection_metadata={"hnsw:space": "cosine"}
    )
retriever = db.as_retriever(search_kwargs={"k": 3})
query = "What was NVIDIA's first graphics accelerator called?"

relevant_docs = retriever.invoke(query)
# print user query
print(f"User query: {query}")
for i,doc in enumerate(relevant_docs):
    print(f"Document {i}: \n{doc.page_content}\n")

# Synthetic Questions: 

# 1. "What was NVIDIA's first graphics accelerator called?"
# 2. "Which company did NVIDIA acquire to enter the mobile processor market?"
# 3. "What was Microsoft's first hardware product release?"
# 4. "How much did Microsoft pay to acquire GitHub?"
# 5. "In what year did Tesla begin production of the Roadster?"
# 6. "Who succeeded Ze'ev Drori as CEO in October 2008?"
# 7. "What was the name of the autonomous spaceport drone ship that achieved the first successful sea landing?"
# 8. "What was the original name of Microsoft before it became Microsoft?"