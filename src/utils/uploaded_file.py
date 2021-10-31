import os 
import streamlit as st
import pandas as pd
import ssl
import pymongo
import os
import pandas as pd
import json
import re
import numpy as np


def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join("src//data",uploaded_file.name),"wb") as f:
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

class Database:
    ## Connect with cloud mongodb and create collection inside the database
    def connect(self, table, client_secret ="mongodb+srv://test:test@cluster0.ulenu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority" ,db = "eda"):
        
        self.table = table
        
        self.db = db

        
        client = pymongo.MongoClient(client_secret,ssl_cert_reqs=ssl.CERT_NONE)

        self.mng_db = client[self.db]
        self.collection_name = self.table
        return self.mng_db, self.collection_name


    

    def retrieve_data(self,table, client_secret, db):
        self.table =table
        self.mng_db, self.collection_name = self.connect(self.table, client_secret, db)
        #fetching the list of column_names of the data stored
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
        #self.load_data(self.table)
        #assinging the column names
        mongo_df.columns = column_list[1:]
        return mongo_df,  mongo_df.dtypes

    def get_path(self,table,filepath,client_secret,db):
        self.mng_db, self.collection_name=self.connect(table, client_secret, db)
        self.db_cm = self.mng_db[self.collection_name]
        cdir = os.path.dirname(__file__)
        self.file_res = os.path.join(cdir, filepath)
        return self.file_res,self.db_cm

    def read_data(self,table,filepath,filetype, client_secret,db):
        if filepath is None:
            self.file_res, self.db_cm = self.get_path(table,filepath,client_secret,db)
        if filetype == 'csv':
            data = pd.read_csv(self.file_res)
        columns_list =[]
        for col in data.columns:
            clean_col = re.sub('[\W]+','',col)
            columns_list.append(clean_col)
        data.columns = columns_list
        return data

    #inserting data into mongodatabase , calling readadata->get_path->connect()
    def insert_data(self,table,df=None,filepath=None,extension=None,client_secret=None,db=None):
        if df is None:
            data_json = json.loads(self.read_data(table,filepath,extension,client_secret,db).to_json(orient='records'))
        else:
            
            result = df.to_json(orient='records')
            data_json = json.loads(result)
            
        self.mng_db, self.collection_name=self.connect(table)
        self.db_cm = self.mng_db[self.collection_name]
        self.db_cm.remove()
       
        self.db_cm.insert(data_json)

    def save_mongodf(self,df,path,filename):
        self.filename = filename
        path = os.path.join(path,self.filename)
        df.to_csv(path)

    def upload_data(self,df,table):
        # table_raw = table + type
        # self.mng_db, self.collection_name=self.connect(table)
        self.insert_data(table,df)
    
    
    
