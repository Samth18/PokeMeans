from src.data_processing import load_and_preprocess_data, save_processed_data
from src.clustering import apply_clustering_to_all
from src.visualization import plot_cluster_distribution, plot_attack_index_vs_speed, interactive_3d_plot
from src.team_builder import TeamBuilder
import os

def main():
    # Crear directorios si no existen
    os.makedirs('data/processed', exist_ok=True)
    os.makedirs('docs', exist_ok=True)
    
    # 1. Cargar y preprocesar datos
    non_legendary, legendary = load_and_preprocess_data('data/raw/Pokemon.csv')
    
    # 2. Aplicar clustering
    clustered_data = apply_clustering_to_all(non_legendary, legendary)
    clustered_data.to_csv('data/processed/clustered_pokemon.csv', index=False)
    
    # 3. Visualizaciones
    plot_cluster_distribution(clustered_data)
    plot_attack_index_vs_speed(clustered_data)
    interactive_3d_plot(clustered_data)
    
    # 4. Construir equipos de ejemplo
    team_builder = TeamBuilder(clustered_data)
    
    # Equipo normal
    normal_team = team_builder.build_team(legendary=False, balance_threshold=0.6)
    print("\nEquipo Normal (60% balanceado):")
    print(normal_team[['Name', 'cluster_name', 'attack_index']])
    normal_team.to_csv('data/processed/normal_team.csv', index=False)
    
    # Equipo legendario
    legendary_team = team_builder.build_team(legendary=True, balance_threshold=0.4)
    print("\nEquipo Legendario (40% balanceado - más especializado):")
    print(legendary_team[['Name', 'cluster_name', 'attack_index']])
    legendary_team.to_csv('data/processed/legendary_team.csv', index=False)

if __name__ == "__main__":
    main()