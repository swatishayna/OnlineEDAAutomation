import streamlit as st
import ssl
import pymongo
import os
import pandas as pd
import json
import re
import numpy as np
from pathlib import Path
import shutil


def get_log_directory_path():
    return os.path.join((Path(__file__).resolve().parent.parent.parent), 'logs')

def delete_and_create_log_directory():
    log_directory_path = get_log_directory_path()
    if os.path.isdir(log_directory_path):
        shutil.rmtree(log_directory_path)
    os.mkdir(log_directory_path)
    os.open(os.path.join(log_directory_path,"eda_logs.txt"), "a+")

def get_log_file():
    log_directory_path = get_log_directory_path()
    log_directory_file_path = os.path.join(log_directory_path,"eda_logs.txt")
    return log_directory_file_path

def get_data_directory_path():
    return os.path.join((Path(__file__).resolve().parent.parent),'data')

def delete_create_data_directory():
    data_directory_path = get_data_directory_path()
    if os.path.isdir(data_directory_path):
        shutil.rmtree(data_directory_path)
    os.mkdir(data_directory_path)

def read_datafolder():
    try:
        data_directory_path = get_data_directory_path()
        files = os.listdir(data_directory_path)
        file_path = os.path.join(data_directory_path,files[0])
        try:
            df = pd.read_csv(file_path)
        except:
            df = pd.read_excel(file_path)
        return df
    except:
        return "There is no Project Running!!Start Project (Project Dashboard-->Add Project or Project Dashboard-->View Project)"

def onlyprojname(column):
    for i in column:
        i = str(i).split("_")[1]
        return i

def save_dataset(filename):
    delete_create_data_directory()
    data_directory_path = get_data_directory_path()
    mongo_connection = Database()
    print(filename)
    mongo_df = mongo_connection.retrieve_data(table = filename)
    mongo_df[0].to_csv(os.path.join(data_directory_path,filename),index = False)
    print("file added")

def save_uploaded_file(file):   #csv
    path = get_data_directory_path()
    try:

        with open(os.path.join(path, file.name), "wb") as f:
            f.write(file.getbuffer())
            return st.success("Saved file {} in data folder. ".format(file.name))
    except Exception as e :
        message = "Something went wrong while saving the file in to the data folder"
        st.error(message+"\n{}".format(e))

def save_csv(data_frame,upload_file):
    try:
        path = os.getcwd()
        os.chdir("src//data")
        data_frame.to_csv("{}".format(upload_file), index = False)
        os.chdir("path")

        return st.success("Saved file {} in data folder.".format(upload_file))

    except Exception as e:
        message = "Something went wrong while saving the CSV in to the data folder"
        st.error(message+"\n {}".format(e))
        #logger.log(message,error)

def save_cassandra_bundle(user,uploaded_file):
    os.mkdir("{}//")
    with open(os.path.join("{}\\config".format(user),uploaded_file.name),'wb') as f:
        f.write(uploaded_file.getbuffer())
    return st.success("Saved file {} in {}'s config folder".format(uploaded_file.name,user))




################################MongoDB################################################


