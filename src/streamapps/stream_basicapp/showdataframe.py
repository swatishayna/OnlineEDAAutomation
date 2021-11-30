import streamlit as st
from src.utils import uploaded_file

def app():
    st.header("Complete Data View")
    dataframe = uploaded_file.read_datafolder()
    if dataframe == "Start Project (Project Dashboard-->Add Project or Project Dashboard-->View Project":
        st.write(dataframe)
    else:
        st.dataframe(dataframe)
    