import pandas as pd
import numpy as np
import plotly.express as px
import os


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


   