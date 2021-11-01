import streamlit as st
from src.utils import uploaded_file
import pandas as pd
import os
import logging as lg
from xml.etree import ElementTree as ET
from pathlib import Path
import mysql.connector as connection




def app():
    st.header("Data Ingestion")
    


                    #['CSV','CSV from HTML','JSON','EXCEL',"SQL-DB",'Mongo-DB','Cassandra',"TVS","XML"]

    Data_Getter  = ['CSV','CSV from HTML','EXCEL','JSON','TSV',"SQL-DB"]
                    #['Cassandra',"XML"]


    choice = st.sidebar.selectbox("Data Type",Data_Getter)

    if choice == "CSV":
        st.subheader("Upload the CSV file")
        datafile = st.file_uploader("Upload CSV", type=['csv'])
        try : 
            if datafile is not None:
                file_details = {"FileName":datafile.name,"FileType":datafile.type}
                df = pd.read_csv(datafile, sep =",")
                st.dataframe(df)
                uploaded_file.save_uploaded_file(datafile)
                filename = datafile.name.split(".")[0]
                #saving to mongo_db
                uploaded_file.Database().upload_data(df,filename)
                
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
            filename = table
            mongo_result = uploaded_file.Database().retrieve_data(table,client_secret, db)
            df = pd.DataFrame(mongo_result[0]).reset_index(drop=True)
            st.dataframe(df)

            ## saving file to local repo for temporary check
            
            uploaded_file.Database().save_mongodf(df,data_path,table+'.csv')
            uploaded_file.Database().upload_data(df,filename)
            st.write("Data has been successfully uploaded")


    elif choice == 'CSV from HTML':

        with st.form("CSV from HTML"):
            try:
                link = st.text_input('Enter the html link of CSV file') # Need to check once again for an eror. 
                link_submitted = st.form_submit_button("Execute")

                if link_submitted :
                    if link is not None:
                        df = pd.read_csv(link)
                        st.dataframe(df)
                        df.to_csv("src\\data\\"+link.split('/')[-1]+".csv", index = False)
                        st.success("Saved file '{}'' in data folder".format(link.split('/')[-1]))
                    else:
                        message = "Something went wront while saving the CSV file."
                        st.error(message)

                else:
                    st.info("Enter the CSV link and kindly have an active internet connection.")

            except Exception as e:
                message = "Something went wrong wiht 'CSV from HTML' file. Kindly choose right advance options and try one again. "
                st.error( message +"\n{}".format(e))
                lg.error(message)




    elif choice == "JSON":
        st.subheader("Upload the JSON file")
        datafile = st.file_uploader("Upload JSON file", type=['json'])
        try:
            if datafile is not None:
                file_details = {"FileName":datafile.name,"FileType":datafile.type}
                df = pd.read_json(datafile)
                st.dataframe(df)
                uploaded_file.save_uploaded_file(datafile)
        except Exception as e:
            message = "Something went Wrong with your JSON file. Kindly choose right advance options and try once again."
            st.error(message+ "\n {}".format(e))
            lg.error(message)

        
    
    elif choice == "EXCEL":
        st.subheader("Upload the EXCEL file")
        datafile = st.file_uploader("Upload EXCEL", type=['xls','xlsx'])
        try:
            if datafile is not None:
                file_details = {"FileName":datafile.name,"FileType":datafile.type}
                df = pd.read_excel(datafile)
                st.dataframe(df)
                uploaded_file.save_uploaded_file(datafile)
        except Exception as e:
            message = "Something went Wrong with your EXCEL file. Kindly choose right advance options and try once again."
            st.error(message+ "\n {}".format(e))
            lg.info(message)

    
    elif choice == "SQL-DB":         #   Ctrl + /  
        st.subheader("Enter your MySQL credentials.")

        col1, col2 = st.columns(2)

        with col1:
            with st.form(key = "Credentials form"):
                Host = st.text_input("Enter Host credentials.")
                Database = st.text_input("Enter Database credentials.")
                User = st.text_input("Enter User credentials.Type 'root' for default.")
                Password = st.text_input("Enter Password credentials")
                Table = st.text_input("Enter the Table name.")
                submit_credentials = st.form_submit_button("Execute")
                
                   
        with col2:
            if submit_credentials :
                
                try:
                    mydb = connection.connect(host = Host,database = Database, user = User, password = Password, use_pure = True)

                    if mydb.is_connected():
                         st.success("MySQL credentials is successfully applied. ")
                         try :
                            df = pd.read_sql("select * from {}".format(Table),mydb)
                            st.dataframe(df)
                            df.to_csv("src\\data\\"+Table+".csv", index = False)
                            st.success("Saved file '{}'' in data folder.".format(Table))
                         except Exception as e:
                            message = "Kindly enter the correct table name."
                            st.error(message+"\n{}".format(e))
                except Exception as e:
                    message ="Kindly enter the right credentials."
                    st.error(message+"\n {}".format(e))

                          

            else:
                message = "Kindly login into your MySQL before giving the credentials."
                st.info(message)


    
    
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


    elif choice == "TSV":

        st.subheader("Upload the TSV file")
        datafile = st.file_uploader("Upload the TVS file", type=['tsv','txt','csv'])
        try:
            if datafile is not None:
                file_details = {'FileName': datafile.name, "FileType" : datafile.type}
                df = pd.read_csv(datafile, sep='\t')
                st.dataframe(df)
                uploaded_file.save_uploaded_file(datafile)

        except Exception as e:
            message = "Something went Wrong with your TVS file. Kindly choose right advance options and try once again."
            st.error(message+ "\n {}".format(e))
            lg.info(message)
    
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