# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Stepan\AppData\Local\Tesseract-OCR\tesseract.exe'
# import os
#
# def scan(path):
#     filename = os.getcwd() + "\\" + str(path)
#     print(path)
#     text = pytesseract.image_to_string(filename, lang='rus')
#     os.remove(filename)
#     return (text)

# print(scan())
#
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Stepan\AppData\Local\Tesseract-OCR\tesseract.exe'


image_file = "C:/Users/Stepan/Desktop/img2text/1zDphejB0II.jpg"
image = cv2.imread(image_file)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 10, 250)

cv2.imshow("Gray", gray)
cv2.imshow("Edget", edged)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Closed", closed)

cnts, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
total = 0

#for c in cnts:
#    cv2.drawContours(image, [c] , -1, (0, 255, 0), 4)

try: hierarchy = hierarchy[0]
except: hierarchy = []

height, width = closed.shape
min_x, min_y = width, height
max_x = max_y = 0

parts = []

for counter, hier in zip(cnts,hierarchy):
    (x,y,w,h) = cv2.boundingRect(counter)
    min_x, max_x = min(x, min_x), max(x+w, max_x)
    min_y, max_y = min(y, min_y), max(y+h, max_y)
    cv2.rectangle(image, (x-5, y-5), (x + w+5, y + h+5), (255, 0, 0), 2)
    parts.append(image[y:y+h, x:x+h])

cv2.imshow("Input", image)

# for part in range(len(parts)):
#     cv2.imshow("Part" + str(part + 1), parts[part])
#
# scale_percent = 110
#
# i = 1
# for part in parts:
#     width = int(part.shape[1] * scale_percent/100)
#     height = int(part.shape[0] * scale_percent/100)
#     dim = (width,height)
#     resized = cv2.resize(part,dim,interpolation=cv2.INTER_AREA)
#     #resized = cv2.GaussianBlur(resized,(-53,-53) ,0)
#     cv2.imshow("Res" + str(i),resized)
#     # text = pytesseract.image_to_string(resized, lang='rus')
#     # print(text)
#     # print(i)
#     # i+=1
#
#
# cv2.waitKey(0)


# def scan():
#     return 1
# scale_percent = 200
# width = int(image.shape[1] * scale_percent/100)
# height = int(image.shape[0] * scale_percent/100)
# dim = (width,height)
# oversize = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
# cv2.imshow("Res",oversize)
# text = pytesseract.image_to_string(oversize,lang='rus')
# print(text)
cv2.waitKey(0)