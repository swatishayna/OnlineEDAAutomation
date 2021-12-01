import streamlit as st
from src.utils import uploaded_file

def app():
    st.header("Basic Exploratory Data Analysis")
    data = uploaded_file.read_datafolder()

    try:
       st.dataframe(data)
    except:
        st.write(data)
    