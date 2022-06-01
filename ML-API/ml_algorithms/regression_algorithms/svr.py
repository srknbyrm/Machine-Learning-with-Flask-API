from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


class SVRAlg:
    def __init__(self, independent_features, dependent_feature):
        self.independent_features = independent_features
        self.dependent_feature = dependent_feature

    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.independent_features, self.dependent_feature,
                                                            test_size=1 / 3, random_state=123, shuffle=1)
        model = SVR(kernel='rbf')
        model.fit(X_train, y_train)
        print(X_train)
        print(X_test)
        prediction = model.predict(X_test)
        results = {"Coefficients": "model.coef_.tolist()", "Intercept": " model.intercept_",
                   "R2": model.score(X_test, y_test)}
        return results

    def plotter(self, X_train, y_train, model):
        # Visualising the SVR results
        plt.scatter(X_train, y_train, color='red')
        plt.plot(X_train, model.predict(X_train), color='blue')
        plt.title('(SVR)')
        plt.xlabel(self.independent_features)
        plt.ylabel(self.dependent_feature)
        plt.savefig()
