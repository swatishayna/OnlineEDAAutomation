import streamlit as st
import pandas as pd

def get_datatype_list(df):
    a = [i for i in df.dtypes]
    b = [i for i in df.columns]
    c = [str(i) for i in a]
    datatype_list = {b[i]:c[i] for i in range(len(a))}
    st.write(pd.Series(datatype_list))