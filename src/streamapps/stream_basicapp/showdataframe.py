import streamlit as st
from src.utils import uploaded_file

def app():
    st.header("Complete Data View")
    dataframe = uploaded_file.read_datafolder()
    st.dataframe(dataframe)
    