from datetime import datetime
from src.utils import uploaded_file
import os

class App_Logger:
    def __init__(self):
        pass

    def log(self, file_object, email, log_message, log_writer_id):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")


        file_object.write(
            email+ "_eda_" + log_writer_id + "\t\t" +str(self.date) + "/" + str(self.current_time) + "\t\t"  +email+ "\t\t" +log_message +"\n")

