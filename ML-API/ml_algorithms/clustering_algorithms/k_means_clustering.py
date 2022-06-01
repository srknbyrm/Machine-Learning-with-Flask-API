# # Importing the libraries
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
#
# # Importing the dataset
# dataset = pd.read_csv('Mall_Customers.csv')
# X = dataset.iloc[:, [3, 4]].values
#
# # Using the elbow method to find the optimal number of clusters
# from sklearn.cluster import KMeans
# wcss = []
# for i in range(1, 11):
#     kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
#     kmeans.fit(X)
#     wcss.append(kmeans.inertia_)


# # Training the K-Means model on the dataset
# kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
# y_kmeans = kmeans.fit_predict(X)

