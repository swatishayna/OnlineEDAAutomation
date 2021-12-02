from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
from pathlib import Path
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel
import pandas as pd
import time
import datetime
from cassandra.query import BatchStatement
import numpy as np


class cassandra_user:
    def connect(self):
        dir_path = os.path.join((Path(__file__).resolve().parent.parent.parent),'files')
        file_path = os.path.join(dir_path,'secure-connect-onlineedaautomation.zip')
        cloud_config= {'secure_connect_bundle': file_path}
        # auth_provider = PlainTextAuthProvider(os.environ.get('EDA_INEURON_CASSANDRA_CLIENTID'),
        #                                       os.environ.get('EDA_INEURON_CASSANDRA_CLIENTSECRET'))
        auth_provider = PlainTextAuthProvider('lmzksofvDqTOMcKEvCHkxxDq',
                                              'QYJD5.tkio5FmTy.egAUkW,YoSi24UZRJcEeRerAA+0btYbZ6ZtSSdERAJeN.T.Wo_5no_GIxW0Dr+bc1R,Ue+3.,7-,cca6+bgQsezAUItB64U0zfkwvhn9DRn_bqXX')

        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()
        return self.session

    def get_useraccount(self,query):
        session = self.connect()
        session.execute("USE user_account")
        simple_statement = SimpleStatement(query, consistency_level=ConsistencyLevel.ONE)
        execute_result = session.execute(simple_statement, timeout=None)
        result = execute_result._current_rows
        return pd.DataFrame(result)

    def add_user(self, query):
        try:
            session = self.connect()
            session.execute("USE user_account")
            info = session.execute(query)
            return info.all()
        except:
            pass

    def add_project(self,query):
        session = self.connect()
        session.execute("USE user_account")
        info = session.execute(query)
        return info.all()

    def delete_record(self,query):
        session = self.connect()
        session.execute("USE user_account")
        session.execute(query)

    def add_suggestion(self,email,name,suggestion_msg):
        session = self.connect()
        session.execute("USE suggestion_db")
        try:
            id_value = email + '_eda_'+str(datetime.datetime.fromtimestamp(time.time()))
            query = f"INSERT INTO suggestion (suggestion_id , name , email, suggestion) VALUES ('{id_value}','{name}','{email}','{suggestion_msg}')"
            session.execute(query)
            return "Suggestion Recorded"
        except Exception as e:
            return "Suggestion Couldnt be REcorded!! Try Again!!"



    def write_to_cassandra(self,df):

        session = self.connect()
        CASSANDRA_PARTITION_NUM = 200
        session.execute("USE user_log")
        prepared_query = session.prepare('INSERT INTO logs(logger_id , log_date , email , log_msg ) VALUES (?,?,?,?)')
        for partition in self.split_to_partitions(df, CASSANDRA_PARTITION_NUM):
            batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)
            for index, item in partition.iterrows():
                batch.add(prepared_query, (str(item[0]), str(item[1]), str(item[2]), str(item[3])))
            session.execute(batch)

    def split_to_partitions(self,df, partition_number):
        permuted_indices = np.random.permutation(len(df))
        partitions = []
        for i in range(partition_number):
            partitions.append(df.iloc[permuted_indices[i::partition_number]])
        return partitions