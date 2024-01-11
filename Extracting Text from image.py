try:
    from PIL import Image #try import image from PIL, if it shows any error, try import image.
except ImportError:
    import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

info = recText('C:/Users/OWNER/Desktop/AI PS/sample 16/TEST2.png')
print(info)
file = open("C:/Users/OWNER/Desktop/AI PS/sample 16/result.txt","w")#write the text and overwrite
file.write(info)
file.close()
print("Written Successful")
