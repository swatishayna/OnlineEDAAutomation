import streamlit as st
import pandas as pd

# This Function  is used to get column names
def get_columns_names(df):
    column = pd.DataFrame(df.columns)
    st.write(column)

# This function is to get a small description of dataset
def describe_dataset(df):
    describe = df.describe()
    st.write(describe)

# This function is used to get datatypes of the columns
def get_datatype_list(df):
    a = [i for i in df.dtypes]
    b = [i for i in df.columns]
    c = [str(i) for i in a]
    datatype_list = {b[i]:c[i] for i in range(len(a))}
    st.write(pd.Series(datatype_list))

# This function is used to get Duplicate rows in a dataset
def get_duplicate_rows(df):
    Duplicates = df[df.duplicated()]
    st.write(Duplicates)

# TestCase
# df = pd.read_csv('https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv')
# function_name(df) # Give unction name and run this file Using 'streamlit run BasicEda.py'
    