import streamlit as st
from src.utils.advanced_def import Advancedanalysis
from src.utils import uploaded_file,visual_def


def app():
    st.header("Advanced Exploratory Data Analysis")
    dataframe = uploaded_file.read_datafolder()
    try:
        advanced = Advancedanalysis(dataframe)

        option = st.sidebar.radio("View  Complete Analysis of Selected Column", ("numerical_columns","categorical columns"))

        if option =="categorical columns":
            categorical_column_list = [column for column in dataframe.columns if dataframe[column].dtypes == 'object']
            categorical_column = st.sidebar.selectbox("Select Column", categorical_column_list)
            if categorical_column:
                st.header(" Analysis Report of Categorical Column ")
                st.write("\n")

                st.subheader(f"Categorical Statistics of {categorical_column} column")
                st.write(advanced.get_categorical_stats(categorical_column))

                st.subheader(f"Missing Value Detail of column {categorical_column}")
                st.write(advanced.get_missing_value(column = categorical_column))

                st.subheader(f"Graphical Distribution of Missing Values of column {categorical_column}")
                visual = visual_def.Visualization()
                result = visual.distributionplot(dataframe, categorical_column)
                st.plotly_chart(result)

                st.subheader(f"Zero Value Detail of column {categorical_column}")
                st.write(advanced.get_zero_count_detail(column=categorical_column))

                st.subheader("Frequency Count")
                st.dataframe(advanced.get_categories(categorical_column))

                st.subheader(f"frequency_plot for column {categorical_column}")
                result = visual.frequency_plot(dataframe, categorical_column)
                st.plotly_chart(result)


        else:
            numerical_column_list = [column for column in dataframe.columns if dataframe[column].dtypes != 'object']
            numerical_column = st.sidebar.selectbox("Select Column", numerical_column_list)
            if numerical_column:
                st.header(f" Analysis Report of {numerical_column} Numerical Column")

                st.subheader(f"Quantile Stats of {numerical_column}")
                st.write(dataframe[numerical_column].describe())

                st.subheader(f"Get quantile")
                quantile_value = st.slider('Size', max_value=0.0, min_value=1.0)
                if quantile_value:
                    st.write(f"values at the given quantile is {dataframe[numerical_column].quantile(quantile_value)}")

                st.subheader(f"Missing Value Detail of column {numerical_column}")
                st.write(advanced.get_missing_value(column=numerical_column))

                st.subheader(f"Graphical Distribution of Missing Values of column {numerical_column}")
                visual = visual_def.Visualization()
                result = visual.distributionplot(dataframe, numerical_column)
                st.plotly_chart(result)

                st.subheader(f"Zero Value Detail of column {numerical_column}")
                st.write(advanced.get_zero_count_detail(column=numerical_column))

                st.subheader(f"Total number of unique values in {numerical_column}")
                st.write(advanced.get_count_value(column=numerical_column))

                st.subheader(f"Frequency Count {numerical_column}")
                st.dataframe(advanced.get_categories(numerical_column))

                st.subheader(f"Histogram for column {numerical_column}")
                visual = visual_def.Visualization()
                result = visual.distributionplot(dataframe, numerical_column)
                st.plotly_chart(result)

                st.subheader(f"Cumulative Distribution Plot for column {numerical_column}")
                result = visual.cumulative_distribution_plot(dataframe,numerical_column)
                st.plotly_chart(result)

                st.subheader(f"boxplot for column {numerical_column}")
                axis = st.radio("Rotate the graph", ['x axis', 'y axis'])
                result = visual.boxplot(dataframe, numerical_column,axis)
                st.plotly_chart(result)
    except:
        st.write(dataframe)

