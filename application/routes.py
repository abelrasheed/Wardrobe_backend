from PIL import Image,ImageOps
import numpy
import io
from flask import request,send_file,make_response,request
from flask_restful import Resource

from application import api
import numpy as np
from application.conversion import conversion



class image_return(Resource):
    def post(self):
        pic = request.files['pic']

        if not pic :
            return "No image uploaded",400

        
        img_rgb = Image.open(pic)
        img_grey = ImageOps.grayscale(img_rgb)

        img_rbg = np.array(img_rgb)
        img_grey = np.array(img_grey)

        img_res = conversion(img_rbg,img_grey)

        img_byte_arr = io.BytesIO()
        img_res.save(img_byte_arr, format='png')

        img_byte_arr = img_byte_arr.getvalue()
        # return send_file(
        #     img_byte_arr,
        #     mimetype='image/jpeg',
        #     as_attachment = True,
        #     attachment_filename='image.jpg'
        # )
        response = make_response(img_byte_arr)
        response.headers.set('Content-type','image/png')
        response.headers.set(
            'Content-Disposition','attachment',filename='image.png'
        )
        return response


class home(Resource):
    def get(self):
        return "Home"

api.add_resource(image_return, "/image")
api.add_resource(home, "/")


