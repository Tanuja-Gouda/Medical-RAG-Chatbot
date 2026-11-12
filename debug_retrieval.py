import chromadb

from embeddings import generate_embeddings

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="medical_documents"
)

# Check how many chunks are stored
print("Total chunks:", collection.count())

# User question
question = "What are the common symptoms of diabetes?"

# Convert question into embedding
query_embedding = generate_embeddings([question])

# Retrieve relevant chunks
results = collection.query(
    query_embeddings=query_embedding.tolist(),
    n_results=5
)

# Display retrieved information
print("\n========== RETRIEVED RESULTS ==========")

for i, document in enumerate(results["documents"][0]):

    print(f"\nChunk {i + 1}:")
    print(document)

    print("Distance:", results["distances"][0][i])

    print("Metadata:", results["metadatas"][0][i])

print("\n=======================================")