from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
from pathlib import Path
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel
import pandas as pd
import time
import datetime


class cassandra_user:
    def connect(self):
        dir_path = os.path.join((Path(__file__).resolve().parent.parent.parent),'files')
        file_path = os.path.join(dir_path,'secure-connect-onlineedaautomation.zip')
        cloud_config= {'secure_connect_bundle': file_path}
        auth_provider = PlainTextAuthProvider(os.environ.get('EDA_INEURON_CASSANDRA_CLIENTID'),
                                              os.environ.get('EDA_INEURON_CASSANDRA_CLIENTSECRET'))

        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()
        return self.session

    def get_useraccount(self,query):
        session = self.connect()
        session.execute("USE user_account")
        simple_statement = SimpleStatement(query, consistency_level=ConsistencyLevel.ONE)
        execute_result = session.execute(simple_statement, timeout=None)
        result = execute_result._current_rows
        # user_detail = session.execute(query)
        # return user_detail.all()
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