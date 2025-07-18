from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf_with_images(pdf_path):
    text = ''
    images = convert_from_path(pdf_path)
    for image in images:
        image_text = pytesseract.image_to_string(image)
        text += image_text
    return text

# Path to your PDF file
pdf_path = 'volumes.pdf'

# Extract text from PDF with images
text_with_images = extract_text_from_pdf_with_images(pdf_path)

print(text_with_images)
