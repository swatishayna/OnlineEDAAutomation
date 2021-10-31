import streamlit as st
import numpy as np
from src.utils import advanced_def,uploaded_file
import pandas as pd
from src.streamapps.stream_uploadapp import upload_data
from pathlib import Path

def app():
    @st.cache
    def load_data(self):
        filename = 
        mongo_result = uploaded_file.Database().retrieve_data(filename)
        df = pd.DataFrame(mongo_result[0]).reset_index(drop=True)
        return




    analysis = advanced_def.Advancedanalysis()
    operation_list = ["correlation"]
    choice = st.sidebar.selectbox("Data Type",operation_list)
    
    if choice == "correlation":
        def description():
            expander = st.expander("Pearson")
            expander.write(""" The Pearson's correlation coefficient (r) is a measure of 
            linear correlation between two variables. It's value lies between
            -1 and +1, -1 indicating total negative linear correlation, 0 indicating 
            no linear correlation and 1 indicating total positive linear correlation.
            Furthermore, r is invariant under separate changes in location and scale 
            of the two variables, implying that for a linear function the angle to the
            x-axis does not affect r.To calculate r for two variables X and Y, one divides
            the covariance of X and Y by the product of their standard deviations.""")
            expander = st.expander("Spearman")
            expander.write(""" The Spearman's rank correlation coefficient (ρ) 
            is a measure of monotonic correlation between two variables, 
            and is therefore better in catching nonlinear monotonic correlations 
            than Pearson's r. It's value lies between -1 and +1, -1 indicating 
            total negative monotonic correlation, 0 indicating no monotonic 
            correlation and 1 indicating total positive monotonic correlation.
            To calculate ρ for two variables X and Y, one divides the covariance
            of the rank variables of X and Y by the product of their standard deviations.""")
            expander = st.expander("Kendell")
            expander.write(""" Similarly to Spearman's rank correlation coefficient,
            the Kendall rank correlation coefficient (τ) measures ordinal
            association between two variables. It's value lies between
            -1 and +1, -1 indicating total negative correlation,
            0 indicating no correlation and 1 indicating total
            positive correlation.To calculate τ for two variables
            X and Y, one determines the number of concordant and
            discordant pairs of observations. τ is given by the
            number of concordant pairs minus the discordant pairs
            divided by the total number of pairs""")

        user_choice = st.sidebar.radio("Choose",
                                        ("View Correlation for all Columns", "View Correlation w.r.t Target column"))

        if user_choice == "View Correlation for all Columns":
            chosen_method = st.sidebar.selectbox('Select the method: ', ('pearson', 'spearman', 'kendall'))
            graph_matrix_choice = st.selectbox("", ('Graph', 'Matrix'))
            st.write(chosen_method.capitalize() + " Correlation Matrix")
            result = analysis.generate_matrix_graph(chosen_method, graph_matrix_choice)
            if graph_matrix_choice == 'Matrix':
                st.write(result)
            else:
                st.plotly_chart(result)
            st.header("Check Description")
            description()

        else:
            data_columns = self.analysis.data1.columns

            select_label = st.sidebar.selectbox('select your label col',
                                                ([i for i in data_columns ]))
            #if data_type[i] == 'float64' or data_type[i] == 'int64'
            if select_label:
                chosen_method = st.sidebar.selectbox('choose correlation type', ('pearson', 'spearman', 'kendall'))
                if chosen_method:
                    st.subheader(
                        chosen_method.capitalize() + " Correlation Matrix wrt Target " + select_label + " method- " + chosen_method)

                    result = self.analysis.generate_label_correlation(chosen_method, select_label)
                    st.write(result[0])
                    st.subheader("\n\nCorrelation Graph - " + chosen_method + " Method")
                    st.plotly_chart(result[1])
                    description()
        