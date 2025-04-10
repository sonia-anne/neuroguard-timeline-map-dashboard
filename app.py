import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Streamlit config
st.set_page_config(page_title="NeuroGuard Timeline & Global Map", layout="wide", initial_sidebar_state="collapsed")

# Dark theme override
st.markdown("""
    <style>
    body, .stApp { background-color: #0d1117; color: #e6edf3; }
    .css-18ni7ap { background-color: #0d1117; }
    h1, h2, h3 { color: #58a6ff; }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🔭 NeuroGuard Timeline & Global Collaboration Map 🌐</h1>", unsafe_allow_html=True)
st.markdown("---")

# ---------------- TIMELINE ----------------
st.subheader("🚀 Execution Roadmap: From Lab to Deep Space")

# Update timeline with separated Y positions for readability
timeline_data = {
    "Year": ["2025", "2027", "2030", "2035+"],
    "Phase": ["Organoid Testing", "Animal Trials", "Human Application", "Mars Deployment"],
    "Details": [
        "AI-directed nanobots tested in human cerebral organoids with GBM.",
        "Full NeuroGuard modules applied in mice & primates with real-time brain monitoring.",
        "Terminal-stage GBM patients treated under enhanced ethical protocols.",
        "Autonomous neural repair in microgravity during space missions."
    ],
    "Y_Position": [1.0, 0.75, 1.0, 0.75]  # staggered positions for clarity
}

df = pd.DataFrame(timeline_data)

fig_timeline = go.Figure()

for i, row in df.iterrows():
    fig_timeline.add_trace(go.Scatter(
        x=[row["Year"]],
        y=[row["Y_Position"]],
        mode="markers+text",
        marker=dict(size=24, color="#1f77b4"),
        text=[f"<b>{row['Phase']}</b><br><span style='font-size:12px'><i>{row['Details']}</i></span>"],
        textposition="bottom center",
        hoverinfo="text"
    ))

fig_timeline.update_layout(
    title="Strategic Milestones Toward Implementation",
    template="plotly_dark",
    xaxis=dict(title="Milestone Year", tickvals=df["Year"], tickfont=dict(size=14)),
    yaxis=dict(visible=False),
    showlegend=False,
    height=550
)

st.plotly_chart(fig_timeline, use_container_width=True)

# ---------------- GLOBAL MAP ----------------
st.subheader("🌍 Global Scientific Collaborators for NeuroGuard")

map_data = pd.DataFrame({
    'Institute': ['Harvard', 'MIT', 'Neuralink', 'Moderna', 'Google AI', 'Caltech', 'Oxford'],
    'Latitude': [42.3770, 42.3601, 37.4848, 42.3624, 37.4220, 34.1377, 51.7548],
    'Longitude': [-71.1167, -71.0942, -122.1477, -71.0846, -122.0841, -118.1253, -1.2544]
})

fig_map = go.Figure(go.Scattergeo(
    lon=map_data['Longitude'],
    lat=map_data['Latitude'],
    text=map_data['Institute'],
    mode='markers+text',
    marker=dict(size=12, color='cyan', line=dict(width=1, color='black')),
    textposition="top center"
))

fig_map.update_layout(
    title="NeuroGuard Global Network of Innovation",
    geo=dict(
        projection_type="orthographic",
        showland=True,
        landcolor='rgb(10,10,10)',
        oceancolor='rgb(30,30,50)',
        showocean=True,
        bgcolor='#0d1117',
    ),
    template="plotly_dark",
    height=600
)

st.plotly_chart(fig_map, use_container_width=True)
