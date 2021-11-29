import streamlit as st

# Custom imports
from src.streamapps.multipage import MultiPage
from src.streamapps import edabasic,edaadvanced,visual,upload
import os
import shutil
from src.utils.uploaded_file import get_data_directory_path
import atexit



#clean data directory
@atexit.register
def on_exit():
    data_directory_path = get_data_directory_path()
    if os.path.isdir(data_directory_path):
        shutil.rmtree(data_directory_path)
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

