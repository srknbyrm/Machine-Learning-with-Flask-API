from data_prep.data_preparation import DataPreparation
from ml_algorithms.regression_algorithms.linear_regression import *
from ml_algorithms.regression_algorithms.polynomial_regression import *
from ml_algorithms.regression_algorithms.svr import *
from ml_algorithms.regression_algorithms.decision_tree_regression import *
from ml_algorithms.regression_algorithms.random_forest_regression import *
from ml_algorithms.classification_algorithms.random_forest_classification import *
from ml_algorithms.classification_algorithms.decision_tree_classification import *
from ml_algorithms.classification_algorithms.naive_bayes import *
from ml_algorithms.classification_algorithms.kernel_svm import *
from ml_algorithms.classification_algorithms.k_nearest_neighbors import *
from ml_algorithms.classification_algorithms.logistic_regression import *
from ml_algorithms.classification_algorithms.support_vector_machine import *
from ml_algorithms.clustering_algorithms.k_means_clustering import *
from ml_algorithms.clustering_algorithms.hierarchical_clustering import *

from models.data_set_model import *


class AlgorithmManager:
    def __init__(self, data_set: DataSet):
        self.data_set = data_set
        dp = DataPreparation(file_name=self.data_set.file_name, independent_var_list=self.data_set.independent_var_list,
                             dependent_var=self.data_set.dependent_var)
        self.x, self.y = dp.split_data()

    def algorithm_selector(self):
        if self.data_set.algorithm == "linear_regression":
            print('linear reg')
            linear_reg = LinearRegressionAlg(dependent_feature_name=self.data_set.dependent_var,
                                             independent_feature_name=self.data_set.independent_var_list,
                                             dependent_feature=self.y, independent_features=self.x)
            result = linear_reg.train()
            print(result)
            return result
        elif self.data_set.algorithm == "polynomial_regression":
            poly_reg = PolynomialRegressionAlg(dependent_feature=self.y, independent_features=self.x)
            result = poly_reg.train()
            return result
        elif self.data_set.algorithm == "svr":
            svr = SVRAlg(dependent_feature=self.y, independent_features=self.x)
            result = svr.train()
            return result
        elif self.data_set.algorithm == "decision_tree_regression":
            dta = DecisionTreeAlg(dependent_feature=self.y, independent_features=self.x)
            result = dta.train()
            return result
        elif self.data_set.algorithm == "random_forest_regression":
            random_forest_regression = RandomForestAlg(dependent_feature=self.y, independent_features=self.x)
            result = random_forest_regression.train()
            return result

        ###################### Classification ############################

        elif self.data_set.algorithm == "random_forest_classification":
            random_forest_classification = RandomForestClassificationAlg(dependent_feature=self.y, independent_features=self.x)
            result = random_forest_classification.train()
            return result
        elif self.data_set.algorithm == "naive_bayes":
            naive_bayes = NaiveBayesAlg(dependent_feature=self.y, independent_features=self.x)
            result = naive_bayes.train()
            return result
        elif self.data_set.algorithm == "kernel_svm":
            kernel_svm = KernelSVMAlg(dependent_feature=self.y, independent_features=self.x)
            result = kernel_svm.train()
            return result
        elif self.data_set.algorithm == "k_nearest_neighbors":
            k_nearest_neighbors = KNeighborsClassificationAlg(dependent_feature=self.y, independent_features=self.x)
            result = k_nearest_neighbors.train()
            return result
        elif self.data_set.algorithm == "logistic_regression":
            print("logistic")
            logistic_regression = LogisticRegressionAlg(dependent_feature=self.y, independent_features=self.x)
            result = logistic_regression.train()
            return result
        elif self.data_set.algorithm == "support_vector_machine":
            support_vector_machine = SupportVectorMachineAlg(dependent_feature=self.y, independent_features=self.x)
            result = support_vector_machine.train()
            return result

        ###################### Clustering ############################

        elif self.data_set.algorithm == "k_means_clustering":
            random_forest_regression = RandomForestAlg(dependent_feature=self.y, independent_features=self.x)
            result = random_forest_regression.train()
            return result
        elif self.data_set.algorithm == "hierarchical_clustering":
            random_forest_regression = RandomForestAlg(dependent_feature=self.y, independent_features=self.x)
            result = random_forest_regression.train()
            return result
