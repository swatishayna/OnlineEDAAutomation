import pandas as pd
import os
from pathlib import Path

class Basic:
    def get_data(self, filename):
        data_directory_path = os.path.join((Path(__file__).resolve().parent.parent),'data')
        file_path = os.path.join(data_directory_path,filename)
        return pd.read_csv(file_path)

    def get_shape(self,data):
        return data.shape

    def get_missing_value(self):
        return self.data.isnull()

    def get_count_missing_value(self):
        return self.data.isnull().sum()

    def get_percentage_missing_values(self, missing_value_count):
        return missing_value_count/len(self.data)