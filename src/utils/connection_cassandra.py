from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
from pathlib import Path
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel
import pandas as pd


class cassandra_user:
    def connect(self):
        dir_path = os.path.join((Path(__file__).resolve().parent.parent.parent),'files')
        file_path = os.path.join(dir_path,'secure-connect-onlineedaautomation.zip')
        cloud_config= {
        'secure_connect_bundle': file_path
                        }
        auth_provider = PlainTextAuthProvider('lmzksofvDqTOMcKEvCHkxxDq', 'QYJD5.tkio5FmTy.egAUkW,YoSi24UZRJcEeRerAA+0btYbZ6ZtSSdERAJeN.T.Wo_5no_GIxW0Dr+bc1R,Ue+3.,7-,cca6+bgQsezAUItB64U0zfkwvhn9DRn_bqXX')
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

    def adduser(self,query):
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
        # email text, project_name text PRIMARY KEY, project_description text, source text, filename text
        info = session.execute(query)
        return info.all()