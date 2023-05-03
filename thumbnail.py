import os
import sys
from pdf2image import convert_from_path
from PIL import Image

def convert_first_page_to_image(pdf_path, output_directory):
    images = convert_from_path(pdf_path, dpi=200, first_page=1, last_page=1)
    if images:
        images[0].save(os.path.join(output_directory, f"{os.path.splitext(os.path.basename(pdf_path))[0]}.jpg"), "JPEG")

def convert_pdfs_in_directory(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_directory, filename)
            convert_first_page_to_image(pdf_path, output_directory)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_directory> <output_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]

    if not os.path.isdir(input_directory):
        print(f"Error: {input_directory} is not a directory.")
        sys.exit(1)

    convert_pdfs_in_directory(input_directory, output_directory)

