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

        col1, col2,col3 = st.columns(3)
        feature_x = col1.selectbox('X', data_columns)
        feature_y = col2.selectbox('Y',data_columns)
        feature_z = col3.selectbox('Z', data_columns)

        submit = st.button("ShowPlot")
        if submit:
            result = visual.surfaceplot(data,feature_x,feature_y,feature_z)
            try:
                st.plotly_chart(result)
            except:
                st.write(result)
    except:
        st.write(data)