import streamlit as st

# Custom imports
from src.streamapps.multipage import MultiPage
from src.streamapps import edabasic,edaadvanced,visual,upload
import os
import shutil
from src.utils.uploaded_file import get_data_directory_path
import atexit
from src.utils.uploaded_file import Database,Database_mongoexit
from src.utils.connection_cassandra import cassandra_user
from src.utils.uploaded_file import onlyprojname
import numpy as np

#clean data directory
@atexit.register
def on_exit():
    data_directory_path = get_data_directory_path()
    if os.path.isdir(data_directory_path):
        shutil.rmtree(data_directory_path)
    mongo_collection_list = Database_mongoexit().get_collection_list()
    file_name_list = [str(i).split('_onlineeda_')[-1] for i in mongo_collection_list]
    print(file_name_list)
    cassandra = cassandra_user()
    project_list = cassandra.get_useraccount("SELECT * FROM project")
    project_list['existing_projects'] = project_list[['project_name']].apply(onlyprojname, axis=1)
    delete_project_df = project_list[np.isin(project_list['filename'], file_name_list, invert=True)]
    print(delete_project_df)
    remove_projects = delete_project_df['project_name'].to_list()
    print(remove_projects)
    cassandra.delete_record(f"DELETE FROM project WHERE project_name IN {tuple(remove_projects)}")

    print("Program Stopped")





try:
    # Create an instance of the app

    apps = MultiPage()

    # Add all your applications (pages) here
    apps.add_page("Project Dashboard", upload.app)
    apps.add_page("BasicEDA",    edabasic.app)
    apps.add_page("AdvancedEDA", edaadvanced.app)
    apps.add_page("VisualEDA",   visual.app)
except:
    pass






if __name__ == "__main__":
    apps.run()

