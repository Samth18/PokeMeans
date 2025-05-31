# Estructura del Proyecto

## Visión General

PokeMeans es un proyecto de análisis de datos que utiliza el algoritmo K-Means para agrupar Pokémon según sus estadísticas, permitiendo la construcción de equipos equilibrados. El proyecto procesa datos de Pokémon, aplica clustering, genera visualizaciones y recomienda equipos optimizados.

## Estructura de Directorios

### `/data/` - Almacenamiento de Datos
- **`/raw/`**: Contiene los datos sin procesar
  - `Pokemon.csv`: Dataset original con información de Pokémon

- **`/processed/`**: Almacena los datos después del preprocesamiento
  - `clustered_pokemon.csv`: Dataset con Pokémon agrupados por clusters
  - `legendary_team.csv`: Equipo recomendado de Pokémon legendarios
  - `normal_team.csv`: Equipo recomendado de Pokémon no legendarios

### `/src/` - Código Fuente
- `data_processing.py`: Funciones para cargar y preprocesar los datos
- `clustering.py`: Implementación del algoritmo K-Means para agrupar Pokémon
- `visualization.py`: Generación de gráficos y visualizaciones interactivas
- `team_builder.py`: Algoritmos para construir equipos equilibrados de Pokémon
- `main.py`: Versión alternativa del script principal ubicada en src
- **`__pycache__/`**: Archivos de caché Python generados automáticamente durante la ejecución

### `/docs/` - Documentación
- `estructura.md`: Este archivo, que explica la estructura del proyecto
- `analisis.md`: Documentación sobre el análisis realizado

- **`/image/`**: Contiene las visualizaciones generadas por el proyecto
  - `attack_vs_speed.png`: Gráfico que muestra la relación entre el índice de ataque y la velocidad de los Pokémon
  - `cluster_distribution.png`: Visualización de la distribución de Pokémon en los diferentes clusters
  - `3d_clusters.html`: Visualización interactiva en 3D de los clusters de Pokémon
  - `image.png`: Imagen adicional relacionada con el proyecto

### Raíz del Proyecto
- `main.py`: Script principal que coordina el flujo de trabajo completo

## Flujo de Ejecución

1. El script `main.py` inicia el proceso llamando a las diferentes funcionalidades
2. Se cargan y preprocesan los datos desde `Pokemon.csv` usando `data_processing.py`
3. Se aplica clustering a los Pokémon usando `clustering.py`
4. Se generan visualizaciones con `visualization.py`
5. Se construyen equipos recomendados utilizando `team_builder.py`
6. Los resultados se guardan en la carpeta `/data/processed/`

## Descripción de Componentes Principales

- **Procesamiento de Datos**: Separa Pokémon legendarios de no legendarios y normaliza atributos
- **Clustering**: Agrupa Pokémon en categorías según sus estadísticas (ofensivos, defensivos, veloces, etc.)
- **Visualización**: Genera gráficos de distribución de clusters y comparativas de estadísticas
- **Constructor de Equipos**: Crea equipos equilibrados basados en los clusters y un umbral de balance