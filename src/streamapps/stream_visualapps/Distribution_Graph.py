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

        choice = st.sidebar.radio("",["Generate histogram for all columns", "Select the Column"])
        if choice == "Generate histogram for all columns":
            st.subheader("Histogram for all columns")

            #valid_columns = [i for i in data_columns if data_type[i] == 'float64' or data_type[i] == 'int64']
            all_results = visual.distributionplot_all(data,data_columns)
            for result in all_results:
                st.plotly_chart(result)
        else:
            select_column = st.sidebar.selectbox('select  column',
                                            ([i for i in data_columns if data_type[i] == 'float64' or data_type[i] == 'int64']))
            st.subheader("Histogram for column", select_column)
            result = visual.distributionplot(data,select_column)
            st.plotly_chart(result)
    except:
        st.write(data)