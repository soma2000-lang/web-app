import pandas as pd
import numpy as np
import streamlit as st
#import the dataset and create a checkbox to shows the data on your website
df1 = pd.read_csv("df_surf.csv")
if st.checkbox('Show Dataframe'):
    st.write(df1)
#Read in data again, but by using streamlit's caching aspect. Our whole app re-runs every time we make small changes, which is infeasible the more complicated our code becomes. So this is the recommended way to import the data.
df = st.cache(pd.read_csv)("df_surf.csv")
#create side bars that allow for multiple selections:
age = st.sidebar.multiselect("Select age", df['surfer_age'].unique())
st.write("Age selected", age)
weekly_surfs = st.sidebar.multiselect("Surfer Exercise frequency", df['surfer_exercise_frequency'].unique())
st.write("Frequency selected", weekly_surfs)
surfer_experience = st.sidebar.multiselect("Surfer Experience", df['surfer_experience'].unique())
st.write("Experience selected", surfer_experience)
surfer_gender = st.sidebar.multiselect("Surfer Gender", df['surfer_gender'].unique())
st.write("Gender selected", surfer_gender)
wave_height = st.sidebar.multiselect("Wave height", df['wave_height'].unique())
st.write("Wave height selected", wave_height)
board_type = st.sidebar.multiselect("Board Type", df['board_type'].unique())
st.write("Board type selected", board_type)
#create a sidebar to select the variable output you want to see after making your multiple selections
variables = st.sidebar.multiselect("Select what you want to see for your selection", df.columns)
st.write("You selected these variables", variables)
# return the sub-set data  of variables you want to see
selected_data = df[(df['surfer_age'].isin(age))]
subset_data = selected_data[variables]
data_is_check = st.checkbox("Display the data of selected variables")
if data_is_check:
    st.write(subset_data)