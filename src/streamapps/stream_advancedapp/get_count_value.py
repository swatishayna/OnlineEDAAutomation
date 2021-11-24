import streamlit as st
from src.utils.advanced_def import Advanced


def app():
    advanced = Advanced()
    st.header("Visualisation Analysis")
    dataframe = advanced.get_data("train.csv")

    data_columns = dataframe.columns
    data_type = dataframe.dtypes
    # feature_col = st.selectbox('X', data_columns)

    submit = st.button("Show count value")
    if submit:
        st.dataframe(advanced.get_count_value(dataframe))
