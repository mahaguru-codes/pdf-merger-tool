from pypdf import PdfReader, PdfWriter
import os

def merge_pdfs(pdf_paths, output_path):
    writer = PdfWriter()
    
    for path in pdf_paths:
        if os.path.exists(path) and path.lower().endswith(".pdf"):
            try:
                reader = PdfReader(path)
                for page in reader.pages:
                    writer.add_page(page)
            except Exception as e:
                print(f"Failed to read {path}: {e}")
        else:
            print(f"Invalid file: {path}")
    
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    print(f"Merged PDF saved to: {output_path}")
