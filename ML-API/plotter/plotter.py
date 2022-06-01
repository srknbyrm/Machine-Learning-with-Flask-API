import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, x, y, dependent_feature_name, independent_feature_name, dependent_feature, independent_features, model):
        self.x = x
        self.y = y
        self.model = model
        self.dependent_feature = dependent_feature
        self.independent_features = independent_features
        self.dependent_feature_name = dependent_feature_name
        self.independent_feature_name = independent_feature_name

    def plotter(self):
        print("X is : ", self.x)
        print("Y is : ", self.dependent_feature)
        print(self.independent_features)

        plt.scatter(self.x, self.y, color='red')
        plt.plot(self.x, self.model.predict(self.x), color='blue')
        plt.title('Linear Regression')
        plt.xlabel(self.independent_feature_name[0])
        plt.ylabel(self.dependent_feature_name)
        plt.savefig("plots\\plot.png")
