import cv2
from PIL import Image,ImageOps
import numpy as np
from cartoonize import cartoonize
from conversion_script import conversion_script


# img_rgb = Image.open("D:\Source codes\AR wardrobe\AR-Backend\conversion\download.jpg")
# img_grey = ImageOps.grayscale(img_rgb)
# img_rgb = np.array(img_rgb)
# img_grey = np.array(img_grey)

def conversion(img_rgb,img_grey):


    res = cartoonize(img_rgb,img_grey)

    res = Image.fromarray(res)
    res_final = conversion_script(res)
    return res_final 
    # res_final.save("finale.png", "PNG")
