import pandas as pd
from ml_algorithms.algorithm_manager import AlgorithmManager
from models.data_set_model import DataSet


def get_variables(file_name):
    # in macos its / but in windows \
    data = pd.read_csv(f'upload/{file_name}')
    context_list = list()
    for item in data.columns:
        context_list.append(item)
    return context_list


def train(data_set: DataSet):
    algorithm_manager = AlgorithmManager(data_set=data_set)
    results = algorithm_manager.algorithm_selector()
    return results
