import random
import pandas as pd

class TeamBuilder:
    def __init__(self, clustered_data):
        self.data = clustered_data
        self.non_legendary = clustered_data[clustered_data['Legendary'] == False]
        self.legendary = clustered_data[clustered_data['Legendary'] == True]
    
    def build_team(self, legendary=False, team_size=6, balance_threshold=0.5):
        """
        Crea un equipo con restricciones de balance
        
        Parameters:
        - legendary: Si es True, usa Pokémon legendarios
        - team_size: Número de Pokémon en el equipo
        - balance_threshold: Umbral de balance (0-1), donde 1 es completamente balanceado
        """
        source = self.legendary if legendary else self.non_legendary
        
        # Calcular proporciones de clusters
        n_aggressive = max(1, int(team_size * (1 - balance_threshold) / 2))
        n_defensive = max(1, int(team_size * (1 - balance_threshold) / 2))
        n_balanced = team_size - n_aggressive - n_defensive
        
        # Seleccionar Pokémon de cada cluster
        aggressive = source[source['cluster_name'].str.contains('Aggressive')].sample(n_aggressive)
        defensive = source[source['cluster_name'].str.contains('Defensive')].sample(n_defensive)
        balanced = source[source['cluster_name'].str.contains('Balanced')].sample(n_balanced)
        
        # Combinar equipo
        team = pd.concat([aggressive, defensive, balanced]).sample(frac=1)  # Mezclar
        
        return team
    
    def evaluate_team_balance(self, team):
        """Calcula el balance de un equipo (0-1 donde 1 es perfectamente balanceado)"""
        cluster_counts = team['cluster_name'].value_counts(normalize=True)
        balance_score = 1 - abs(cluster_counts.get('Aggressive', 0) - cluster_counts.get('Defensive', 0))
        return balance_score