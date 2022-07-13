import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import pyautogui
import numpy

def read_text(img):
    img0 = numpy.array(img)
    text = pytesseract.image_to_string(img0)
    return text.lower()

im = pyautogui.screenshot()
im1 = im.crop((700, 300, 888, 349))
#im1.show()
text = read_text(im1)
text = text.split('$')[1]
text = text.split('\n\x0c')[0]
print(text)

"""
img = numpy.asarray(im1)
text = pytesseract.image_to_string(img)
print(text)
"""



#imge = cv2.imread('money.png')
