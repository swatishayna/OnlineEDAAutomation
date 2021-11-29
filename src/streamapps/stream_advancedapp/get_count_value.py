import streamlit as st
from src.utils.advanced_def import Advancedanalysis
from src.utils import uploaded_file
import pandas as pd

def app():

    st.header("Visualisation Analysis")
    #dataframe = uploaded_file.read_datafolder()
    dataframe = pd.read_csv('D:\data science\ineuron\Project\python project\OnlineEDAAutomation\OnlineEDAAutomation\src\streamapps\stream_advancedapp\diabetes.csv')
    advanced = Advancedanalysis(dataframe)
    st.write(advanced.get_count_value())



    column = st.selectbox("View Frequency of datapoints of Column", dataframe.columns)
    if column:
        st.dataframe(advanced.get_categories(column))


