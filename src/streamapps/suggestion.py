import streamlit as st
from src.utils.connection_cassandra import cassandra_user

def app():
    st.header("Welcome To Suggestion Page")
    st.write("(You can leave your suggestion in the suggestion form.Our Team will look into it)")
    st.write("\n\n\n")

    st.subheader("       SUGGESTION FORM               ")
    form = st.form(key='my-form')

    email = form.text_input("Enter your registered emailid here")
    name  = form.text_input("Enter Your name here")
    suggestion = form.text_input("Write Your Suggestion")
    submit = form.form_submit_button('Submit')

    if submit:
        cassandra = cassandra_user()
        response = cassandra.add_suggestion(email,name,suggestion)
        st.write(response)