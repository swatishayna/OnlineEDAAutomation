import streamlit as st
from src.utils import uploaded_file
from src.utils.basic_def import Basic

def app():
    basic = Basic()
    st.header("Basic Exploratory Data Analysis")

    dataframe = uploaded_file.read_datafolder()
    try:
        option = st.sidebar.radio("Select",("Head","Tail"))
        if option == "Head":
            value = st.number_input("Input the number of rows", max_value=dataframe.shape[0],min_value=1)
            st.dataframe(dataframe.head(value))
        else:
            value = st.number_input("Input the number of rows", max_value=dataframe.shape[0], min_value=1)
            st.dataframe(dataframe.tail(value))
    except:
        st.write(dataframe)