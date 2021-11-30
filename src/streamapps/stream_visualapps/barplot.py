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


        col1, col2 = st.columns(2)
        feature_x = col1.selectbox('X', data_columns)
        feature_y = col2.selectbox('Y', data_columns)
        submit = st.button("Show Plot")
        if submit:
            result = visual.barplot(data,feature_x,feature_y)
            try:
                st.plotly_chart(result)
            except:
                st.write(result)

