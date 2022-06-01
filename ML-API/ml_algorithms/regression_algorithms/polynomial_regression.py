import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


class PolynomialRegressionAlg:
    def __init__(self, independent_features, dependent_feature):
        self.independent_features = independent_features
        self.dependent_feature = dependent_feature

    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.independent_features, self.dependent_feature,
                                                            test_size=1 / 3, random_state=123, shuffle=1)
        poly_reg = PolynomialFeatures(degree=2)
        X_poly = poly_reg.fit_transform(X_train)
        number_of_ind_var = len(X_train[1, :])
        shape_of_train_set = list()
        shape_of_train_set.append(number_of_ind_var+1)
        if number_of_ind_var > 1:
            difference = number_of_ind_var
            for index in range(0, number_of_ind_var-1):
                shape_of_train_set.append(shape_of_train_set[index] + difference)
                difference -= 1
        #print(shape_of_train_set)
        X_poly_2D = np.reshape(X_poly[:, shape_of_train_set], (-1, number_of_ind_var))
        model = LinearRegression()
        model.fit(X_poly_2D, y_train)
        results = {"Coefficients": model.coef_.tolist(), "Intercept": model.intercept_,
                   "R2": model.score(X_test, y_test)}
        return results

