
import chromadb

from document_loader import load_pdf
from text_splitter import split_text
from embeddings import generate_embeddings

# Step 1: Load PDF
text = load_pdf("data/medical_documents/diabetes_symptoms.pdf")

# Step 2: Split text
chunks = split_text(text)

# Step 3: Extract chunk text
chunk_texts = [chunk.page_content for chunk in chunks]

# Step 4: Generate embeddings using our function
embeddings = generate_embeddings(chunk_texts)

# Step 5: Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="medical_documents",
    metadata={"hnsw:space": "cosine"}
)

# Step 6: Generate IDs
ids = [f"diabetes_chunk_{i}" for i in range(len(chunks))]

# Step 7: Generate metadata
metadatas = [
    {
        "source": "diabetes_symptoms.pdf",
        "chunk_number": i
    }
    for i in range(len(chunks))
]

# Step 8: Store existing embeddings
collection.upsert(
    ids=ids,
    documents=chunk_texts,
    embeddings=embeddings.tolist(),
    metadatas=metadatas
)

print("Documents stored successfully!")
print("Total stored chunks:", collection.count())
