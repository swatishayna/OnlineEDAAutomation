import streamlit as st
from src.utils import uploaded_file
import pandas as pd
import uuid
from logger_application import logger
from src.utils.connection_cassandra import cassandra_user


def app():
    st.header("Add Project")
    
    uploaded_file.delete_create_data_directory()

    

    email = st.text_input("Enter your registered emailid here")
    Data_Getter  = ['CSV','EXCEL','TSV','Mongo-DB']
    Project_Name = st.text_input("Enter the name of your Project here")
    description = st.text_input("Enter the description of Project here")
    select_source = st.selectbox('Select Data Source',Data_Getter , key=2)
    
    file_obj = open(uploaded_file.get_log_file(), "a+")
    obj_logger =logger.App_Logger()

    
    if select_source == "CSV":
        log_writer_id = str(uuid.uuid4())
        obj_logger.log(file_obj, email, "Selected CSV", log_writer_id)
        st.subheader("Upload the CSV file")
        datafile = st.file_uploader("Upload CSV", type=['csv'])
        try : 
            if datafile is not None:
                file_details = {"FileName":datafile.name,"FileType":datafile.type}
                df = pd.read_csv(datafile, sep =",")
                st.dataframe(df)
                uploaded_file.save_uploaded_file(datafile)
                file_name = datafile.name.split(".")[0]
                log_writer_id = str(uuid.uuid4())
                obj_logger.log(file_obj, email, "DATA LOADED TO DIRECTORY", log_writer_id)

        except Exception as e:
            message = "Something went Wrong with your CSV file. Kindly choose right advance options and try once again."
            log_writer_id = str(uuid.uuid4())
            obj_logger.log(file_obj, email, message, log_writer_id)
            st.error(message+ "\n {}".format(e))


    elif select_source == 'Mongo-DB':
        log_writer_id = str(uuid.uuid4())
        obj_logger.log(file_obj, email, "Selected Mongodb", log_writer_id)

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
                message = "Data has been successfully uploaded"
                log_writer_id = str(uuid.uuid4())
                obj_logger.log(file_obj, email, message, log_writer_id)
                st.write(message)
        except:
            pass


    elif select_source == 'CSV from WEB':
        log_writer_id = str(uuid.uuid4())
        obj_logger.log(file_obj, email, "Selected CSV from WEB", log_writer_id)

        with st.form("CSV from HTML"):
            try:
                link = st.text_input('Enter the html link of CSV file') # Need to check once again for an eror.
                link_submitted = st.form_submit_button("Execute")
                datafile = link.split('/')[-1]+".csv"
                if link_submitted :
                    if link is not None:
                        try:
                            df = pd.read_csv(link)
                        except:
                            df = pd.read_csv(link, sep = "\t")
                        st.dataframe(df)
                        #df.to_csv("src\\data\\"+link.split('/')[-1]+".csv", index = False)
                        uploaded_file.save_uploaded_file(datafile)
                        file_name = datafile.split(".")[0]
                        st.success("Saved file '{}'' in data folder".format(link.split('/')[-1]))
                    else:
                        message = "Something went wront while saving the CSV file."
                        log_writer_id = str(uuid.uuid4())
                        obj_logger.log(file_obj, email, message, log_writer_id)
                        st.error(message)

                else:
                    log_writer_id = str(uuid.uuid4())
                    obj_logger.log(file_obj, email, "CSV LINK NEEDS TO BE ENTERED", log_writer_id)
                    st.info("Enter the CSV link and kindly have an active internet connection.")

            except Exception as e:
                message = "Something went wrong wiht 'CSV from HTML' file. Kindly choose right advance options and try one again. "
                st.error( message +"\n{}".format(e))


    elif select_source == "JSON":
        log_writer_id = str(uuid.uuid4())
        obj_logger.log(file_obj, email, "Selected JSON", log_writer_id)
        st.subheader("Upload the JSON file")
        datafile = st.file_uploader("Upload JSON file", type=['json'])
        try:
            if datafile is not None:
                file_details = {"FileName":datafile.name,"FileType":datafile.type}
                df = pd.read_json(datafile)
                st.dataframe(df)
                uploaded_file.save_uploaded_file(datafile)
                file_name = datafile.name.split(".")[0]
        except Exception as e:
            message = "Something went Wrong with your JSON file. Kindly choose right advance options and try once again."
            log_writer_id = str(uuid.uuid4())
            obj_logger.log(file_obj, email, message, log_writer_id)
            st.error(message+ "\n {}".format(e))


    elif select_source == "EXCEL":
        log_writer_id = str(uuid.uuid4())
        obj_logger.log(file_obj, email, "Selected Excel", log_writer_id)
        st.subheader("Upload the EXCEL file")
        datafile = st.file_uploader("Upload EXCEL", type=['xls','xlsx'])
        try:
            if datafile is not None:
                file_details = {"FileName":datafile.name,"FileType":datafile.type}
                df = pd.read_excel(datafile)
                st.dataframe(df)
                uploaded_file.save_uploaded_file(datafile)
                file_name = datafile.name.split(".")[0]
                log_writer_id = str(uuid.uuid4())
                obj_logger.log(file_obj, email, "DATA UPLOADED TO DIRECTORY", log_writer_id)
        except Exception as e:
            message = "Something went Wrong with your EXCEL file. Kindly choose right advance options and try once again."
            log_writer_id = str(uuid.uuid4())
            obj_logger.log(file_obj, email, message, log_writer_id)
            st.error(message+ "\n {}".format(e))


    elif select_source == "TSV":
        log_writer_id = str(uuid.uuid4())
        obj_logger.log(file_obj, email, "Selected TSV", log_writer_id)
        st.subheader("Upload the TSV file")
        datafile = st.file_uploader("Upload the TVS file", type=['tsv','txt','csv'])
        try:
            if datafile is not None:
                file_details = {'FileName': datafile.name, "FileType" : datafile.type}
                df = pd.read_csv(datafile, sep='\t')
                st.dataframe(df)
                uploaded_file.save_uploaded_file(datafile)
                file_name = datafile.name.split(".")[0]
                log_writer_id = str(uuid.uuid4())
                obj_logger.log(file_obj, email, "DATA UPLOADED TO DIRECTORY", log_writer_id)

        except Exception as e:
            message = "Something went Wrong with your TVS file. Kindly choose right advance options and try once again."
            log_writer_id = str(uuid.uuid4())
            obj_logger.log(file_obj, email, message, log_writer_id)
            st.error(message+ "\n {}".format(e))

