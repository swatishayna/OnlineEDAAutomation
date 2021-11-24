import streamlit as st
from src.utils.advanced_def import Advanced
from src.utils import uploaded_file


def app():
    advanced = Advanced()
    st.header("Missing value")
    dataframe = uploaded_file.read_datafolder()

    data_columns = dataframe.columns
    data_type = dataframe.dtypes
    # feature_col = st.selectbox('X', data_columns)

    submit = st.button("Show missing value")
    if submit:
        st.dataframe(advanced.get_missing_value(dataframe))
