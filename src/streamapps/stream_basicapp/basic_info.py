import streamlit as st
import pandas as pd
from src.utils.basic_def import Basic
from pathlib import Path
import os

def app():
    basic = Basic()    
    st.header("Basic Exploratory Data Analysis")
    dataframe = basic.get_data("winequality_red.csv")

    column_names = st.checkbox("Get Column names of the dataframe")
    if column_names:
        st.write(basic.get_columns_names(dataframe))
    
    describe = st.checkbox("Get small description of the dataframe")
    if describe:
        st.write(basic.describe_dataset(dataframe))
    
    datatype = st.checkbox("Get Datatype list with respect to columns names of the dataframe")
    if datatype:
        st.write(basic.get_datatype_list(dataframe))

    duplicate_rows = st.checkbox("Get Duplicate rows of the datatframe")
    if duplicate_rows:
        st.write(basic.get_duplicate_rows(dataframe))

    view_df = st.checkbox("View Dataframe")
    if view_df:
        st.dataframe(dataframe)

    datashape = st.checkbox("Get shape of the dataframe")
    if datashape:
        st.write(basic.get_shape(dataframe))
        
