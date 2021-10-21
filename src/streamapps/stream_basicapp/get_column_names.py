import streamlit as st
import pandas as pd

def get_columns_names(df):
    column = pd.DataFrame(df.columns)
    st.write(column)