import streamlit as st
import pandas as pd
import ssl
import pymongo
import os
import pandas as pd
import json
import re
import numpy as np
from pathlib import Path
import shutil



def get_data_directory_path():
    return os.path.join((Path(__file__).resolve().parent.parent),'data')


def delete_create_data_directory():
    data_directory_path = get_data_directory_path()
    if os.path.isdir(data_directory_path):
        shutil.rmtree(data_directory_path)
    os.mkdir(data_directory_path)
def read_datafolder():
        data_directory_path = get_data_directory_path()
        files = os.listdir(data_directory_path)
        print(files)
        file_path = os.path.join(data_directory_path,files[0])
        return pd.read_csv(file_path)

def onlyprojname(column):
    for i in column:
        i = str(i).split("_")[1]
        return i
def save_dataset(filename):
    delete_create_data_directory()
    data_directory_path = get_data_directory_path()
    mongo_connection = Database()

    mongo_df = mongo_connection.retrieve_data(table = filename)
    mongo_df[0].to_csv(os.path.join(data_directory_path,filename))
    print("file added")



def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join("src//data",  uploaded_file.name),"wb") as f:
            f.write(uploaded_file.getbuffer())
            return st.success("Saved file {} in data folder. ".format(uploaded_file.name))
    except Exception as e :
        message = "Something went wrong while saving the file in to the data folder"
        st.error(message+"\n{}".format(e))
        # logger.log(message,error)

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

    def connect(self, table,
                client_secret="mongodb+srv://eda:eda@cluster0.vqh6p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
                db="dataset"):

        self.table = table
        self.db = db

        client = pymongo.MongoClient(client_secret, ssl_cert_reqs=ssl.CERT_NONE)

        self.mng_db = client[self.db]
        self.collection_name = self.table
        return self.mng_db, self.collection_name

    def retrieve_data(self, table, client_secret=None, db=None):
        self.table = table
        if client_secret:
            self.mng_db, self.collection_name = self.connect(self.table, client_secret, db)
        else:
            self.mng_db, self.collection_name = self.connect(self.table)

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

    # inserting data into mongodatabase , calling readadata->get_path->connect()
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
            pass

    def save_mongodf(self, df, path, filename):
        self.filename = filename
        path = os.path.join(path, self.filename)
        df.to_csv(path)

    def upload_data(self, df, table):
        try:
            self.insert_data(table, df)
            return 1
        except:
            return 0

    def check_existing_collection(self, table):
        self.mng_db, self.collection_name = self.connect(table)
        status = hasattr(self.mng_db, table)
        #collection_list = self.mng_db.list_collection_names()
        return status


class Database_mongoexit:
    def connect(self,client_secret="mongodb+srv://eda:eda@cluster0.vqh6p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",db="dataset"):
        self.db = db

        client = pymongo.MongoClient(client_secret, ssl_cert_reqs=ssl.CERT_NONE)
        self.mng_db = client[self.db]
        return self.mng_db

    def get_collection_list(self):
        self.mng_db = self.connect()
        print("yes")
        collection_list = self.mng_db.list_collection_names()
        return collection_list