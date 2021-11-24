import streamlit as st
from src.utils import uploaded_file
from src.utils.connection_cassandra import cassandra_user





def app():
    st.header("View Project")
   
    
    form = st.form(key='my-form')
    st.write("Reverify your credentials")
    email = form.text_input("Enter your registered emailid here")
    password = form.text_input("Enter password here")
    submit = form.form_submit_button('View All Existing Projects')
    if submit:
        cassandra = cassandra_user()
        user = cassandra.get_useraccount(f"SELECT * FROM user WHERE email = '{email}'  AND Password = '{password}' ALLOW FILTERING ")
        if len(user) > 0:
            project_list = cassandra.get_useraccount(f"SELECT project_name, project_description FROM project WHERE email = '{email}' ALLOW FILTERING ")
            st.dataframe(project_list)
             