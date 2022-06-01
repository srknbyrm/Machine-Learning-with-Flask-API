class DataSet:
    def __init__(self):
        self.model_name = ""
        self.independent_var_list = list()
        self.dependent_var = ""
        self.file_name = ""
        self.algorithm = ""

    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, model_name_param):
        self._model_name = model_name_param

    @property
    def independent_var_list(self):
        return self._independent_var_list

    @independent_var_list.setter
    def independent_var_list(self, independent_var_list_param):
        self._independent_var_list = independent_var_list_param

    @property
    def dependent_var(self):
        return self._dependent_var

    @dependent_var.setter
    def dependent_var(self, dependent_var_param):
        self._dependent_var = dependent_var_param

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, file_name_param):
        self._file_name = file_name_param

    @property
    def algorithm(self):
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm_param):
        self._algorithm = algorithm_param
