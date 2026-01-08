# src/core/rl_optimizer.py

import numpy as np
import pandas as pd

def rl_optimize_formation(df, iterations=50):
    """
    Simple RL-based formation optimizer placeholder.
    Adjusts xG/xT for 'optimal' formation using random policy gradients.
    """
    df_copy = df.copy()
    best_score = -np.inf
    best_df = df_copy.copy()

    for _ in range(iterations):
        # Random "policy" changes to xG/xT
        xG_change = np.random.uniform(0.95, 1.15, size=len(df_copy))
        xT_change = np.random.uniform(0.95, 1.15, size=len(df_copy))
        df_copy['xG_temp'] = df_copy['xG'] * xG_change
        df_copy['xT_temp'] = df_copy['xT'] * xT_change

        # Simple reward = sum(xG + xT)
        score = df_copy['xG_temp'].sum() + df_copy['xT_temp'].sum()
        if score > best_score:
            best_score = score
            best_df['xG_opt'] = df_copy['xG_temp']
            best_df['xT_opt'] = df_copy['xT_temp']

    return best_df

def what_if_simulation(df, adjustments: dict):
    """
    Apply hypothetical what-if adjustments to regions.
    adjustments = {'Asia': 1.1, 'Europe': 0.9, ...}
    """
    df_copy = df.copy()
    for region, factor in adjustments.items():
        df_copy.loc[df_copy['region'] == region, 'xG'] *= factor
        df_copy.loc[df_copy['region'] == region, 'xT'] *= factor
    return df_copy
