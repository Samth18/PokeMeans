import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_cluster_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='cluster_name', data=data)
    plt.title('Distribución de Pokémon por Cluster')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('docs/cluster_distribution.png')
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
    plt.savefig('docs/attack_vs_speed.png')
    plt.close()

def interactive_3d_plot(data):
    fig = px.scatter_3d(data, x='Attack', y='Defense', z='Speed',
                        color='cluster_name', hover_name='Name',
                        title='Visualización 3D de Clusters de Pokémon')
    fig.write_html('docs/3d_clusters.html')