######################################################################################################################################

    submit_form = st.button('Add Project')
    if submit_form:
        log_writer_id = str(uuid.uuid4())
        obj_logger.log(file_obj, email, "Submitted the project", log_writer_id)
        cassandra = cassandra_user()
        user = cassandra.get_useraccount(f"SELECT * FROM user WHERE email = '{email}' ALLOW FILTERING ")
        
        
        if user.shape[0] >  0 :
            file = email + '_' + Project_Name + '_onlineeda_' + file_name
            try:
                df = uploaded_file.read_datafolder()
            except:
                pass
            finally:
                uploaded_file.Database().upload_data(df,file)
            status = uploaded_file.Database().check_existing_collection(file)
            if status:
                project_name = email +'_'+ Project_Name
                try:
                    cassandra.add_project(f"INSERT INTO project (email, project_name, project_description, source, filename) VALUES ('{email}', '{project_name}', '{description}', '{select_source}','{file_name}')")
                    log_writer_id = str(uuid.uuid4())
                    obj_logger.log(file_obj, email, "Project Added", log_writer_id)
                    st.write("Project Added")
                except Exception as e:
                    log_writer_id = str(uuid.uuid4())
                    obj_logger.log(file_obj, email, str(e), log_writer_id)
                    st.write(" There is some Issue ")

            else:
                log_writer_id = str(uuid.uuid4())
                obj_logger.log(file_obj, email, "Dataset Not Present", log_writer_id)
                st.write("Dataset Not Present")
        else:
            log_writer_id = str(uuid.uuid4())
            obj_logger.log(file_obj, email, "Entered emailid is not registered", log_writer_id)
            st.write("Entered emailid is not registered")



