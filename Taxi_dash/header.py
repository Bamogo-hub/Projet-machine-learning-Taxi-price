import streamlit as st
from PIL import Image  # Pillow

def show_header():
    # Charger l'image
    img = Image.open("Images/freedom.jpg")  # Chemin vers l'image

    # Diviser l'espace pour l'image et le titre
    col1, col2 = st.columns([5, 1], gap="small")  # Réduire l'espacement entre les colonnes
    with col1: 
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #FFA500; margin: 0; font-size: 30px;">
                    NYC Taxi Fare Predictions
            </h1>
        </div>
        """,
        unsafe_allow_html=True,
        )  
    with col2:
        st.image(img)  # Afficher l'image avec une taille contrôlée
    st.divider()