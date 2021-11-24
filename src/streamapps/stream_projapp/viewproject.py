import streamlit as st
from src.utils import uploaded_file
import pandas as pd
import os
import logging as lg
from xml.etree import ElementTree as ET
from pathlib import Path
from src.utils.connection_cassandra import cassandra_user





def app():
    st.header("View Project")