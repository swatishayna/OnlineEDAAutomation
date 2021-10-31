import streamlit as st
from src.utils.basic_def import Basic
import numpy as np
import pandas as pd
import os
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report



    
def app():
    basic = Basic()    
    st.header("Basic Exploratory Data Analysis")
    dataframe = basic.get_data("train.csv")
    pr = ProfileReport(dataframe, explorative=True, minimal=True,correlations={"cramers": {"calculate": False}})
    
    st.header('*Exploratory Data Analysis Fast Report*')
    st_profile_report(pr)