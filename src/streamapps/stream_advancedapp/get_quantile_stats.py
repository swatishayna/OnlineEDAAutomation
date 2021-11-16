import streamlit as st
from src.utils.advanced_def import Advanced


def app():
    advanced = Advanced()
    st.header("Quantile Statistics")
    dataframe = advanced.get_data("winequality_red.csv")

    data_columns = dataframe.columns
    data_type = dataframe.dtypes
    # feature_col = st.selectbox('X', data_columns)

    submit = st.button("Show Quantile statistics")
    if submit:
        st.dataframe(advanced.get_quantile_stats(dataframe))
