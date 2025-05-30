import os

def crear_estructura_proyecto():
    """Crea la estructura de directorios con archivos útiles en lugar de .gitkeep"""
    
    # Directorios principales
    directorios = [
        'data/raw',
        'data/processed',
        'notebooks',
        'src',
        'src/utils',
        'results/plots',
        'results/tables',
        'docs'
    ]
    
    # Crear cada directorio
    for directorio in directorios:
        os.makedirs(directorio, exist_ok=True)
        print(f'Directorio creado: {directorio}')
    
    # Archivos base con contenido relevante
    archivos_base = {
        'src/main.py': '# Script principal para el análisis K-Means',
        'notebooks/exploracion.ipynb': '# Notebook de análisis exploratorio',
        'README.md': '# PokeMeans - Clustering de Pokémon con K-Means',
        'requirements.txt': 'pandas\nscikit-learn\nmatplotlib\nseaborn\njupyter',
        
        # Archivos más útiles para data/
        'data/raw/LEEME.md': '# Datos Originales\n\nColocar aquí el archivo pokemon.csv descargado de Kaggle',
        'data/processed/LEEME.md': '# Datos Procesados\n\nAquí se almacenarán los datasets después del preprocesamiento',
        
        # Documentación útil en docs/
        'docs/metodologia.md': '# Metodología\n\nDescripción del proceso de análisis y clustering',
        'docs/estructura.md': '# Estructura del Proyecto\n\nExplicación del propósito de cada carpeta'
    }
    
    for archivo, contenido in archivos_base.items():
        with open(archivo, 'w') as f:
            f.write(contenido)
        print(f'Archivo creado: {archivo}')
    
    print("\n✅ Estructura del proyecto creada con éxito!")

if __name__ == "__main__":
    crear_estructura_proyecto()
