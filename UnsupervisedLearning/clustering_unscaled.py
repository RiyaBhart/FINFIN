import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Example vehicle data
data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)
df_clustering = pd.get_dummies(df,columns=['vehicle_type'],drop_first=True)

x= df_clustering.values
wcss=[]

for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method Graph')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.show()


kmeans_noscaling = KMeans(n_clusters=2, init='k-means++', random_state=42)
y_predict = kmeans_noscaling.fit_predict(x)


plt.figure(figsize=(8, 6))
for cluster in np.unique(y_predict):
    plt.scatter(
        x[y_predict == cluster, 1],
        x[y_predict == cluster, 3],
        s=100,
        label=f'Cluster {cluster + 1}'
    )

plt.xlabel('Mileage')
plt.ylabel('Maintenance Cost')
plt.title('K-Means Clustering (No Scaling)')
plt.legend()
plt.show()
