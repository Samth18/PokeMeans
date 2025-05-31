import pandas as pd
import numpy as np

def load_and_preprocess_data(filepath):
    # Cargar datos
    df = pd.read_csv(filepath)
    
    # Calcular índice de ataque
    df['attack_index'] = (df['Attack'] + df['Sp. Atk']) - (df['Defense'] + df['Sp. Def'])
    
    # Separar Pokémon legendarios y no legendarios
    non_legendary = df[df['Legendary'] == False]
    legendary = df[df['Legendary'] == True]
    
    return non_legendary, legendary

def save_processed_data(non_legendary, legendary, processed_dir):
    non_legendary.to_csv(f"{processed_dir}/non_legendary.csv", index=False)
    legendary.to_csv(f"{processed_dir}/legendary.csv", index=False)