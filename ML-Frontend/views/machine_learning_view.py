import os
from flask import Blueprint, render_template, request
from controllers.machine_learning_controller import *

bp = Blueprint('machine_learning', __name__)

variable = list()
file_name = ""
modified_variable = False


@bp.route('/machine-learning', methods=['GET', 'POST'])
def machine_learning():
    if request.method == "GET":
        context_data = {
            "title": "NSH Toolbox",
            "Variables": 0
        }
        return render_template("machine_learning.html", **context_data)
    elif request.method == "POST":
        if request.files['file'].filename != "":
            file = request.files['file']
            global file_name
            file_name = file.filename
            file.save(os.path.join("upload", file.filename))
            #  print(file.filename)
            variables = get_variables(file_name=file.filename)
            variables_modified = list()
            for item in variables:
                if " " in item:
                    global modified_variable
                    modified_variable = True
                variables_modified.append(item.replace(" ", "_"))
            global variable
            variable = variables_modified
            context_data = {
                "Variables": variables_modified,
                "Length": len(variables)
            }
            return render_template("machine_learning.html", **context_data)


@bp.route('/machine-learning-train', methods=['GET', 'POST'])
def train_model():
    if request.method == "POST":
        selected_algo = request.form.get('form_select_algo')
        print(selected_algo)
        #  print(variable)
        checked_list = list()

        for item in variable:
            check = request.form.get(f'{item + "_check"}')
            checked_list.append(check)

        independent_var = list()
        #  print("checklist1")
        for item, checked in zip(variable, checked_list):
            if checked == "True":
                #  print(item, "--->", checked)
                independent_var.append(item)

        checked_list_2 = list()
        for item in variable:
            check = request.form.get(f'{item + "_check_2"}')
            checked_list_2.append(check)
        dependant_var = ""
        for item, checked in zip(variable, checked_list_2):
            if checked == "True":
                #  print(item, "--->", checked)
                dependant_var = item

        if modified_variable:
            dependant_var = dependant_var.replace("_", " ")
            for index in range(0, len(independent_var)):
                independent_var[index] = independent_var[index].replace("_", " ")

        print(selected_algo)
        results = sent_train_data(independent_var_list=independent_var, dependent_var=dependant_var,
                                  file_name=file_name, algorithm=selected_algo)
        # intercept = results["Intercept"]
        # equation = ""
        # index = 1
        #  print(results["Coefficients"])
        # r2 = results["R2"]
        # for item in results["Coefficients"]:
        #     equation = equation + f"X{index}*" + str(item)
        #     index += 1

        context_data = {
            "R2": results["R2"],
        }
        return render_template("ml_result.html", **context_data)
