import os
import subprocess

def compress_pdf_ghostscript(input_path, output_path, dpi=150):
    """
    Compress a PDF using Ghostscript.
    
    Parameters:
    - input_path: path to original PDF
    - output_path: path to save compressed PDF
    - dpi: target resolution for images (150 is usually good balance)
    """
    try:
        subprocess.run([
            "gs",
            "-sDEVICE=pdfwrite",
            f"-dPDFSETTINGS=/screen",  # /screen = low-res, /ebook = medium, /prepress = high-quality
            "-dNOPAUSE",
            "-dBATCH",
            "-dQUIET",
            f"-sOutputFile={output_path}",
            input_path
        ], check=True)
        print(f"Compressed: {os.path.basename(input_path)} -> {os.path.basename(output_path)}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to compress {input_path}: {e}")

def compress_all_pdfs_ghostscript(folder_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(output_folder, filename)
            compress_pdf_ghostscript(input_file, output_file)

# Example usage
input_folder = "Dataset"
output_folder = "Dataset/Narkotika_compressed"

compress_all_pdfs_ghostscript(input_folder, output_folder)
