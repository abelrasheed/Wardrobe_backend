 # Helper libraries
import cv2
import numpy as np


from PIL import Image

def conversion_script(img2):

    # img2 = Image.open('D:\Source codes\AR wardrobe\AR-Backend\conversion\Cartoon version.png')
    pix = img2.load()

    print(img2.size)  # Get the width and hight of the image for iterating over
    print(pix[0,0])  # Get the RGBA Value of the a pixel of an imag

    col = list(pix[0,0])

    img2 = img2.convert("RGBA")

    datas = img2.getdata()
    newData = []
    for item in datas:
        if item[0] in range(col[0] - 15, col[0] + 15) and item[1] in range(col[1] - 15, col[1] + 15)  and item[2] in range(col[1] - 15, col[1] + 15) :
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)


    img2.putdata(newData)
    return img2