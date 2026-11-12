import chromadb
from embeddings import generate_embeddings

# Step 1: Connect to the existing ChromaDB database
client = chromadb.PersistentClient(path="./chroma_db")

# Step 2: Access the existing collection
collection = client.get_collection(name="medical_documents")

# Step 3: Get the user's question
question = "What are the common symptoms of diabetes?"

# Step 4: Convert the question into an embedding
query_embedding = generate_embeddings([question])

# Step 5: Search for the 3 most relevant chunks
results = collection.query(
    query_embeddings=query_embedding.tolist(),
    n_results=5
)

# Step 6: Display the retrieved chunks
for i, document in enumerate(results["documents"][0]):
    print(f"\nResult {i + 1}:")
    print(document)
    print("Distance:", results["distances"][0][i])