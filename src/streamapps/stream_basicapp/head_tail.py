import streamlit as st
import pandas as pd
from pathlib import Path
import os
from src.utils import uploaded_file
from src.utils.basic_def import Basic

def app():
    basic = Basic()
    st.header("Basic Exploratory Data Analysis")

    dataframe = uploaded_file.read_datafolder()
    try:
        st.write(dataframe)
    except:
        option = st.sidebar.radio("Select",("Head","Tail"))
        if option == "Head":
            value = st.number_input("Input the number of rows", max_value=dataframe.shape[0],min_value=1)
            st.dataframe(dataframe.head(value))
        else:
            value = st.number_input("Input the number of rows", max_value=dataframe.shape[0], min_value=1)
            st.dataframe(dataframe.tail(value))