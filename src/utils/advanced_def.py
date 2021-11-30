import pandas as pd
import plotly.express as px




class Advanced:
    
    def get_missing_value(self, df):
        missing_vale_Df = pd.DataFrame(df.isnull().sum(), columns=['Missing Value Count'])
        missing_vale_Df['Missing Value Percentage'] = (df.isnull().sum() / df.shape[0]) * 100
        missing_vale_Df.reset_index(inplace=True)
        missing_vale_Df.rename(columns={'index': 'column_name'})
        return missing_vale_Df

    def get_categorical_stats(self, df,column):


        categorical_stats = df[column].describe()
        categorical_stats_dict = {}
        categorical_stats_dict['Total data points present'] = df[column].describe().loc['count']
        categorical_stats_dict['Total unique data points present'] = df[column].describe().loc['unique']
        categorical_stats_dict['Top most common value'] = df[column].describe().loc['top']
        categorical_stats_dict['Frequency of the most common value'] = df[column].describe().loc['freq']
        return categorical_stats_dict

    def get_count_value(self, df):

        d = {}
        for column in df.columns:
            key = "total number of categories in " + column
            d[key] = df[column].nunique()

        return d

    def get_categories(self,df,column):
        category_count_df = pd.DataFrame()
        category_count_df['categories'] = df[column].value_counts().index
        category_count_df['Count'] = df[column].value_counts().values
        return category_count_df





    

    


class Advancedanalysis:
    def __init__(self, data):
        self.data = data

    def get_matrix_graph(self, chosen_method, graph_matrix):

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

    def get_label_correlation(self, chosen_method, label):
        try:
            matrix = self.data.corr(method=chosen_method)[label]
            write = self.data.corr(method=chosen_method)[[label]].sort_values(by=label, ascending=False)
            fig = px.imshow(write)
            return matrix, fig
        except:
            return "Correlation Result cant be produced due to data insufficiency"

    def get_missing_value(self, column =None):
        if column is None:
            missing_vale_Df = pd.DataFrame(self.data.isnull().sum(), columns=['Missing Value Count'])
            missing_vale_Df['Missing Value Percentage'] = (self.data.isnull().sum() / self.data.shape[0]) * 100
            missing_vale_Df.reset_index(inplace=True)
            missing_vale_Df.rename(columns={'index': 'column_name'})
            return missing_vale_Df
        else:
            missing_value_dict = {}
            missing_value_dict['Total missing_value'] = self.data[column].isnull().sum()
            missing_value_dict['Percentage of missing_value'] = (self.data[column].isnull().sum()/self.data.shape[0])*100
            return missing_value_dict

    def get_categorical_stats(self,column):
        categorical_stats_dict = {}
        categorical_stats_dict['Total data points present'] = self.data[column].describe().loc['count']
        categorical_stats_dict['Total unique data points present'] = self.data[column].describe().loc['unique']
        categorical_stats_dict['Percentage of unique data points present'] = (self.data[column].describe().loc['unique']/self.data[column].describe().loc['count'])*100
        categorical_stats_dict['Top most common value'] = self.data[column].describe().loc['top']
        categorical_stats_dict['Frequency of the most common value'] = self.data[column].describe().loc['freq']

        return categorical_stats_dict

    def get_count_value(self, column = None):
        d = {}
        if column is None:
            for column in self.data.columns:
                key = "total number of categories in " + column
                d[key] = self.data[column].nunique()
        else:
            key = "total number of categories in " + column
            d[key] = self.data[column].nunique()
        return d

    def get_categories(self,column,order=None):
        category_count_df = pd.DataFrame()
        category_count_df['categories'] = self.data[column].value_counts().index
        category_count_df['Count'] = self.data[column].value_counts().values
        category_count_df['Count_Percentage'] = (self.data[column].value_counts().values / self.data[column].notnull().sum()) * 100
        if order is None :
            return category_count_df
        else:
            if order == "ascending":
                category_count_df = pd.DataFrame(category_count_df).sort_values('Count', ascending=True)
            else:
                category_count_df = pd.DataFrame(category_count_df).sort_values('Count', ascending=False)
            return category_count_df

    def get_zero_count_detail(self,column):
        zero_count_dict = {}
        zero_count_dict['Total zeroes in the column'] = self.data[self.data[column] == 0].shape[0]
        zero_count_dict['Percentage of Total zeroes in the column'] = (self.data[self.data[column] == 0].shape[0]/self.data.shape[0])*100
        return zero_count_dict

    def get_sorted_column(self, column, order, value_head):
        data = self.data.copy()
        if order == "ascending":
            sorted_df = pd.DataFrame(data).sort_values(column,ascending=True).head(value_head)
        else:
            sorted_df = pd.DataFrame(data).sort_values(column, ascending=False).head(value_head)
        return sorted_df

    def get_group(self,column,aggregate_func):
        df = pd.DataFrame(self.data.copy())
        if aggregate_func=="sum":
            df= df.groupby(column).sum()
        elif aggregate_func=="count":
            df = df.groupby(column).count()
        elif aggregate_func=="describe":
            df = df.groupby(column).describe()
        elif aggregate_func=="mean":
            df = df.groupby(column).mean()
        elif aggregate_func == "median":
            df = df.groupby(column).mean()
        return df