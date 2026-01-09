# PRITHVI-NET

**Global Risk & Scenario Simulator**

---

## Overview

**PRITHVI-NET** is a prototype software system designed to simulate and analyze global disaster risks. It integrates AI techniques, scenario analysis, and teleconnection modeling to predict the propagation of natural and human-made hazards. Users can visualize potential impacts, evaluate mitigation strategies, and explore "what-if" scenarios at a global scale.

---

## Key Features

1. **3D Interactive Globe Visualization**
   - Risk events displayed on a globe, suspended in space.
   - Teleconnections and event propagation paths represented with dynamic lines.
   - Real-time updates based on scenario and regional adjustments.

2. **Scenario Simulation**
   - Adjustable scenario slider (0–100) to simulate different risk levels.
   - Scenario effects applied across risk, population impact, infrastructure impact, and derived metrics like xG/xT.

3. **What-If Regional Adjustments**
   - Fine-grained control over Asia, Europe, Africa, Americas, and Oceania.
   - Explore hypothetical disaster responses and region-specific sensitivity.

4. **AI-Based Risk Optimization**
   - Reinforcement Learning optimizes response strategies and risk mitigation formation.
   - Provides actionable insights on resource allocation and prioritization.

5. **Comprehensive Metrics**
   - Temporal risk evolution with uncertainty bounds.
   - Event propagation intensity and patterns across regions.
   - xG/xT analysis (expected goals/threats) for risk prioritization.

---

## Problem Statement

Disasters often have complex, cascading effects influenced by interconnected global systems. Traditional risk assessment methods are static and limited. PRITHVI-NET addresses this by:

- Simulating disaster propagation globally.
- Capturing teleconnections and interdependencies.
- Allowing interactive exploration of hypothetical scenarios.
- Providing actionable insights for disaster preparedness and management.

---

## Conceptual Significance

- **Predictive Analytics:** Combines historical and simulated data to forecast potential disaster outcomes.
- **Global Perspective:** Models risk interactions across continents and countries.
- **Decision Support:** Enhances emergency planning, resource allocation, and policy formulation.
- **Prototype to Production:** Demonstrates integration of AI, visualization, and scenario analysis for future scalable systems.

---

## Technology Stack

- **Python 3.11**
- **Dash & Plotly:** Interactive dashboards and 3D visualizations.
- **Pandas & NumPy:** Data processing and numerical computations.
- **Scipy & Requests:** Statistical modeling and API integrations.
- **Dash Bootstrap Components:** UI enhancements.
- **Reinforcement Learning:** Optimization of mitigation strategies.

---

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd PRITHVI-NET
