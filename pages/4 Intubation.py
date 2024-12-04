import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset (replace with the correct path to your dataset)

def load_data():
    return pd.read_csv("transformed_dataset.csv")  # Replace with your actual file path

df = load_data()

# Count the number of patients who required intubation
intubated_counts = df['INTUBATED'].value_counts().reset_index()
intubated_counts.columns = ['Intubation Status', 'Number of Patients']

# Create an interactive bar chart using Plotly
fig = px.bar(
    intubated_counts,
    x='Intubation Status',
    y='Number of Patients',
    title='Number of Patients Who Required Intubation',
    labels={'Intubation Status': 'Intubation Status', 'Number of Patients': 'Number of Patients'},
    color='Intubation Status',  # Color bars by Intubation Status
    color_discrete_map={'YES': 'lightgreen', 'NO': 'salmon', 'UNKNOWN': 'gray', 'DOES NOT APPLY': 'skyblue'},  # Custom color mapping
    text='Number of Patients',  # Display the count on top of the bars
)

# Customize layout
fig.update_layout(
    xaxis_title="Intubation Status",
    yaxis_title="Number of Patients",
    title_font_size=20,
    xaxis_tickangle=0,
    template="plotly_white",
)

# Display the interactive chart in Streamlit
st.plotly_chart(fig, use_container_width=True)