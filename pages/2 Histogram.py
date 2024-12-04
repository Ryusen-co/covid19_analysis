import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
def load_data():
    return pd.read_csv("transformed_dataset.csv")  # Replace with your dataset path

df = load_data()

# Create a copy of the dataframe for analysis
analysis = df.copy()

# Define age bins and labels
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = [f"{age_bins[i]}-{age_bins[i+1]-1}" for i in range(len(age_bins) - 1)]
analysis["AGE_GROUP"] = pd.cut(analysis["AGE"], bins=age_bins, labels=age_labels, right=False)

# Filter data for hospitalized cases
hospitalized_df = analysis[analysis["HOSPITALIZED"] == 'YES']

# Sidebar options for interaction
st.sidebar.header("Interactive Options")
chart_type = st.sidebar.radio(
    "Select Chart Type", ["Total Cases by Age Group", "Hospitalized Cases by Age Group"]
)

# Plot Total Cases or Hospitalized Cases based on user selection
if chart_type == "Total Cases by Age Group":
    chart_data = analysis.groupby("AGE_GROUP").size().reset_index(name="Count")
    title = "Total Cases by Age Group"
    color = "skyblue"
else:
    chart_data = hospitalized_df.groupby("AGE_GROUP").size().reset_index(name="Count")
    title = "Hospitalized Cases by Age Group"
    color = "salmon"

# Interactive bar chart
fig = px.bar(
    chart_data,
    x="AGE_GROUP",
    y="Count",
    title=title,
    labels={"AGE_GROUP": "Age Group", "Count": "Number of Cases"},
    text="Count",
    color_discrete_sequence=[color],
)

fig.update_layout(
    xaxis_title="Age Group",
    yaxis_title="Number of Cases",
    title_font_size=20,
    xaxis_tickangle=-45,
    template="plotly_white",
)

# Display the chart
st.plotly_chart(fig, use_container_width=True)