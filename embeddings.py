
# from sentence_transformers import SentenceTransformer

# from document_loader import load_pdf
# from text_splitter import split_text

# # Step 1: Load the medical PDF
# text = load_pdf("data/medical_documents/diabetes.pdf")

# # Step 2: Split the extracted text
# chunks = split_text(text)

# # Step 3: Load the embedding model
# model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# # Step 4: Extract text from each chunk
# chunk_texts = [chunk.page_content for chunk in chunks]

# # Step 5: Generate embeddings
# embeddings = model.encode(chunk_texts)

# # Step 6: Display results
# print("Total chunks:", len(chunks))

# print("Embedding shape:", embeddings.shape)

# print("\nFirst chunk:")
# print(chunk_texts[0])

# print("\nFirst chunk embedding:")
# print(embeddings[0])

# print("\nEmbedding generation completed!")



from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def generate_embeddings(texts):
    embeddings = model.encode(texts)

    return embeddings
