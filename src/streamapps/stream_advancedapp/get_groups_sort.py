import streamlit as st
from src.utils.advanced_def import Advancedanalysis
from src.utils import uploaded_file



def app():
    st.header("Advanced Exploratory Data Analysis")
    dataframe = uploaded_file.read_datafolder()
    try:
        advanced = Advancedanalysis(dataframe)

        aggregate_fun_list = ["sum", "count", "describe", "mean", "median"]
        numerical_column_list = [column for column in dataframe.columns if dataframe[column].dtypes != 'object']
        minimum_not_na_data_point_column = dataframe.notna().sum().sort_values()[0]


        option = st.sidebar.selectbox("Choose Operation",["Groupby","Sort DataFrame wrt Column", "Sort Column"])

        if option == "Groupby":
            st.header("Groupby Operation")
            column, aggregate_fun = st.columns(2)
            value_column = column.selectbox("Select Column", dataframe.columns)
            value_aggreagate_func = aggregate_fun.selectbox("Select Function", aggregate_fun_list)
            submit = st.button("Show Result")

            if submit:
                st.header("RESULT")
                result = advanced.get_group(value_column,value_aggreagate_func)
                try:
                    st.dataframe(result)
                except Exception as e:
                    st.write("Try Again")

        elif option == "Sort DataFrame wrt Column":
            st.header("Sort Dataframe")
            st.write("\n\n")
            column,order,head = st.columns(3)
            numerical_column = column.selectbox("Select Column", numerical_column_list)
            value_order = order.selectbox("Select Order", ["ascending", "descending"])
            value_head = head.number_input("View Top Selected Rows", min_value=1, max_value=minimum_not_na_data_point_column, step=1)
            submit = st.button("Show Result")

            if submit:
                st.header("RESULT")
                result = advanced.get_sorted_column(numerical_column, value_order, value_head)
                try:
                    st.dataframe(result)
                except Exception as e:
                    st.write("Try Again")

        elif option == "Sort Column":
            column, order, head = st.columns(3)
            value_column = column.selectbox("Select Column", dataframe.columns)
            value_order = order.selectbox("Select Order by Count(Frequency)", ["ascending", "descending"])
            submit = st.button("Show Result")

            if submit:
                st.header("RESULT")
                result = advanced.get_categories(value_column,value_order)
                try:
                    st.dataframe(result)
                except Exception as e:
                    st.write("Try Again")
    except:
        st.write(dataframe)