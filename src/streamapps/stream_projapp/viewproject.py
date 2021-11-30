import streamlit as st
from src.utils.connection_cassandra import cassandra_user
from src.utils.uploaded_file import save_dataset, onlyprojname





def app():
    st.header("View Project")
    st.write("Reverify your credentials")

    form = st.form(key='my-form')

    email = form.text_input("Enter your registered emailid here")
    password = form.text_input("Enter password here")
    current_project_name = form.text_input("Enter the name of the project to work with")
    submit = form.form_submit_button('Submit')
    if submit:
        cassandra = cassandra_user()
        user = cassandra.get_useraccount(f"SELECT * FROM user WHERE email = '{email}'  AND Password = '{password}' ALLOW FILTERING ")

        if len(user) > 0:
            project_list = cassandra.get_useraccount(
                f"SELECT project_name, project_description,filename FROM project WHERE email = '{email}' ALLOW FILTERING ")
            project_list['existing_projects'] = project_list[['project_name']].apply(onlyprojname, axis=1)
            st.dataframe(project_list[['existing_projects', 'project_description', 'filename']])
            if current_project_name:
                try:
                    file_name = project_list[project_list['existing_projects'] == current_project_name]['filename'].iloc[0]
                    collection_name = email + '_' + current_project_name + '_onlineeda_' + file_name
                    try:
                        save_dataset(collection_name)
                    except:
                        st.write("Dataset doesnt exist Provide Dataset")

                except:
                    st.write('Project Doesnt Exist!! Choose from Above Existing Projects or Add new Project')

            else:
                st.write("Perform EDA on any of your dataset")
        else:
            st.write('Email id is not registered')







