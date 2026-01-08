# src/core/teleconnection.py
import numpy as np
import pandas as pd

def el_nino_coupling(data: pd.DataFrame) -> pd.DataFrame:
    """
    Simulate El Niño-like teleconnection effects.
    Modifies 'risk' column using a sinusoidal factor.
    """
    factor = 1 + np.sin(np.linspace(0, 2*np.pi, len(data)))
    data_copy = data.copy()
    data_copy["risk"] = data_copy["risk"] * factor
    return data_copy

def apply_teleconnection(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply simple El Niño-like teleconnection effect on 'risk_level'.
    """
    df_copy = df.copy()
    if 'risk_level' in df_copy.columns:
        df_copy['risk_level'] = df_copy['risk_level'] * 1.1
    else:
        df_copy['risk_level'] = df_copy['risk'] * 1.1
    return df_copy
