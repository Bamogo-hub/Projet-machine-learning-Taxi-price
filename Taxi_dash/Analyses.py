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
from yellowbrick.regressor import ResidualsPlot
import ydata_profiling as prf
import pygwalker as pyg #installer pygwalker au préalable
from pygwalker.api.streamlit import StreamlitRenderer
from header import show_header

def show_page(): 
    show_header() #pour l'en-tête   
    data= pd.read_excel("c:/Users/DELL/Downloads/new-york-city-taxi-fare-prediction/test.xlsx") 
    data_size = len(data)
    # Calcul des statistiques pour fare_amount
    mean_fare = data['fare_amount'].mean()
    max_fare = data['fare_amount'].max()
    min_fare = data['fare_amount'].min()
    # Diviser la page en 5 colonnes pour afficher les boxs
    col1, col2, col3, col4 = st.columns(4)
    # Affichage des informations dans la première colonne
    with col1:
        # Taille de la base
        st.info("Taille de la base")
        st.markdown(
            f"""
            <div style="background: linear-gradient(to bottom, #FF6F00, #FFB74D); padding: 10px; border-radius: 5px; text-align: center;">
                <h3 style="color: white;">{data_size:,}</h3>
            </div>
            """, 
            unsafe_allow_html=True
        )
    with col2:
        # Moyenne de la variable fare_amount
        st.info("Tarif moyen", icon="💵")
        st.markdown(
            f"""
            <div style="background: linear-gradient(to bottom, #FF6F00, #FFB74D); padding: 10px; border-radius: 5px; text-align: center;">
                <h3 style="color: white;">${mean_fare:.2f}</h3>
            </div>
            """, 
            unsafe_allow_html=True
        )
    with col3:
        # Maximum de la variable fare_amount
        st.info("Tarif max", icon="💰")
        st.markdown(
            f"""
            <div style="background: linear-gradient(to bottom, #FF6F00, #FFB74D); padding: 10px; border-radius: 5px; text-align: center;">
                <h3 style="color: white;">${max_fare:.2f}</h3>
            </div>
            """, 
            unsafe_allow_html=True
        )
    with col4:
        # Minimum de la variable fare_amount
        st.info("Tarif min", icon="💸")
        st.markdown(
            f"""
            <div style="background: linear-gradient(to bottom, #FF6F00, #FFB74D); padding: 10px; border-radius: 5px; text-align: center;">
                <h3 style="color: white;">${min_fare:.2f}</h3>
            </div>
            """, 
            unsafe_allow_html=True
        )
    st.subheader("Graphiques") 

    # Liste des colonnes à afficher dans les menus déroulants (sauf 'key')
    columns = [col for col in data.columns if col != 'key']

    """
    # Par défaut, variables sélectionnées
    default_column_1 = 'fare_amount'
    default_column_2 = 'passenger_count'

    # Diviser la page en deux colonnes
    col5, col6= st.columns([1, 1])  # Ajuster le ratio des colonnes

    # COLONNE 5 (Sélection de la première variable et affichage de la distribution)
    with col5:
        
        # Menu déroulant pour sélectionner une variable
        var_1 = st.selectbox("Sélectionner une variable", columns, index=columns.index(default_column_1))
        
        # Afficher le graphique de la distribution de la variable choisie
        st.write(f"Distribution de : {var_1}")
        
        # Tracer la distribution
        plt.figure(figsize=(8, 6))
        sns.histplot(data[var_1], kde=True, color='blue')
        st.pyplot(plt)

    # COLONNE 6 (Sélection de la deuxième variable et affichage de la distribution en fonction de la première)
    with col6:
        # Menu déroulant pour sélectionner la deuxième variable
        var_2 = st.selectbox("Sélectionner une autre variable", columns, index=columns.index(default_column_2))
        
        # Afficher le graphique de la distribution de la deuxième variable en fonction de la première
        st.write(f"Distribution de {var_2} selon {var_1}")
        # Tracer la distribution
        plt.figure(figsize=(8, 6)) 
        sns.scatterplot(x=data[var_1], y=data[var_2], color='green', alpha=0.7)
        st.pyplot(plt)
    """ 
    pyg_app = StreamlitRenderer(data)
    pyg_app.explorer()
