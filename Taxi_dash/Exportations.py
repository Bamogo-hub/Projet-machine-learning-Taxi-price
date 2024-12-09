import streamlit as st
from PIL import Image  # Pillow
import pandas as pd
from header import show_header 

def show_page(): 
    show_header() #pour l'en-tête   
    st.markdown(
        """
        <div style="text-align: left;">
            <h3 style="margin: 0; font-size: 20px">  Importation de la base (CSV uniquement) </h3>
        </div>
        """,
        unsafe_allow_html=True,
        )
    # Charger une base de données depuis le local
    uploaded_file = st.file_uploader("", type=["csv"]) 
    if uploaded_file is None: 
        st.warning("Veuillez importer un fichier pour commencer les analyses.")
    else :
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
        st.divider()
        st.write ("Prédictions")
    
