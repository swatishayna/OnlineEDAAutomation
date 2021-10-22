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
        st.dataframe(dataframe)

    datashape = st.checkbox("Get shape of the dataframe")
    if datashape:
        st.write(basic.get_shape(dataframe))
        
