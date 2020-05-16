import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Stepan\AppData\Local\Tesseract-OCR\tesseract.exe'
import os

def scan(path):
    filename = os.getcwd() + "\\" + str(path)
    print(path)
    text = pytesseract.image_to_string(filename, lang='rus')
    os.remove(filename)
    return (text)

# print(scan())
#
# import cv2
# import numpy as np
#
# image_file = "C:/Users/Stepan/Desktop/text.png"
# image = cv2.imread(image_file)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# edged = cv2.Canny(gray, 10, 250)
#
# cv2.imshow("Gray", gray)
# cv2.imshow("Edget", edged)
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
# closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
#
# cv2.imshow("Closed", closed)
#
# cnts, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# total = 0
#
# #for c in cnts:
# #    cv2.drawContours(image, [c] , -1, (0, 255, 0), 4)
#
# try: hierarchy = hierarchy[0]
# except: hierarchy = []
#
# height, width = closed.shape
# min_x, min_y = width, height
# max_x = max_y = 0
#
# parts = []
#
# for counter, hier in zip(cnts,hierarchy):
#     (x,y,w,h) = cv2.boundingRect(counter)
#     min_x, max_x = min(x, min_x), max(x+w, max_x)
#     min_y, max_y = min(y, min_y), max(y+h, max_y)
#     #cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
#     parts.append(image[y:y+h, x:x+h])
#
# cv2.imshow("Input", image)
#
# for part in parts:
#     print(pytesseract.image_to_string(part, lang='rus'))
#
# cv2.waitKey(0)
#
#
# def scan():
#     return 1