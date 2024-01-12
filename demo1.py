import pytesseract
from pytesseract import Output
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
img_path1 = 'test2.png'

# text = pytesseract.image_to_string(img_path1,lang='jpn+eng')
# print(text)


# img = cv2.imread(img_path1)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow("result", img)
# cv2.waitKey(0)


def putText_japanese(img, text, point, size, color):
    #Notoフォントとする
    font = ImageFont.truetype('NotoSansCJK-Bold.ttc', size)

    #imgをndarrayからPILに変換
    img_pil = Image.fromarray(img)

    #drawインスタンス生成
    draw = ImageDraw.Draw(img_pil)

    #テキスト描画
    draw.text(point, text, fill=color, font=font)

    #PILからndarrayに変換して返す
    return np.array(img_pil)

######################################################################## detect text


# img = cv2.imread(img_path1)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print()
# hImg, wImg, _ = img.shape
# boxes = pytesseract.image_to_boxes(img_path1,lang='jpn')
# fontPIL = "Dflgs9.TTC"
# for b in boxes.splitlines():
#     # print(b)
#     b = b.split(" ")
#     print(b)
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img, (x,hImg - y), (w,hImg- h), (0,0,225), 1)
#     img = putText_japanese(img, b[0], (x, hImg-y-25), 5, (25, 131, 255))
######################################################################## detect text

    
img = cv2.imread(img_path1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img_path1,lang='jpn')
print(pytesseract.image_to_string(img_path1,lang='jpn'))
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
    # print(b)
        b = b.split()
        # print(b)
        if len(b) == 12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img, (x, y), (w +x,h+y), (0,0,225), 1)
            img = putText_japanese(img, b[11], (x, y+15), 10, (0, 0, 255))

cv2.imshow("result", img)

cv2.imwrite("result/"+ img_path1, img) 

cv2.waitKey(0)