############################
###################
class Database:

    def connect(self, table, client_secret="mongodb+srv://eda:eda@cluster0.vqh6p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",db="dataset"):

        self.table = table
        self.db = db

        client = pymongo.MongoClient(client_secret, ssl_cert_reqs=ssl.CERT_NONE)
        #client = pymongo.MongoClient(client_secret)
        self.mng_db = client[self.db]
        self.collection_name = self.table
        print("66666666666666666666666666666666666666")
        return self.mng_db, self.collection_name

    def retrieve_data(self, table, client_secret=None, db=None):

        self.table = table
        if client_secret:
            self.mng_db, self.collection_name = self.connect(self.table, client_secret, db)
        else:
            self.mng_db, self.collection_name = self.connect(self.table)
        print("fgfdsh%%%%%%%%%%%%%%%%%%%%%")
        # fetching the list of column_names of the data stored
        record = self.mng_db[self.table].find_one()
        column_list = [key for key in record]

        mongo_docs = self.mng_db[self.collection_name].find()

        # create an empty dictionary for the MongoDB documents' fields
        fields = {}

        # go through list of MongoDB documents
        for doc in mongo_docs:

            # iterate key-value pairs of each MongoDB document
            # use iteritems() for Python 2
            for key, val in doc.items():

                # attempt to add field's value to dict
                try:
                    # append the MongoDB field value to the NumPy object
                    fields[key] = np.append(fields[key], val)
                except KeyError:
                    # create a new dict key will new NP array
                    fields[key] = np.array([val])
        series_list = []

        # iterate over the dict of lists
        for key, val in fields.items():

            # convert the 'fields' NumPy arrays into Pandas Series
            if key != "_id":
                fields[key] = pd.Series(fields[key])
                fields[key].index = fields["_id"]

                # put the series with index into a list
                series_list += [fields[key]]

        # create a dictionary for the DataFrame frame dict
        df_series = {}
        for num, series in enumerate(series_list):
            # same as: df_series["data 1"] = series
            df_series['data ' + str(num)] = series

        # create a DataFrame object from Series dictionary
        mongo_df = pd.DataFrame(df_series)
        print(mongo_df)
        # assinging the column names
        mongo_df.columns = column_list[1:]
        return mongo_df, mongo_df.dtypes

    def get_path(self, table, filepath, client_secret, db):
        self.mng_db, self.collection_name = self.connect(table, client_secret, db)
        self.db_cm = self.mng_db[self.collection_name]
        cdir = os.path.dirname(__file__)
        self.file_res = os.path.join(cdir, filepath)
        return self.file_res, self.db_cm

    def read_data(self, table, filepath, filetype, client_secret, db):
        if filepath is None:
            self.file_res, self.db_cm = self.get_path(table, filepath, client_secret, db)
        if filetype == 'csv':
            data = pd.read_csv(self.file_res)
        columns_list = []
        for col in data.columns:
            clean_col = re.sub('[\W]+', '', col)
            columns_list.append(clean_col)
        data.columns = columns_list
        return data

    def insert_data(self, table, df=None, filepath=None, extension=None, client_secret=None, db=None):
        try:
            if df is None:
                data_json = json.loads(
                    self.read_data(table, filepath, extension, client_secret, db).to_json(orient='records'))
            else:

                result = df.to_json(orient='records')
                data_json = json.loads(result)

            self.mng_db, self.collection_name = self.connect(table)
            self.db_cm = self.mng_db[self.collection_name]
            self.db_cm.remove()

            self.db_cm.insert(data_json)
        except:
            print("**********data Cant be inserted from above method ***********")
            self.insert_dataframe_into_collection(table,df)

    def save_mongodf(self, df, filename):
        #path = get_data_directory_path()
        path = os.path.join((Path(__file__).resolve().parent.parent),'data')
        path = os.path.join(path,filename)
        df.to_csv(path)
        print("rrrrrrrrrrrrrrrrrrrrrr")

    def insert_dataframe_into_collection(self, table,data_frame):
        try:
            records = list(json.loads(data_frame.T.to_json()).values())
            self.mng_db, self.collection_name = self.connect(table)
            self.db_cm = self.mng_db[self.collection_name]
            self.db_cm.insert_many(records)
            return len(records)
        except Exception as e:
            print("Nooooooooooooooooooooooooo")

    def upload_data(self, df, table):
        try:
            self.insert_data(table, df)
            print("***************************")

        except:
            pass

    def check_existing_collection(self, table):
        self.mng_db, self.collection_name = self.connect(table)
        status = hasattr(self.mng_db, table)
        return status



class Database_mongoexit:
    def connect(self,client_secret="mongodb+srv://eda:eda@cluster0.vqh6p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",db="dataset"):
        self.db = db

        client = pymongo.MongoClient(client_secret,ssl_cert_reqs=ssl.CERT_NONE)
        self.mng_db = client[self.db]
        return self.mng_db,client

    def get_collection_list(self):
        self.mng_db = self.connect()[0]
        print("yes")
        collection_list = self.mng_db.list_collection_names()
        return collection_list

    def close_connection(self):
        try:
            obj = self.connect()[1]
            obj.close()
            return True
        except:
            return False
