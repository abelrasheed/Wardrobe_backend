from flask_cors import CORS
from flask_restful import Api
from PIL import Image,ImageOps
import io
from flask import request,send_file,make_response,request,Flask,jsonify
from flask_restful import Resource
import numpy as np
from conversion import conversion
from base64 import encodebytes
import requests

app = Flask(__name__)

CORS(app)
api = Api(app)

class image_return(Resource):
    def get(self):
        
        pic_loc = "https://raw.githubusercontent.com/aldrinjenson/wardrobe-ar/master/assets/normal.jpeg"
        img_rgb = Image.open(requests.get(pic_loc, stream=True).raw)
        img_grey = ImageOps.grayscale(img_rgb)

        img_rbg = np.array(img_rgb)
        img_grey = np.array(img_grey)

        img_res = conversion(img_rbg,img_grey)

        img_byte_arr = io.BytesIO()
        img_res.save(img_byte_arr, format='png')

        encoded_img =  encodebytes(img_byte_arr.getvalue()).decode('ascii')
        # return send_file(
        #     img_byte_arr,
        #     mimetype='image/jpeg',
        #     as_attachment = True,
        #     attachment_filename='image.jpg'
        # )
        # response = make_response(img_byte_arr)
        # response.headers.set('Content-type','image/png')
        # response.headers.set(
        #     'Content-Disposition','attachment',filename='image.png'
        # )
        response =  { 'Status' : 'Success', 'message': "Ithenkilum nadakkuvo" , 'ImageBytes': encoded_img}
        return jsonify(response)


class home(Resource):
    def get(self, thing):
        test_return = {"Home" : "Homes"}
        
        return thing

api.add_resource(image_return, "/image")
api.add_resource(home, "/<string:thing>")








if __name__ == "__main__":
    app.run(debug=True)