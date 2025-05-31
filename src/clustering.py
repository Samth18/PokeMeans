import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def cluster_pokemon(data, n_clusters=3):
    # Seleccionar características y escalar
    X = data[['attack_index']].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Aplicar K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(X_scaled)
    
    # Asignar clusters
    data['cluster'] = clusters
    
    # Renombrar clusters según tu criterio
    cluster_names = {
        0: 'Balanced',
        1: 'Aggressive',
        2: 'Defensive'
    }
    
    data['cluster_name'] = data['cluster'].map(cluster_names)
    
    return data

def apply_clustering_to_all(non_legendary, legendary):
    # Cluster para no legendarios
    non_legendary = cluster_pokemon(non_legendary)
    
    # Cluster para legendarios (mismo criterio)
    legendary = cluster_pokemon(legendary)
    legendary['cluster'] += 3  # Para tener clusters 3,4,5
    legendary['cluster_name'] = legendary['cluster_name'] + ' Legendary'
    
    # Combinar resultados
    clustered_df = pd.concat([non_legendary, legendary])
    
    return clustered_df