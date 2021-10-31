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


    def linechart(self,data,feature_x,feature_y):
        x_axis = list(data[feature_x])
        y_axis = list(data[feature_y])
        
        try:
            fig = px.line(data, x=x_axis, y=y_axis,markers = True)
            return fig
        except:
            return "Plot cant be generated due to data insufficiency"
        


    def meshplot(self,data,feature_x, feature_y,feature_z,feature_size):
        x_axis = list(data[feature_x])
        y_axis = list(data[feature_y])
        z_axis = list(data[feature_z])
        size = list(data[feature_size])
        try:
             fig = px.scatter_3d(data, x=x_axis, y=y_axis, z=z_axis, size=size)
             return fig
        except:
            return "Plot cant be generated due to data insufficiency"
        

    def piechart(self,data,feature_values,feature_names):
        fig = px.pie(data, values=feature_values, names =feature_names )
        return fig

    def scatterchart(self,data,feature_x,feature_y,feature_z,feature_size):
        x_axis = list(data[feature_x])
        y_axis = list(data[feature_y])
        z_axis = list(data[feature_z])
        size   = list(data[feature_size])
        
        try:
            fig = px.scatter_3d(data, x=x_axis, y=y_axis, z=z_axis, size=size)
            return fig
        except:
            return "Plot cant be generated due to data insufficiency"
        
    def barplot(self,data,feature_x,feature_y):
        x_axis = list(data[feature_x])
        y_axis = list(data[feature_y])
        
        try:
            fig = px.bar(data, x=x_axis, y=y_axis)
            return fig
        except:
            return "Plot cant be generated due to data insufficiency"

    def scatterplot(self,data,feature_x,feature_y):
        x_axis = list(data[feature_x])
        y_axis = list(data[feature_y])
        try:
            fig = px.scatter(df,x=x_axis,y=y_axis)
            return fig
        except:
            return "Plot cant be generated due to data insufficiency"