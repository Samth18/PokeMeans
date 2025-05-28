import os

def crear_estructura_proyecto():
    """Crea la estructura de directorios para el proyecto PokeMeans"""
    
    # Directorios principales
    directorios = [
        'data/raw',            # Datos originales (CSV de Pokémon)
        'data/processed',      # Datos procesados
        'notebooks',           # Jupyter notebooks de análisis
        'src',                 # Código fuente Python
        'src/utils',           # Utilidades compartidas
        'results/plots',       # Gráficos y visualizaciones
        'results/tables',      # Tablas de resultados
        'docs'                 # Documentación adicional
    ]
    
    # Crear cada directorio
    for directorio in directorios:
        os.makedirs(directorio, exist_ok=True)
        print(f'Directorio creado: {directorio}')
    
    # Crear archivos base vacíos
    archivos_base = {
        'src/main.py': '# Script principal para el análisis K-Means',
        'notebooks/exploracion.ipynb': '# Notebook de análisis exploratorio',
        'README.md': '# PokeMeans - Clustering de Pokémon con K-Means',
        'requirements.txt': '# Dependencias del proyecto'
    }
    
    for archivo, contenido in archivos_base.items():
        with open(archivo, 'w') as f:
            f.write(contenido)
        print(f'Archivo creado: {archivo}')
    
    print("\n✅ Estructura del proyecto creada con éxito!")

if __name__ == "__main__":
    crear_estructura_proyecto()