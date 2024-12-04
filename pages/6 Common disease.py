import pandas as pd
import plotly.express as px
import streamlit as st

# Assuming the transformed dataset is already loaded
df = pd.read_csv("transformed_dataset_with_death_status.csv")

# Filter for deceased patients
deceased_df = df[df['DATE_OF_DEATH'] == 'YES'].copy()  # Create a copy of the subset to avoid warnings

# List of disease columns to check for deceased patients
disease_columns = ['DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 'HYPERTENSION', 
                   'CARDIOVASCULAR', 'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO']

# Map disease columns to numeric values (1 = disease present, 2 = disease absent, 99 = unknown)
# We will count only the diseases marked as 'YES'
disease_mappings = {
    'YES': 1, 'NO': 0, 'UNKNOWN': 0, 1: 1, 2: 0, 99: 0  # Assuming 99 means unknown or not applicable
}

# Map disease columns for deceased patients using .loc to avoid the warning
for column in disease_columns:
    if column in deceased_df.columns:
        deceased_df.loc[:, column] = deceased_df[column].map(disease_mappings).fillna(0)

# Sum up the diseases for deceased patients
disease_counts = deceased_df[disease_columns].sum()

# Create an interactive bar chart using Plotly Express
fig = px.bar(
    x=disease_counts.index,
    y=disease_counts.values,
    labels={'x': 'Disease', 'y': 'Number of Deceased Patients'},
    title='Common Diseases Among Deceased Patients',
    color=disease_counts.values,  # Color based on the disease count
    color_continuous_scale='reds',  # Use a red color scale for visual emphasis
    text=disease_counts.values,  # Display the counts on top of the bars
)

# Customize the layout to make it more interactive
fig.update_layout(
    xaxis_tickangle=-45,  # Rotate x-axis labels
    template='plotly_white',  # Clean white background
    showlegend=False,  # Hide the legend (it's not needed)
    margin=dict(t=50, b=100, l=50, r=50)  # Add some margins for better layout
)

# Streamlit interface
st.title("Deceased Patients' Disease Analysis")
st.write("This bar chart shows the common diseases among deceased patients.")

# Show the interactive plot
st.plotly_chart(fig)