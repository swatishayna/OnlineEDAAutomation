import streamlit as st
import pandas as pd

def describe_dataset(df):
    describe = df.describe()
    st.write(describe)