import streamlit as st

# Custom imports
from src.streamapps.multipage import MultiPage
from src.streamapps import upload, edabasic,edaadvanced, visual

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Online EDA Application")

# Add all your applications (pages) here
app.add_page("Upload Data", upload.app)
app.add_page("BasicEDA", edabasic.app)
app.add_page("AdvancedEDA",edaadvanced.app)
app.add_page("VisualEDA", visual.app)

# app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()