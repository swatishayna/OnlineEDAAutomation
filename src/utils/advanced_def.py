import pandas as pd
import numpy as np
import plotly.express as px
import os
from pathlib import Path

class Advanced:
    def get_data(self, filename):
        data_directory_path = os.path.join((Path(__file__).resolve().parent.parent),'data') # - Written by Suraj
        file_path = os.path.join(data_directory_path,filename)
        return pd.read_csv(file_path)

    def get_missing_value(self, df):
        return df.isnull()

    def get_quantile_stats(self, df):
        q = df.quantile(.2, axis=0)
        return q

    def get_count_value(self, df):
        sr = pd.Series(df)
        cv = sr.value_counts()
        return cv

    def get_crosstab(self, df1, df2):
        ct = pd.crosstab(df1, df2)
        return ct

    def get_groups(self, df, col):
        gb = df.groupby(col)
        return gb

    def get_filtered_info(self, df):
        f = df.filter(items=['fixed acidity', 'citric acid'])
        return f


class Advancedanalysis:
    def __init__(self,data):
        self.data = data
     
    def generate_matrix_graph(self,chosen_method, graph_matrix):
        
        if graph_matrix == 'Matrix':
            try:
                matrix = self.data.corr(method=chosen_method)
            except Exception as e:
                matrix = "Matrix cant be generated"
            finally:
                return matrix
        else:
            fig = px.imshow(self.data.corr(method=chosen_method))
            return fig

    def generate_label_correlation(self,chosen_method,label):
        try:
            matrix = self.data.corr(method=chosen_method)[label]
            write =  self.data.corr(method=chosen_method)[[label]].sort_values(by=label, ascending=False)
            fig = px.imshow(write)
            return matrix,fig
        except:
            return "Correlation Result cant be produced due to data insufficiency"
