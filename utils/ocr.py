import pytesseract
from PIL import Image

def extract_text_labels(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text.split("\n")
