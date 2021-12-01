import streamlit as st
from src.utils import uploaded_file
import numpy as np
import pandas as pd
import os
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def app():
   
    st.header("Basic Exploratory Data Analysis")
    dataframe = uploaded_file.read_datafolder()
    try:
        pr = ProfileReport(dataframe, explorative=True, minimal=True,correlations={"cramers": {"calculate": False}})
        st.header('*Exploratory Data Analysis Fast Report*')
        st_profile_report(pr)
    except:
        st.write(dataframe)