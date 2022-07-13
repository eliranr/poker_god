from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#im = Image.open(r"new_img\call33.png")

def theReds(img):
    im1 = img.crop((1120, 800, 1230, 878))
    #im1.show()
    list = pytesseract.image_to_string(im1).split()
    print(list)
    text = list[0]
    money = ''
    if len(list) == 2:
        money = list[1]
        money = money.replace('$', '')
        money = float(money)
        print(money)

    return {
        'text': text,
        'money': money
    }
#theReds(im)



def getPot(img):
    im1 = img.crop((819, 322, 890, 352))
    text = pytesseract.image_to_string(im1).split()[0]
    text = text.replace('$', '')
    text = float(text)
    return text
