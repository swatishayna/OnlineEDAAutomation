import streamlit as st
import pandas as pd
from src.utils.basic_def import Basic
from pathlib import Path
import os

def app():
    basic = Basic()    
    st.header("Basic Exploratory Data Analysis")
    dataframe = basic.get_data("winequality_red.csv")
    view_df = st.checkbox("View Dataframe")
    if view_df:
        st.write("Dataframe")
        st.dataframe(dataframe)

    datashape = st.checkbox("Get shape of the dataframe")
    if datashape:
        st.write("Shape of the Dataframe:",basic.get_shape(dataframe))
        st.write("Total number of Rows:", basic.get_shape(dataframe)[0])
        st.write("Total number of Columns:", basic.get_shape(dataframe)[1])
    
    missing_values = st.checkbox("Get missing values")
    if missing_values:
        st.write("Missing values", basic.get_missing_value(dataframe))

    missing_values_count = st.checkbox("Get count of missing values")
    if missing_values_count:
        st.write("Count of missing values", basic.get_count_missing_value(dataframe))

    percentage_missing_values = st.checkbox("Get percentage of missing values")
    if percentage_missing_values:
        st.write("Percentage of missing value", basic.get_percentage_missing_values(dataframe, basic.get_count_missing_value(dataframe)))
