# Script principal para el análisis K-Meansimport os
import os
import pandas as pd


# Construir ruta relativa desde main.py hacia el archivo csv
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Subir un nivel desde src/
DATA_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'Pokemon.csv')

# Cargar archivo CSV
df = pd.read_csv(DATA_PATH)

# Mostrar algunas filas
print(df.head())
