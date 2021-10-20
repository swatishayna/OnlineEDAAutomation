import os 
import streamlit as st
import pandas as pd


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
		df.to_csv("{}".format(uploaded_file.name), index = False)
		os.chidir("path")

		return st.success("Saved file {} in data folder.".format(uploaded_file.name))

	except Exception as e:
		message = "Something went wrong while saving the CSV in to the data folder"
		st.error(message+"\n {}".format(e))
		#logger.log(message,error)

def save_cassandra_bundle(user,uploaded_file):
	os.mkdir("{}//")
	with open(os.path.join("{}\\config".format(user),uploaded_file.name),'wb') as f:
		f.write(uploaded_file.getbuffer())
	return st.success("Saved file {} in {}'s config folder".format(uploaded_file.name,user))