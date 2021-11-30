import streamlit as st
import numpy as np
from src.utils import advanced_def,visual_def
import pandas as pd
from src.streamapps.stream_projapp import upload_data
from pathlib import Path
from src.utils import uploaded_file


def app():

    
    st.header("Visualisation Analysis")
    data = uploaded_file.read_datafolder()
    if data == "Start Project (Project Dashboard-->Add Project or Project Dashboard-->View Project":
        st.write(data)
    else:
        data_columns = data.columns
        data_type = data.dtypes


        visual = visual_def.Visualization()

        values, names = st.columns(2)
        valid_columns_continous = [i for i in data_columns if data_type[i] == 'float64' or data_type[i] == 'int64']
        feature_values = values.selectbox('Values', valid_columns_continous)
        limit_names = names.radio("Select limit of unique categories", [10,20,30])
        valid_columns_categorical = [i for i in data_columns if data[i].nunique()<limit_names]
        feature_names = names.selectbox("Select the categorical list", valid_columns_categorical)


        submit = st.button("Submit")
        if submit:
            result = visual.piechart(data,feature_values,feature_names)
            try:
                st.plotly_chart(result)
            except:
                st.write(result)