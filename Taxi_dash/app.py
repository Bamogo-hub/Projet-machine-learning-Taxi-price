import streamlit as st

# Configuration de l'application
st.set_page_config(page_title="Taxi Fare Dashboard", layout="wide", initial_sidebar_state="expanded")

# Ajouter une image en haut de la barre latérale
st.sidebar.markdown(
    """
    <div style="text-align: left;">
        <img src="https://media.giphy.com/media/SuG8hEiyKDCDe/giphy.gif" alt="Taxi NYC" width="120" style="border-radius: 70%;">
    </div>
    """,
    unsafe_allow_html=True
)

# Menu latéral pour la navigation
menu = st.sidebar.radio("", 
                        ["🏠 Accueil", "📊 Analyses", "⚙️ Modèles", "🚖 Prédictions", "📤 Soumission"])

# Charger les pages en fonction du menu sélectionné
if menu == "🏠 Accueil":
    import Accueil
    Accueil.show_page()
elif menu == "📊 Analyses":
    import Analyses
    Analyses.show_page()
elif menu == "⚙️ Modèles":
    import Modèles
    Modèles.show_page()
elif menu == "🚖 Prédictions":
    import Prédictions
    Prédictions.show_page()
elif menu == "📤 Soumission":
    import Exportations
    Exportations.show_page()
