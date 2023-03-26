import cv2
import pytesseract




img =cv2.imread('a.png')

text=pytesseract.image_to_string(img)
print(text)

text=text.replace('?', '')
text=text.replace('%', '/')
text=text.replace('x', '*')
text=text.replace('=', ' ')

print(text)
print (eval(text))