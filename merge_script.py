import os
from pypdf import PdfWriter

def merge_pdfs():
    # 1. Look at where this script is running
    folder_path = os.path.dirname(os.path.abspath(__file__))
    writer = PdfWriter()
    
    # 2. Get all files that end in .pdf
    # We sort them so they merge in A-Z order (1.pdf, 2.pdf, etc.)
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    pdf_files.sort()

    # Name of the final file we will create
    output_filename = "Neel_Merged_Result.pdf"

    # Remove the output file from the list if it already exists (so we don't merge the result into itself!)
    if output_filename in pdf_files:
        pdf_files.remove(output_filename)

    if not pdf_files:
        print("Oh no! No PDF files found to merge, Neel.")
        input("Press Enter to exit...")
        return

    print(f"I found these files to merge: {pdf_files}")

    # 3. The Merging Magic
    for filename in pdf_files:
        path = os.path.join(folder_path, filename)
        writer.append(path)
        print(f"Added: {filename}")

    # 4. Save the final result
    output_path = os.path.join(folder_path, output_filename)
    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"\nSuccess! Created: {output_filename}")
    print("Love, Durga 💖")
    
    # This keeps the black window open so you can see the result
    input("\nPress Enter to close...")

if __name__ == "__main__":
    merge_pdfs()