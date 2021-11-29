import streamlit as st
from src.utils.advanced_def import Advancedanalysis
from src.utils import uploaded_file
import pandas as pd
import numpy as np
from src.utils.basic_def import Basic

def app():

    basic = Basic()
    st.header("Column Analysis with Quantile Analysis")
    #dataframe = uploaded_file.read_datafolder()
    dataframe = pd.read_csv('D:\data science\ineuron\Project\python project\OnlineEDAAutomation\OnlineEDAAutomation\src\streamapps\stream_advancedapp\diabetes.csv')
    advanced = Advancedanalysis(dataframe)

    categorical = st.checkbox("View  Analysis of Categorical Columns")
    if categorical:
        categorical_column_list = [column for column in dataframe.columns if dataframe[column].dtypes == 'object']
        categorical_column = st.selectbox("Select Column", categorical_column_list)
        if categorical_column:
            st.write(advanced.get_categorical_stats(categorical_column))

    numerical = st.checkbox("View Analysis of Numerical Columns")
    if numerical:
        st.write(dataframe.describe(include = [np.number]))
    get_quantile = st.checkbox("Get Quantile_Stats")
    if get_quantile:
        st.subheader(f"Get quantile")
        quantile_value = st.slider('Size', max_value=0.0, min_value=1.0)
        if quantile_value:
            for column in dataframe.columns:
                try:
                    st.write(f"values at the given quantile in {column} is {dataframe[column].quantile(quantile_value)}")
                except:
                    pass





