import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime, time
from header import show_header

# Charger la base de données des lieux
data_lieux = pd.read_excel("Places_data/data_lieux.xlsx")  # À adapter selon ton fichier

def show_page():
    show_header()
    
    # Diviser la page en 2 colonnes
    col1, col2 = st.columns([1, 1.5])  # Colonne 1 pour l'input utilisateur, Colonne 2 pour la carte
    
    # COLONNE GAUCHE (Input utilisateur)
    with col1:
        st.subheader("Informations")
        
        # Sélection du lieu de départ
        pickup_location = st.selectbox("Lieu de départ", data_lieux['nom_lieu'])
        pickup_lat = data_lieux[data_lieux['nom_lieu'] == pickup_location]['latitude'].values[0]
        pickup_lon = data_lieux[data_lieux['nom_lieu'] == pickup_location]['longitude'].values[0]

        # Sélection du lieu d'arrivée
        dropoff_location = st.selectbox("Lieu d'arrivée", data_lieux['nom_lieu'])
        dropoff_lat = data_lieux[data_lieux['nom_lieu'] == dropoff_location]['latitude'].values[0]
        dropoff_lon = data_lieux[data_lieux['nom_lieu'] == dropoff_location]['longitude'].values[0]

        # Date et heure
        current_date = datetime.now().date()
        current_time = datetime.now().time()
        default_date = st.date_input("Date du trajet", value=current_date)
        default_time = st.time_input("Heure du trajet", value=time(current_time.hour, current_time.minute))
        
        # Nombre de passagers
        passengers = st.number_input("Nombre de passagers", min_value=1, max_value=6, value=1, step=1)
        
        # Bouton pour prédire le tarif
        if st.button("Prédire le tarif"):  
            fare_prediction = 15.50  # Remplacer par ton modèle de prédiction
            st.success(f"Tarif estimé : ${fare_prediction:.2f}")

    # COLONNE DROITE (Carte avec Folium)
    with col2:
        st.subheader("Carte interactive de New York")

        # Initialisation de la carte Folium centrée sur New York
        m = folium.Map(location=[pickup_lat, pickup_lon], zoom_start=12)

        # Ajouter un marqueur pour le lieu de départ
        folium.Marker([pickup_lat, pickup_lon], popup=f"Lieu de départ: {pickup_location}", icon=folium.Icon(color="green")).add_to(m)

        # Ajouter un marqueur pour le lieu d'arrivée
        folium.Marker([dropoff_lat, dropoff_lon], popup=f"Lieu d'arrivée: {dropoff_location}", icon=folium.Icon(color="red")).add_to(m)

        # Afficher la carte
        st_folium(m, width=700, height=500)
