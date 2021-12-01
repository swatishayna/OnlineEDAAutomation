import streamlit as st
from src.utils.advanced_def import Advancedanalysis
from src.utils import uploaded_file,visual_def


def app():

    st.header("Advanced Exploratory Data Analysis")
    dataframe = uploaded_file.read_datafolder()
    try:
        advanced = Advancedanalysis(dataframe)

        missing_value_df = advanced.get_missing_value()
        st.dataframe(missing_value_df)
        column_list = missing_value_df[missing_value_df['Missing Value Count'] > 0]['index'].to_list()
        if len(column_list)>0:
            graphical_view = st.checkbox("View graphical distribution of columns with missing values")
            if graphical_view:
                visual = visual_def.Visualization()
                all_results = visual.distributionplot_all(dataframe,column_list)
                for result in all_results:
                    st.plotly_chart(result)
    except:
        st.write(dataframe)
