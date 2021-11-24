import streamlit as st
from src.utils import uploaded_file

def app():
    st.write('Yes')
    uploaded_file.read_datafolder()