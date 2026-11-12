# from document_loader import load_pdf

# from langchain_text_splitters import RecursiveCharacterTextSplitter

# # Step 1: Load extracted text
# text = load_pdf("data/medical_documents/diabetes.pdf")

# # Step 2: Create text splitter
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,
#     chunk_overlap=50
# )

# # Step 3: Split the text
# chunks = text_splitter.create_documents([text])

# # Step 4: Display chunks
# print("Total chunks:", len(chunks))

# for i, chunk in enumerate(chunks):
#     print(f"\nChunk {i + 1}:")
#     print(chunk.page_content)



from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(text):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.create_documents([text])

    return chunks
