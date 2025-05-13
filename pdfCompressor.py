import subprocess
import sys
import os

def compress_pdf(input_path: str,
                 output_path: str,
                 quality: str = 'ebook') -> None:
    """
    PDF file compressor.

    @ Params
    ----------
    input_path : str
        Path to the original PDF file.
    output_path : str
        Path to the compressed PDF file.
    quality : str, optional
        Compression level. One of 'screen', 'ebook', 'printer', 'prepress', 'default'.
        Default: 'ebook'.
    """
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Input file not found: '{input_path}'")

    gs_settings = {
        'screen': '/screen',     
        'ebook': '/ebook',       
        'printer': '/printer',   
        'prepress': '/prepress',
        'default': '/default'    
    }

    if quality not in gs_settings:
        raise ValueError(f"quality must be one of {list(gs_settings.keys())}")

    gs_args = [
        'gs',
        '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        f"-dPDFSETTINGS={gs_settings[quality]}",
        '-dNOPAUSE',    # Don't pause between pages
        '-dBATCH',      # Exit after processing
        '-dQUIET',      # Suppress routine information output
        f"-sOutputFile={output_path}",
        input_path
    ]

    try:
        subprocess.run(gs_args, check=True)
        print(f"Compression complete: '{output_path}'")
    except subprocess.CalledProcessError as e:
        print("Error occurred while running Ghostscript.", file=sys.stderr)
        raise

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="PDF compression script using Ghostscript")
    parser.add_argument("input_pdf", help="Path to the source PDF file")
    parser.add_argument("output_pdf", help="Path where the compressed PDF will be saved")
    parser.add_argument("-q", "--quality",
                        choices=['screen', 'ebook', 'printer', 'prepress', 'default'],
                        default='ebook',
                        help="Compression quality level (default: ebook)")

    args = parser.parse_args()
    compress_pdf(args.input_pdf, args.output_pdf, args.quality)
