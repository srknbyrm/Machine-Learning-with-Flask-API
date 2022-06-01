import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


class DataPreparation:
    def __init__(self, file_name, independent_var_list, dependent_var):
        self.file_name = file_name
        self.independent_var_list = independent_var_list
        self.dependent_var = dependent_var
        self.data = pd.read_csv(f'upload/{file_name}')
        self.df = pd.DataFrame(self.data)

    def split_data(self):
        index_of_independent = list()
        for index in range(len(self.df.columns)):
            for independent_var in self.independent_var_list:
                if independent_var == self.df.columns[index]:
                    index_of_independent.append(index)
        # print(index_of_independent)
        # print("dependant" + self.dependent_var)
        # print(index_of_independent)
        self.handle_null_values()
        x = self.data.iloc[:, :].values
        if self.find_categorical_features():
            x = self.handle_categorical_data(x_data_set=x)
        #print(x)
        x = x[:, index_of_independent]
        #print(x)
        # print(self.find_categorical_features())
        y = self.data.loc[:, self.dependent_var].values
        return x, y

    def feature_scaled_split(self):
        x, y = self.split_data()
        sc_x = StandardScaler()
        sc_y = StandardScaler()
        x = sc_x.fit_transform(x)
        y = sc_y.fit_transform(y)
        return x, y

    def handle_null_values(self):
        """ Go back here is it really necessary check null values """
        null_check_df = self.data.isnull()
        check_null = False
        for item in null_check_df:
            for value in null_check_df[item]:
                if value == True:
                    print("here")
                    check_null = True
        print(check_null)
        if check_null:
            self.data = self.data.dropna(how="any")

    def find_categorical_features(self):
        categorical_features = list()
        for index in range(len(self.df.columns)):
            for value in self.df[self.df.columns[index]]:
                if type(value) == str:
                    categorical_features.append(index)
        categorical_features = set(categorical_features)
        categorical_features = list(categorical_features)
        return categorical_features

    def handle_categorical_data(self, x_data_set):
        le = LabelEncoder()
        categorical_features = self.find_categorical_features()
        print(categorical_features)
        for item in categorical_features:
            x_data_set[:, item] = le.fit_transform(x_data_set[:, item])
        return x_data_set
