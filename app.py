import streamlit as st

# Custom imports
from src.streamapps.multipage import MultiPage
from src.streamapps import edabasic,edaadvanced,visual,upload


# Create an instance of the app
app = MultiPage()


    # Add all your applications (pages) here
app.add_page("Upload Data", upload.app)
app.add_page("BasicEDA",    edabasic.app)
app.add_page("AdvancedEDA", edaadvanced.app)
app.add_page("VisualEDA",   visual.app)
app.run()