import streamlit as st
import pandas as pd

def get_columns_names(df):
    Duplicates = df[df.duplicated()]
    st.write(Duplicates)