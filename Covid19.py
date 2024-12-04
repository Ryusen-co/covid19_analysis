import streamlit as st
import pandas as pd
from PIL import Image
st.image('shrdc_logo.png', width = 300)

st.header('Welcome to Covid-19 Data Analysis')
covid_data = pd.read_csv('transformed_dataset.csv')
st.dataframe(covid_data)
st.caption('This data contains the total positivs cases recorded within certain area.')


