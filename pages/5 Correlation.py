import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Load the dataset (replace with the correct path to your dataset)

def load_data():
    return pd.read_csv("transformed_dataset.csv")  # Replace with your actual file path

df = load_data()

# List of diseases to check correlation with ICU admission
disease_columns = ['DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 'HYPERTENSION', 
                   'CARDIOVASCULAR', 'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO', 'ICU']

# Map disease columns to numeric values (e.g., Yes=1, No=2 or 1/2 mapping)
disease_mappings = {
    'YES': 1, 'NO': 2, 1: 1, 2: 2, 99: 0  # Assuming 99 means unknown or not applicable
}

# Map each disease column using the mapping
for column in disease_columns:
    if column in df.columns:
        df[column] = df[column].map(disease_mappings).fillna(0)  # Convert any NaN values to 0

# Subset the dataset for the diseases and ICU column
disease_data = df[disease_columns]

# Compute the correlation matrix
correlation_matrix = disease_data.corr()

# Convert the correlation matrix into a long format (for Plotly)
correlation_matrix_long = correlation_matrix.reset_index().melt(id_vars="index")
correlation_matrix_long.columns = ["Disease 1", "Disease 2", "Correlation"]

# Create an interactive heatmap using Plotly
fig = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    colorscale='icefire',
    zmin=-1, zmax=1,
    hoverongaps=False,
    colorbar=dict(title="Correlation Coefficient"),
))

fig.update_layout(
    title="Correlation Between Diseases and ICU Admission",
    xaxis_title="Diseases",
    yaxis_title="Diseases",
    title_font_size=20,
    template="plotly_white",
    xaxis=dict(tickmode='array', tickvals=list(range(len(correlation_matrix.columns))), ticktext=correlation_matrix.columns),
    yaxis=dict(tickmode='array', tickvals=list(range(len(correlation_matrix.columns))), ticktext=correlation_matrix.columns),
)

# Display the interactive chart in Streamlit
st.plotly_chart(fig, use_container_width=True)