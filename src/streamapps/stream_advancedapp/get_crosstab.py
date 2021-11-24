import streamlit as st
from src.utils.advanced_def import Advanced
from src.utils import uploaded_file


def app():
    advanced = Advanced()
    st.header("CrossTab")
    dataframe = uploaded_file.read_datafolder()

    data_columns = dataframe.columns
    data_type = dataframe.dtypes
    feature_col = st.selectbox('X', data_columns)

    submit = st.button("Show crosstab")
    if submit:
        st.dataframe(advanced.get_crosstab(dataframe))
