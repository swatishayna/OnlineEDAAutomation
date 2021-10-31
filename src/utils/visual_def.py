import pandas as pd
import numpy as np
import plotly.express as px
import os


class Visualization:
    def boxplot(self,data,column,axis='x axis'):
        if axis == 'x axis':
            return px.box(data, x = data[column] )
        else:
            return px.box(data, y = data[column] )


    def boxplot_all(self,data, column_list,axis):
        all_boxplot = []
        for col in column_list:
            if axis == 'x axis':
                fig = px.box(data, x = data[col] )
            else:
                fig = px.box(data, y = data[col] )
            all_boxplot.append(fig)
        return all_boxplot


    def distributionplot(self, data, column):
        try:
            return px.histogram(data,x = column)
        except:
            return "Histogram couldnt be generated"

    def distributionplot_all(self,data, column_list):
        all_distplot = []
        for col in column_list:
            fig = px.histogram(data, x = data[col] )
            all_distplot.append(fig)
        return all_distplot
