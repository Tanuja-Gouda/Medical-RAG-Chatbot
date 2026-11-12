import chromadb

from embeddings import generate_embeddings
from llm import generate_answer


# Step 1: Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="medical_documents"
)


# Step 2: Create the chatbot function
def ask_question(question):

    # Convert user question into embedding
    query_embedding = generate_embeddings([question])

    # Search ChromaDB
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=3
    )

    # Get retrieved document chunks
    retrieved_chunks = results["documents"][0]

    if not retrieved_chunks:
        return "I could not find relevant information in the medical documents."

    # Combine chunks into one context
    context = "\n\n".join(retrieved_chunks)

    # Generate answer using Gemini
    answer = generate_answer(question, context)

    # Return answer and source information
    sources = results["metadatas"][0]

    return answer, sources


# Step 3: Ask the user for a question
# question = input("Ask your medical question: ")

# answer, sources = ask_question(question)

# print("\nChatbot Answer:")
# print(answer)

# print("\nSources:")
# for source in sources:
#     print(
#         "File:", source["source"],
#         "| Chunk:", source["chunk_number"]
#     )

if __name__ == "__main__":

    question = input("Ask your medical question: ")

    answer, sources = ask_question(question)

    print("\nChatbot Answer:")
    print(answer)

    print("\nSources:")

    for source in sources:
        print(
            "File:", source["source"],
            "| Chunk:", source["chunk_number"]
        )