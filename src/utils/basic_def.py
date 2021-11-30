import pandas as pd


class Basic:
    

    def get_shape(self,data):
        return data.shape

    def get_missing_value(self):
        return self.data.isnull()

    def get_count_missing_value(self):
        return self.data.isnull().sum()

    def get_percentage_missing_values(self, missing_value_count):
        return missing_value_count/len(self.data)

    # This Function  is used to get column names
    def get_columns_names(self, df):
        column = pd.DataFrame(df.columns)
        return column

    # This function is to get a small description of dataset
    def describe_dataset(self, df):
        describe = df.describe()
        return describe

    # This function is used to get datatypes of the columns
    def get_datatype_list(self, df):
        a = [i for i in df.dtypes]
        b = [i for i in df.columns]
        c = [str(i) for i in a]
        datatype_list = {b[i]:c[i] for i in range(len(a))}
        return pd.Series(datatype_list)

    # This function is used to get Duplicate rows in a dataset
    def get_duplicate_rows(self, df):
        Duplicates = df[df.duplicated()]
        return Duplicates

