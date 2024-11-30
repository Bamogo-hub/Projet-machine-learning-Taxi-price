import streamlit as st
import pandas as pd
from PIL import Image  # Pillow
from pathlib import Path
import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import seaborn as sns
from plotly.subplots import make_subplots
from ydata_profiling import ProfileReport
from yellowbrick.regressor import ResidualsPlot
import ydata_profiling as prf

from header import show_header

def show_page(): 
    show_header() #pour l'en-tête   
    st.markdown(
        """
        <div style="text-align: left;">
            <h3 style="margin: 0; font-size: 20px">  Importation de la base de données (CSV uniquement) </h3>
        </div>
        """,
        unsafe_allow_html=True,
        )
    # Charger une base de données depuis le local
    uploaded_file = st.file_uploader("", type=["csv"])

    # Vérifier si un fichier a été importé
    if uploaded_file is not None:
        # Lire le fichier avec Pandas
        data = pd.read_csv(uploaded_file, sep=";")
        # Afficher les premières lignes du fichier
        st.markdown(
        """
        <div style="text-align: left;">
            <h3 style="margin: 0; font-size: 20px"> Visualisation de la base </h3>
        </div>
        """,
        unsafe_allow_html=True,
        )
        st.dataframe(data.head())
        # Afficher des statistiques descriptives
        st.markdown(
        """
        <div style="text-align: left;">
            <h3 style="margin: 0"; font-size: 5px"> Statistiques descriptives </h3>
        </div>
        """,
        unsafe_allow_html=True,
        )
        st.write(data.describe())

        # Generate a profile report from a Dataset stored as a pandas `DataFrame`.
        profile = ProfileReport(data, title="Profiling Report")
        profile.to_notebook_iframe()  # Used to output the HTML representation to a Jupyter notebook.
        st.divider()
    else:
        st.warning("Veuillez importer un fichier pour commencer les analyses.")
