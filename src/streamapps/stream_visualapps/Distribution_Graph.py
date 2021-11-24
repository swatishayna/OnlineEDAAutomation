import streamlit as st
import numpy as np
from src.utils import advanced_def,visual_def
import pandas as pd
from src.streamapps.stream_projapp import upload_data
from pathlib import Path
from src.utils.basic_def import Basic


def app():
    basic = Basic()    
    st.header("Advanced Exploratory Data Analysis")
    data = basic.get_data("train.csv")

    data_columns = data.columns
    data_type = data.dtypes
    

    visual = visual_def.Visualization()
    
    
    

    choice = st.sidebar.radio("",["Generate histogram for all columns", "Select the Column"])
    if choice == "Generate histogram for all columns":
        st.subheader("Histogram for all columns")
        
        #valid_columns = [i for i in data_columns if data_type[i] == 'float64' or data_type[i] == 'int64']
        all_results = visual.distributionplot_all(data,data_columns)
        for result in all_results:
            st.plotly_chart(result)
    else:
        select_column = st.sidebar.selectbox('select your label col',
                                        ([i for i in data_columns if data_type[i] == 'float64' or data_type[i] == 'int64']))
        st.subheader("Histogram for column", select_column)
        result = visual.distributionplot(data,select_column)
        st.plotly_chart(result)