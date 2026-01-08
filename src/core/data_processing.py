# src/core/data_processing.py
import pandas as pd
import numpy as np

def generate_sample_data() -> pd.DataFrame:
    """
    Generate mock data for visualization, including global events.
    """
    np.random.seed(42)
    df = pd.DataFrame({
        'region': ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania'],
        'lon': [100, 10, 20, -100, 150],
        'lat': [30, 50, 0, 40, -20],
        'risk_level': np.random.rand(5)*100,
        'event': ['Storm', 'Flood', 'Heatwave', 'Earthquake', 'Cyclone'],
        'xG': np.random.rand(5),
        'xT': np.random.rand(5),
        'risk': np.random.rand(5)*100,
        'population_impact': np.random.randint(1000, 5000, size=5),
        'infrastructure_impact': np.random.randint(100, 500, size=5)
    })
    return df
