import streamlit as st  
import pandas as pd
import plotly.express as px

# Assuming the dataset is already loaded
df = pd.read_csv("transformed_dataset_with_death_status.csv")

# Create age groups
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = [f"{age_bins[i]}-{age_bins[i+1]-1}" for i in range(len(age_bins)-1)]
df['AGE_GROUP'] = pd.cut(df['AGE'], bins=age_bins, labels=age_labels, right=False)

# Calculate the number of total cases and hospitalized cases by age group
susceptibility_counts = df.groupby('AGE_GROUP', observed=False).size()
hospitalized_counts = df[df['HOSPITALIZED'] == 'YES'].groupby('AGE_GROUP', observed=False).size()

# Create a summary DataFrame
summary = pd.DataFrame({
    'Total Cases': susceptibility_counts,
    'Hospitalized Cases': hospitalized_counts
}).fillna(0)

# Create an interactive bar chart using Plotly Express
fig = px.bar(
    summary,
    x=summary.index,
    y=['Total Cases', 'Hospitalized Cases'],
    barmode='group',  # Grouped bars for comparison
    labels={'index': 'Age Group', 'value': 'Number of Cases'},
    title='COVID-19 Cases by Age Group',
    color_discrete_map={'Total Cases': 'skyblue', 'Hospitalized Cases': 'salmon'},
    text_auto=True  # Display numbers on top of bars
)

# Customize the layout
fig.update_layout(
    xaxis_title='Age Group',
    yaxis_title='Number of Cases',
    xaxis_tickangle=45,  # Rotate x-axis labels
    template='plotly_white',
    legend_title='Case Type',
    margin=dict(t=50, b=100, l=50, r=50)  # Adjust margins for better layout
)

# Streamlit interface
st.title("COVID-19 Cases by Age Group")
st.write("This bar chart shows the total and hospitalized COVID-19 cases across different age groups.")

# Show the interactive plot in Streamlit
st.plotly_chart(fig)