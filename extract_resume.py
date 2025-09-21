#!/usr/bin/env python3
"""
Extract text content from CV PDF
"""

import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file"""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def main():
    # Try both possible locations
    pdf_paths = [
        'static/files/CV_Innocent Nzimenyera.pdf',
        'static/media/CV_Innocent Nzimenyera.pdf'
    ]
    
    for pdf_path in pdf_paths:
        if os.path.exists(pdf_path):
            print(f"Reading CV from: {pdf_path}")
            text = extract_text_from_pdf(pdf_path)
            if text:
                print("CV Content:")
                print("=" * 50)
                print(text)
                print("=" * 50)
                
                # Save to file for reference
                with open('cv_content.txt', 'w', encoding='utf-8') as f:
                    f.write(text)
                print("\nCV content saved to cv_content.txt")
                return
    
    print("CV file not found in expected locations")

if __name__ == "__main__":
    main()
