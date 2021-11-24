import streamlit as st
import numpy as np
from src.utils import advanced_def,visual_def
import pandas as pd
from src.streamapps.stream_projapp import upload_data
from pathlib import Path
from src.utils.basic_def import Basic

def app():
    basic = Basic()    
    st.header("Visualisation Analysis")
    data = basic.get_data("train.csv")

    data_columns = data.columns
    data_type = data.dtypes
    

    visual = visual_def.Visualization()
    col1, col2 = st.columns(2)
    valid_columns = [i for i in data_columns if data_type[i] == 'float64' or data_type[i] == 'int64']
    feature_x =  col1.selectbox('X', valid_columns)
    feature_y = col2.selectbox('Y', valid_columns)
    submit = st.button("Submit")
    if submit:
        result = visual.linechart(data,feature_x,feature_y)
        try:
            st.plotly_chart(result)
        except:
            st.write(result)
    
    
    
    