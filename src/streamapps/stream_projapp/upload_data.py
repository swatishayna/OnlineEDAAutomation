import streamlit as st
from src.utils import uploaded_file
import pandas as pd
import os
import logging as lg
from src.utils.connection_cassandra import cassandra_user





def app():
    st.header("Add Project")
    
    uploaded_file.delete_create_data_directory()
    

    email = st.text_input("Enter your registered emailid here")
    Data_Getter  = ['CSV','CSV from HTML','EXCEL','JSON','TSV',"SQL-DB",'Mongo-DB']
    Project_Name = st.text_input("Enter the name of your Project here")
    description = st.text_input("Enter the description of Project here")
    select_source = st.selectbox('Select Data Source',Data_Getter , key=2)
    
    
    

    
    if select_source == "CSV":
        st.subheader("Upload the CSV file")
        datafile = st.file_uploader("Upload CSV", type=['csv'])
        try : 
            if datafile is not None:
                file_details = {"FileName":datafile.name,"FileType":datafile.type}
                df = pd.read_csv(datafile, sep =",")
                st.dataframe(df)
                uploaded_file.save_uploaded_file(datafile)
                file_name = datafile.name.split(".")[0]

        except Exception as e:
            message = "Something went Wrong with your CSV file. Kindly choose right advance options and try once again."
            st.error(message+ "\n {}".format(e))
            lg.error(message)



##################################################################################################################################  
# 
#  
#     if select_source == 'Mongo-DB':
#
#         form = st.form(key='my-form')
#         db = form.text_input("Enter the name of your database here")
#         client_secret = form.text_input("Enter client secret here")
#         file_name = form.text_input("Enter the name of collection here")
#
#         submit = form.form_submit_button('UploadData')
#
#         st.write('Press UploadData to continue')
#
#         if submit:
#             mongo_result = uploaded_file.Database().retrieve_data(file_name,client_secret, db)
#             df = pd.DataFrame(mongo_result[0]).reset_index(drop=True)
#             st.dataframe(df)
#
#             ## saving file to local repo for temporary check
#             uploaded_file.Database().save_mongodf(df,filename=file_name)
#             st.write("Data has been successfully uploaded")
    elif select_source == 'Mongo-DB':


        db = st.text_input("Enter the name of your database here")
        client_secret = st.text_input("Enter client secret here")
        file_name = st.text_input("Enter the name of collection here")

        try:
            if db is not None and client_secret is not None and file_name is not None:
                mongo_result = uploaded_file.Database().retrieve_data(file_name, client_secret, db)
                df = pd.DataFrame(mongo_result[0]).reset_index(drop=True)
                st.dataframe(df)


                ## saving file to local repo for temporary check
                uploaded_file.Database().save_mongodf(df, filename=file_name)
                print("Hello WOrld")
                #st.write("Data has been successfully uploaded")
        except:
            pass


    elif select_source == 'CSV from HTML':

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


    elif select_source == "JSON":
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


    elif select_source == "EXCEL":
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

    
    elif select_source == "SQL-DB":         
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


    elif select_source == "TSV":

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
######################################################################################################################################




    submit_form = st.button('Add Project')
    if submit_form:
        print("gggggggggggggggggggggggg")
        cassandra = cassandra_user()
        user = cassandra.get_useraccount(f"SELECT * FROM user WHERE email = '{email}' ALLOW FILTERING ")
        
        
        if user.shape[0] >  0 :
            file = email + '_' + Project_Name + '_onlineeda_' + file_name
            try:
                df = uploaded_file.read_datafolder()
            except:
                pass
            finally:
                print("pppppppppppppppppppppppppppppppppp")
                uploaded_file.Database().upload_data(df,file)
            status = uploaded_file.Database().check_existing_collection(file)
            if status:
                project_name = email +'_'+ Project_Name
                try:
                    cassandra.add_project(f"INSERT INTO project (email, project_name, project_description, source, filename) VALUES ('{email}', '{project_name}', '{description}', '{select_source}','{file_name}')")
                    st.write("Project Added")
                except Exception as e:
                    st.write("Issue ")
                    print(e)
            else:
                print("uuuuuuuuuuuuuuuuuuuuuuu")
        else:
            st.write("Entered emailid is not registered")


            #mongodb+srv://test:test@cluster0.ulenu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
            #automate_eda.stage01_cleaned_data
