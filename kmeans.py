import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('Mall_Customers.csv')

plt.figure()
plt.scatter(df['Age'], df['Spending Score (1-100)'], s=50)
plt.xlabel('Idade')
plt.ylabel('Score (1-100)')
plt.show()

x = df[['Age', 'Spending Score (1-100)']]

number_cluster = 5

model_kmeans = KMeans(n_clusters=number_cluster ,init="k-means++")

y_kmeans = model_kmeans.fit_predict(x)

color = ['r', 'b', 'g', 'k', 'y']

plt.figure()
for i in range(number_cluster):
    cluster = x[y_kmeans==i]
    plt.scatter(cluster['Age'], cluster['Spending Score (1-100)'], s=100, c=color[i], label = f'Cluster {i}')

plt.title('Grupo de Clientes')
plt.xlabel('Idade')
plt.ylabel('Score')
plt.grid()
plt.legend()
plt.show()