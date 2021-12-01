import streamlit as st
from src.utils import visual_def
from src.utils import uploaded_file

def app():
        
    st.header("Advanced Exploratory Visual Data Analysis")
    data = uploaded_file.read_datafolder()
    try:
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
    except:
        st.write(data)

    