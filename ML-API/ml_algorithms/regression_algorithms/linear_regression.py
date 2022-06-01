import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from plotter.plotter import Plotter


class LinearRegressionAlg:
    def __init__(self, dependent_feature_name, independent_feature_name, independent_features, dependent_feature):
        self.independent_features = independent_features
        self.dependent_feature = dependent_feature
        self.dependent_feature_name = dependent_feature_name
        self.independent_feature_name = independent_feature_name

    def save_model(self, model):
        filename = 'finalized_model.sav'
        pickle.dump(model, open(filename, 'wb'))

    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.independent_features, self.dependent_feature,
                                                            test_size=1 / 3, random_state=123, shuffle=1)
        model = LinearRegression()
        model.fit(X_train, y_train)
        # print(X_train)
        # print(X_test)
        prediction = model.predict(X_test)
        plotter = Plotter(x=X_train, y=y_train, model= model, independent_features=self.independent_features[0],
                          dependent_feature=self.dependent_feature, dependent_feature_name=self.dependent_feature_name,
                          independent_feature_name=self.independent_feature_name)
        plotter.plotter()
        results = {"Coefficients": model.coef_.tolist(), "Intercept": model.intercept_,
                   "R2": model.score(X_test, y_test)}
        #self.save_model(model)
        return results


