import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import numpy as np
from matplotlib.patches import Patch
from math import pi


def plot_cluster_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='cluster_name', data=data)
    plt.title('Distribución de Pokémon por Cluster')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('docs/image/cluster_distribution.png')
    plt.close()


def plot_attack_index_vs_speed(data):
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='attack_index', y='Speed', hue='cluster_name', 
                    data=data, palette='viridis', s=100)
    plt.title('Índice de Ataque vs Velocidad por Cluster')
    plt.xlabel('Índice de Ataque (Ataque + Sp. Atk) - (Defensa + Sp. Def)')
    plt.ylabel('Velocidad')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('docs/image/attack_vs_speed.png')
    plt.close()


def interactive_3d_plot(data):
    fig = px.scatter_3d(data, x='Attack', y='Defense', z='Speed',
                        color='cluster_name', hover_name='Name',
                        title='Visualización 3D de Clusters de Pokémon')
    fig.write_html('docs/image/3d_clusters.html')


def plot_cluster_radar(data):
    # Calcular medias por cluster
    stats = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    cluster_means = data.groupby('cluster_name')[stats].mean()
    cluster_names = cluster_means.index.tolist()
    n_stats = len(stats)

    # Preparar figura
    angles = [n / float(n_stats) * 2 * pi for n in range(n_stats)]
    angles += angles[:1]  # cerrar el círculo

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    for i, cluster in enumerate(cluster_names):
        values = cluster_means.loc[cluster].tolist()
        values += values[:1]
        ax.plot(angles, values, label=cluster)
        ax.fill(angles, values, alpha=0.1)

    ax.set_title('Radar Stats Promedio por Cluster', size=15)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(stats)
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    plt.tight_layout()
    plt.savefig('docs/radar_stats_clusters.png')
    plt.close()


def plot_cluster_heatmap(data):
    stats = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    cluster_means = data.groupby('cluster_name')[stats].mean()

    plt.figure(figsize=(12, 8))
    sns.heatmap(cluster_means, annot=True, fmt='.1f', cmap='YlGnBu')
    plt.title('Media de Estadísticas por Cluster')
    plt.tight_layout()
    plt.savefig('docs/cluster_stats_heatmap.png')
    plt.close()
