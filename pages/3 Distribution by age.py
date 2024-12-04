import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset

def load_data():
    return pd.read_csv("transformed_dataset.csv")  # Replace with your actual file path

df = load_data()

# Define age bins and labels
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = [f"{age_bins[i]}-{age_bins[i+1]-1}" for i in range(len(age_bins)-1)]
df["AGE_GROUP"] = pd.cut(df["AGE"], bins=age_bins, labels=age_labels, right=False)


# Filter data to include only 'Female' and 'Male'
gender_age_df = df[df["SEX"].isin(["FEMALE", "MALE"])]

# Interactive bar chart using Plotly
fig = px.histogram(
    gender_age_df,
    x="AGE_GROUP",
    color="SEX",
    title="Distribution of Cases by Gender & Age Group",
    labels={"AGE_GROUP": "Age Group", "count": "Number of Cases", "SEX": "Gender"},
    color_discrete_map={"FEMALE": "pink", "MALE": "lightblue"},
    barmode="stack",  # Stack the bars to show both genders together
    text_auto=True,  # Display the count on top of bars
)

fig.update_layout(
    xaxis_title="Age Group",
    yaxis_title="Number of Cases",
    title_font_size=20,
    xaxis_tickangle=-45,
    template="plotly_white",
)

# Display the interactive chart
st.plotly_chart(fig, use_container_width=True)