import json
import os
import pickle
import sys

from flask import Blueprint, jsonify, request, send_file
from controllers.machine_learning_controller import *
from models.data_set_model import DataSet
import io
import base64
from PIL import Image
from pympler.asizeof import asizeof

bp = Blueprint('machine_learning_view', __name__)
api_version = 0.1


@bp.route(f'/toolbox/api/{api_version}/ml-variables', methods=['POST'])
def machine_learning_view():
    # for item in request.files:
    #     print(item)
    files = request.files.getlist("file")
    for file in files:
        file.save(os.path.join("upload", file.filename))
        response = get_variables(file_name=file.filename)
    return jsonify({"Variables": response})


@bp.route(f'/toolbox/api/{api_version}/ml-result', methods=['POST'])
def ml_train():
    data = request.get_json()
    data_set = DataSet()
    data_set.__dict__ = data
    result = train(data_set=data_set)
    a = readimage("plots\\plot.png")
    img_data = img_new("plots\plot.png")
    img_data = img_data.decode()
    # img_data = str.encode(img_data)
    # im = Image.open(io.BytesIO(base64.b64decode(img_data)))
    # im.save('image1.png', 'PNG')
    #coded_img = get_encoded_img("plots\plot.png")
    #print("RESULT LENGTH"+ len(jsonify({"train_result": result, "image": img_data})))
    return jsonify({"train_result": result, "image": img_data})


def readimage(path):
    count = os.stat(path).st_size / 2
    with open(path, "rb") as f:
        return bytearray(f.read())


def get_encoded_img(image_path):
    img = Image.open(image_path, mode='r')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    my_encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
    return my_encoded_img

def img_new(image_path):
    with open(image_path, "rb") as image_file:
        data = base64.b64encode(image_file.read())
        return data


@bp.route(f'/deneme', methods=['GET'])
def deneme():
    data3 = {"menu": {
        "id": "file",
        "value": "File",
        "popup": {
            "menuitem": [
                {"value": "New", "onclick": "CreateNewDoc()"},
                {"value": "Open", "onclick": "OpenDoc()"},
                {"value": "Close", "onclick": "CloseDoc()"}
            ]
        }
    }}

    data2 = {"widget": {
        "debug": "on",
        "window": {
            "title": "Sample Konfabulator Widget",
            "name": "main_window",
            "width": 500,
            "height": 500
        },
        "image": {
            "src": "Images/Sun.png",
            "name": "sun1",
            "hOffset": 250,
            "vOffset": 250,
            "alignment": "center"
        },
        "text": {
            "data": "Click Here",
            "size": 36,
            "style": "bold",
            "name": "text1",
            "hOffset": 250,
            "vOffset": 100,
            "alignment": "center",
            "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
        }
    }}

    byte = pickle.dumps(data3)
    print(sys.getsizeof(byte))
    result = list()
    index = 0
    for index in range(1, 10001):
        result.append(data3)
    #return bytearray(byte)
    byte = pickle.dumps(result)
    size_of_data3 = asizeof({'result': result})
    print(size_of_data3)
    return {'result': result}
