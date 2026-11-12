# from pypdf import PdfReader

# # Step 1: Provide the PDF file path
# pdf_path = "data/medical_documents/diabetes.pdf"

# # Step 2: Read the PDF
# reader = PdfReader(pdf_path)

# # Step 3: Extract text from all pages
# text = ""

# for page in reader.pages:
#     page_text = page.extract_text()

#     if page_text:
#         text += page_text + "\n"

# # Step 4: Display extracted text
# print("PDF loaded successfully!")
# print("\nExtracted Medical Information:\n")
# print(text)

# # Step 5: Display total characters
# print("\nTotal characters:", len(text))


from pypdf import PdfReader

def load_pdf(pdf_path):
  reader=PdfReader(pdf_path)
  text=""

  for page in reader.pages:
    page_text=page.extract_text()

    if page_text:
      text += page_text + "\n"

  return text