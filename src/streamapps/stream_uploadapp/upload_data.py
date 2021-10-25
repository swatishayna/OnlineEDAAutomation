import streamlit as st
from src.utils import uploaded_file
import pandas as pd
import os
import logging as lg
from xml.etree import ElementTree as ET
from pathlib import Path



#def basic_eda(file_details):
 #   if file_details['FileType'] == 'csv':
  #      df= read_csv(file_details['FileName'])


def app():
    st.header("Data Ingestion")

    Data_Getter  = ['CSV','Mongo-DB']
                    #['CSV','CSV from HTML','JSON','EXCEL',"SQL-DB",'Mongo-DB','Cassandra',"TVS","XML"]

    choice = st.sidebar.selectbox("Data Type",Data_Getter)

    if choice == "CSV":
        st.subheader("Upload the CSV file")
        datafile = st.file_uploader("Upload CSV", type=['csv'])
        try : 
            if datafile is not None:
                file_details = {"FileName":datafile.name,"FileType":datafile.type}
                df = pd.read_csv(datafile)
                st.dataframe(df)
                uploaded_file.save_uploaded_file(datafile)
                
        except Exception as e:
            message = "Something went Wrong with your CSV file. Kindly choose right advance options and try once again."
            st.error(message+ "\n {}".format(e))
            lg.error(message)
    
    if choice == 'Mongo-DB':
        

        form = st.form(key='my-form')
        db = form.text_input("Enter the name of your database here")
        client_secret = form.text_input("Enter client secret here")
        table = form.text_input("Enter the name of collection here")
        
        submit = form.form_submit_button('Submit')

        st.write('Press submit to load your dataset')

        if submit:
           
            data_path = os.path.join((Path(__file__).resolve().parent.parent.parent),'data')
            # final = os.path.join(path1,'winequality_red.csv' )
            # loaddata = uploaded_file.Database().insert_data(final,'csv',table,client_secret , db)
            
            #loaddata = uploaded_file.Database().insert_data('../../../src/data/winequality_red.csv','../../../src/data/winequality_red.csv'.split('.')[-1],table,client_username,client_password , db)
            mongo_result = uploaded_file.Database().retrieve_data(table,client_secret, db)
            df = pd.DataFrame(mongo_result[0]).reset_index(drop=True)
            st.dataframe(df)
            uploaded_file.Database().save_mongodf(df,data_path,table+'.csv')
            st.write("Data has been successfully uploaded")


    # elif choice == 'CSV from HTML':
    #     link = st.text_input('Enter the html link of CSV file') # Need to check once again for an eror. 
    #     try:
    #         link = st.text_input('Enter the html link of CSV file')
    #         if link is not None:            
    #             file_details = {'FileName': link.split('/')[-1], "FileType": 'csv'}
    #             df = pd.read_csv(link)
    #             st.dataframe(df)
    #             uploaded_file.save_csv(df,link.split('/')[-1])

            
    #     except Exception as e:
    #             message = "Something went wrong wiht 'CSV from HTML' file. Kindly choose right advance options and try one again. "
    #             st.error( message +"\n{}".format(e))
    #             lg.error(message)




    # elif choice == "JSON":
    #     st.subheader("Upload the JSON file")
    #     datafile = st.file_uploader("Upload JSON file", type=['json'])
    #     try:
    #         if datafile is not None:
    #             file_details = {"FileName":datafile.name,"FileType":datafile.type}
    #             df = pd.read_json(datafile)
    #             st.dataframe(df)
    #             uploaded_file.save_uploaded_file(datafile)
    #     except Exception as e:
    #         message = "Something went Wrong with your JSON file. Kindly choose right advance options and try once again."
    #         st.error(message+ "\n {}".format(e))
    #         lg.error(message)

        
    
    # elif choice == "EXCEL":
    #     st.subheader("Upload the EXCEL file")
    #     datafile = st.file_uploader("Upload EXCEL", type=['xls','xlsx'])
    #     try:
    #         if datafile is not None:
    #             file_details = {"FileName":datafile.name,"FileType":datafile.type}
    #             df = pd.read_excel(datafile)
    #             st.dataframe(df)
    #             uploaded_file.save_uploaded_file(datafile)
    #     except Exception as e:
    #         message = "Something went Wrong with your EXCEL file. Kindly choose right advance options and try once again."
    #         st.error(message+ "\n {}".format(e))
    #         lg.info(message)

    
    # elif choice == "SQL-DB":            Ctrl + / 
    #     st.subheader("Kindly give the credentials of SQL-DB")

    
    
    # elif choice == "Cassandra":
    #     st.subheader("Kindly give the credentials of Cassandra")
    #     user = st.text_input("Enter your username")
    #     datafile = st.file_uploader("Upload the Cassandra Bundle",type =['zip'])
    #     try:
    #     	if datafile is not None:
    #     		file_details={"FileName":datafile.name,"FileType":datafile.type}
    #     		save_cassandra_bundle(user,datafile)
    #     		keyspace = st.text_input("Enter the Keyspace Name")
    #     		client_id =st.text_input("Enter Client ID")
    #     		client_secret = st.text_input("Enter Client Secret")
    #     except Exception as e:
    #         message = "Something went Wrong with your Cassandra file. Kindly choose right advance options and try once again."
    #         st.error(message+ "\n {}".format(e))
    #         lg.info(message)

    # elif choice == "TVS":
    #     st.subheader("Upload the TVS file")
    
    # elif choice == "XML":
    #     st.subheader("Upload the XML file")
    #     datafile = st.file_uploader("Upload XML", type=['xml'])
    #     try:
    #         if datafile is not None:
    #             file_details = {"FileName": datafile.name,"FileType":datafile.type}
    #             temp = ET.parse(datafile)
    #             df = pd.DataFrame(temp)
    #             st.dataframe(df)
    #             uploaded_file.save_uploaded_file(df)
    #     except Exception as e:
    #         message = "Something went Wrong with your XML file. Kindly choose right advance options and try once again."
    #         st.error(message+"\n {}".format(e))
    #         lg.info(message)


           # x = "Git is working."
   