# src/visualization/dashboard.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Core imports
from src.core.data_processing import generate_sample_data
from src.core.teleconnection import apply_teleconnection
from src.core.scenario import apply_scenario
from src.core.risk_simulation import temporal_risk_evolution, event_propagation
from src.core.rl_optimizer import rl_optimize_formation, what_if_simulation

# Initialize Dash
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "PRITHVI-NET: Global Risk & Scenario Dashboard"

# Generate initial data
df = generate_sample_data()
df = apply_teleconnection(df)

def create_dashboard():
    layout = html.Div([
        html.H1("PRITHVI-NET: Global Risk & Scenario Dashboard", 
                style={'color':'white', 'textAlign':'center'}),
        
        # Scenario Slider
        html.Div([
            html.Label("Scenario Slider (0-100)", style={'color':'white'}),
            dcc.Slider(id='scenario-slider', min=0, max=100, step=1, value=0)
        ], style={"padding": "20px"}),

        # What-If Region Sliders
        html.Div([
            html.Label("What-If Region Adjustments (0.5-1.5)", style={'color':'white'}),
            html.Div([
                html.Label("Asia", style={'color':'white'}), dcc.Slider(id='asia-slider', min=0.5, max=1.5, step=0.05, value=1.0),
                html.Label("Europe", style={'color':'white'}), dcc.Slider(id='europe-slider', min=0.5, max=1.5, step=0.05, value=1.0),
                html.Label("Africa", style={'color':'white'}), dcc.Slider(id='africa-slider', min=0.5, max=1.5, step=0.05, value=1.0),
                html.Label("Americas", style={'color':'white'}), dcc.Slider(id='americas-slider', min=0.5, max=1.5, step=0.05, value=1.0),
                html.Label("Oceania", style={'color':'white'}), dcc.Slider(id='oceania-slider', min=0.5, max=1.5, step=0.05, value=1.0),
            ], style={"padding": "10px 0"})
        ], style={"padding": "20px"}),

        # Graphs
        html.Div([
            dcc.Graph(id='globe-graph', style={"height":"700px"}),
            dcc.Graph(id='xgxt-graph', style={"height":"400px"})
        ]),

        # Footer
        html.Footer("Made by Aniket Agarwal, Bachelor of Technology, Computer Science, Amity University, Punjab", 
                    style={'color':'white', 'textAlign':'center', 'padding':'10px', 'fontSize':'12px'})
    ], style={'backgroundColor':'black', 'padding':'10px', 'font-family':'Arial'})

    app.layout = layout
    return app

# Callback to update graphs
@app.callback(
    Output('globe-graph', 'figure'),
    Output('xgxt-graph', 'figure'),
    Input('scenario-slider', 'value'),
    Input('asia-slider', 'value'),
    Input('europe-slider', 'value'),
    Input('africa-slider', 'value'),
    Input('americas-slider', 'value'),
    Input('oceania-slider', 'value')
)
def update_graphs(scenario_value, asia_adj, europe_adj, africa_adj, americas_adj, oceania_adj):
    # Apply scenario
    df_scenario = apply_scenario(df, scenario_value)

    # Apply what-if regional adjustments
    adjustments = {
        'Asia': asia_adj,
        'Europe': europe_adj,
        'Africa': africa_adj,
        'Americas': americas_adj,
        'Oceania': oceania_adj
    }
    df_scenario = what_if_simulation(df_scenario, adjustments)

    # RL-based formation optimization
    df_scenario = rl_optimize_formation(df_scenario)

    # Risk evolution + uncertainty
    risk, lower, upper = temporal_risk_evolution(df_scenario)

    # Event propagation
    positions, intensity = event_propagation(df_scenario)

    # 3D Globe figure
    globe_fig = go.Figure()
    globe_fig.add_trace(go.Scattergeo(
        lon=df_scenario['lon'], lat=df_scenario['lat'],
        text=df_scenario['event'],
        marker=dict(size=intensity*20, color=intensity, colorscale='Rainbow', line=dict(width=0.5, color='white')),
        mode='markers'
    ))
    globe_fig.update_geos(showland=True, landcolor="black", oceancolor="darkblue")
    globe_fig.update_layout(
        paper_bgcolor="black", plot_bgcolor="black",
        font_color="white", title="Global Event Propagation & Risk"
    )

    # xG/xT bar chart
    xgxt_fig = go.Figure()
    xgxt_fig.add_trace(go.Bar(x=df_scenario['region'], y=df_scenario['xG_opt'], name='xG', marker_color='orange'))
    xgxt_fig.add_trace(go.Bar(x=df_scenario['region'], y=df_scenario['xT_opt'], name='xT', marker_color='cyan'))
    xgxt_fig.update_layout(
        barmode='group', paper_bgcolor='black', plot_bgcolor='black', font_color='white',
        title='Expected Goals & Threats (xG/xT)'
    )

    return globe_fig, xgxt_fig

# Entry point
def run_dashboard():
    app = create_dashboard()
    app.run(debug=True)

if __name__ == "__main__":
    run_dashboard()
