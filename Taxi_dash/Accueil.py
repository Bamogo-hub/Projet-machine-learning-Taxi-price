import streamlit as st
from PIL import Image  # Pillow

from header import show_header

def show_page(): 
    show_header() #pour l'en-tête   
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="margin: 0; font-size: 30px;">
                    Bienvenue !
            </h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("Ce dashoard permet de .....")