import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score


class LogisticRegressionAlg:
    def __init__(self, independent_features, dependent_feature):
        self.independent_features = independent_features
        self.dependent_feature = dependent_feature

    def save_model(self, model):
        filename = 'finalized_model.sav'
        pickle.dump(model, open(filename, 'wb'))

    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.independent_features, self.dependent_feature, test_size=1 / 3, random_state=123, shuffle=1)
        classifier = LogisticRegression(random_state=0)
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        # Making the Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        print(cm)
        accuracy_score(y_test, y_pred)
        results = {"Coefficients": "classifier.coef_.tolist()", "Intercept": "classifier.intercept_",
                   "R2": "classifier.score(X_test, y_test)"}
        #self.save_model(model)
        return results


# # Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)
# print(X_train)
# print(X_test)

# Training the Logistic Regression model on the Training set




