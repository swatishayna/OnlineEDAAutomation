import streamlit as st
from src.utils.advanced_def import Advancedanalysis
from src.utils import uploaded_file

def app():

    st.header("Advanced Exploratory Data Analysis")
    dataframe = uploaded_file.read_datafolder()
    try:
        advanced = Advancedanalysis(dataframe)
        st.write(advanced.get_count_value())
        column = st.selectbox("View Frequency of datapoints of Column", dataframe.columns)
        if column:
            st.dataframe(advanced.get_categories(column))
    except:
        st.write(dataframe)

