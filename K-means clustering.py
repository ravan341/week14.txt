#First install the necessary libraries
!pip install pandas numpy scikit-learn matplotlib seaborn


# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'heart.csv' with your dataset path)
data = pd.read_csv('heart.csv')

# Inspecting the first few rows of the dataset
print(data.head())

# Preprocessing: Extracting the features for clustering
# Dropping target column if present (if target column is named 'target' or 'outcome')
if 'target' in data.columns:
    X = data.drop(columns=['target'])
else:
    X = data


# Scaling the data (K-Means performs better with scaled data)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Running K-Means algorithm (choosing 2 clusters for heart disease: yes/no)
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X_scaled)

# Getting the cluster labels
clusters = kmeans.labels_

# Adding the cluster labels to the dataset
data['Cluster'] = clusters

# Visualizing the clusters using a pair plot (optional, for a quick view of clustering results)
sns.pairplot(data, hue='Cluster', palette='coolwarm')
plt.show()

# Elbow Method to find the optimal number of clusters
inertia = []
for n in range(1, 11):
    kmeans = KMeans(n_clusters=n, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plotting the elbow curve
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()
