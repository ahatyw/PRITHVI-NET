# src/core/scenario.py
import pandas as pd

def apply_scenario(df: pd.DataFrame, scenario_value: float) -> pd.DataFrame:
    """
    Apply scenario simulation based on slider or scenario index.

    Args:
        df (pd.DataFrame): Must contain 'risk', 'population_impact', 'infrastructure_impact', 'xG', 'xT'.
        scenario_value (float): 0-100 slider or scenario index

    Returns:
        pd.DataFrame: Updated DataFrame
    """
    df_copy = df.copy()

    # Risk and impact scaling
    factor = 1 + scenario_value / 100
    df_copy['risk'] *= factor
    if 'population_impact' in df_copy.columns:
        df_copy['population_impact'] *= factor
    if 'infrastructure_impact' in df_copy.columns:
        df_copy['infrastructure_impact'] *= factor

    # xG/xT scaling
    xt_factor = 1 + 0.1 * scenario_value
    if 'xG' in df_copy.columns:
        df_copy['xG'] *= xt_factor
    if 'xT' in df_copy.columns:
        df_copy['xT'] *= xt_factor

    return df_copy
