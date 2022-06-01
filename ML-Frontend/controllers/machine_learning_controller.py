import base64

import requests
import io
from PIL import Image
from models.data_set_model import DataSet
api_version = 0.1

API_URL_2 = f"http://127.0.0.1:5001/toolbox/api/{api_version}/ml-result"


def get_variables(file_name):
    file = {'file': open(f"upload/{file_name}", 'rb')}
    response = requests.post(url="http://127.0.0.1:5001/toolbox/api/0.1/ml-variables", files=file)
    variables = response.json()
    return variables["Variables"]


def sent_train_data(independent_var_list, dependent_var, algorithm, file_name):
    data_set = DataSet()
    data_set.model_name = "Serkan"
    data_set.algorithm = algorithm
    data_set.independent_var_list = independent_var_list
    data_set.dependent_var = dependent_var
    data_set.file_name = file_name
    # train_data = {"independent_var_list": independent_var_list, "dependent_var": dependent_var, "file_name": file_name,
    #                "algorithm": algorithm}
    response = requests.post(url=API_URL_2, json=data_set.__dict__)
    results = response.json()
    img_data = results["image"]
    img_data = str.encode(img_data)
    im = Image.open(io.BytesIO(base64.b64decode(img_data)))
    im.save('static/images/image1.png', 'PNG')
    return results["train_result"]
