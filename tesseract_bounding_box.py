import pytesseract
from pytesseract import Output
import cv2
img = cv2.imread('images\\dove_soap\\3.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

d = pytesseract.image_to_data(gray, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

print(d)
cv2.imshow('img', img)
cv2.imshow('gray', gray)

cv2.waitKey(0)
