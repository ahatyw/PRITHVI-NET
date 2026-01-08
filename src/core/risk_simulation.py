# src/core/risk_simulation.py

import numpy as np
import pandas as pd

def calculate_risk_over_time(df: pd.DataFrame):
    """
    Compute risk evolution over time with optional uncertainty.
    Adds 'risk_over_time' and 'uncertainty' columns to the DataFrame.
    """
    df_copy = df.copy()
    df_copy['risk_over_time'] = df_copy['risk'] * np.linspace(0.8, 1.2, len(df_copy))
    df_copy['uncertainty'] = np.random.rand(len(df_copy)) * 0.2
    return df_copy, df_copy['uncertainty']

def temporal_risk_evolution(data: pd.DataFrame, uncertainty: bool = True):
    """
    Simulate risk evolution with optional confidence bands.
    Returns: risk, lower bound, upper bound
    """
    risk = data["risk"].values
    if uncertainty:
        lower = risk - np.random.rand(len(risk)) * 10
        upper = risk + np.random.rand(len(risk)) * 10
        return risk, lower, upper
    return risk, None, None

def event_propagation(data: pd.DataFrame):
    """
    Simulate events propagating across regions.
    Returns positions (lat/lon normalized) and intensity
    """
    positions = np.random.rand(len(data), 2)  # lat, lon normalized
    intensity = data["risk"].values
    return positions, intensity
