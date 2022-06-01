from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


class RandomForestAlg:
    def __init__(self, independent_features, dependent_feature):
        self.independent_features = independent_features
        self.dependent_feature = dependent_feature

    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.independent_features, self.dependent_feature, test_size=1 / 3, random_state=123, shuffle=1)
        model = RandomForestRegressor(n_estimators = 10, random_state = 0)
        model.fit(X_train, y_train)
        print(X_train)
        print(X_test)
        prediction = model.predict(X_test)
        results = {"Coefficients": "No Coefficient", "Intercept": "No Intercept",
                   "R2": model.score(X_test, y_test)}
        return results
