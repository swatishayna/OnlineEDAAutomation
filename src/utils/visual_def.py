import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import chart_studio.plotly as py



class Visualization:
    def boxplot(self,data,column,axis='x axis'):
        if axis == 'x axis':
            return px.box(data, x = data[column] )
        else:
            return px.box(data, y = data[column] )

    def frequency_plot(self,data,column):
        dfg = data.groupby([column]).count()
        fig = px.bar(dfg, x=dfg.index, y=dfg.iloc[:,0])
        return fig

    def cumulative_distribution_plot(self,data,column):
        x = data[column].values.tolist()
        cumsum = np.cumsum(x)

        trace = go.Scatter(x=[i for i in range(len(cumsum))], y=10 * cumsum / np.linalg.norm(cumsum),
                           marker=dict(color='rgb(150, 25, 120)'))
        layout = go.Layout(
            title="Cumulative Distribution Function"
        )

        fig = go.Figure(data=go.Data([trace]), layout=layout)
        #return py.iplot(fig, filename='cdf-dataset')
        return fig

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
            fig = px.scatter(data,x=x_axis,y=y_axis)
            return fig
        except:
            return "Plot cant be generated due to data insufficiency"

    def surfaceplot(self,data,feature_x,feature_y,feature_z):
        x_axis = list(data[feature_x])
    
        y_axis = list(data[feature_y])
        
        z_axis = list(data[feature_z])
        
        numerical_columns = data.select_dtypes([np.number]).columns
        z_axis=data[numerical_columns].values
        sh_0, sh_1 = z_axis.shape
        x_axis, y_axis = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
        try:
            fig = go.Figure(data=[go.Surface(z=z_axis, x=x_axis, y=y_axis)])
            fig.update_layout(autosize=False,
        #                   scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
                        width=500, height=500,
                        margin=dict(l=65, r=50, b=65, t=90)
            )
            return fig
        except:
            return "Plot cant be generated due to data insufficiency"
            