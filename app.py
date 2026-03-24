import streamlit as st
import pandas as pd

# Remplacez ceci par l'ID de votre feuille Google Sheets (se trouve dans l'URL)
SHEET_ID = 'VOTRE_ID_DE_FEUILLE_ICI'
SHEET_NAME = 'Feuille1'
URL = https://docs.google.com/spreadsheets/d/1RWQSre19ZmQl4rzxNcsIwvWlJuu_Nm9RMBKbBwPuYyE/edit?usp=sharing

st.set_page_config(page_title="L'Art de l'Éloquence", page_icon="⚖️")

# Fonction pour charger les données (avec cache pour la rapidité)
@st.cache_data(ttl=600) # Rafraîchit toutes les 10 minutes
def load_data():
    return pd.read_csv(URL)

try:
    df = load_data()
    
    st.sidebar.title("💎 Rosly Eloquence")
    cat_list = ["Toutes"] + list(df['catégorie'].unique())
    choix_cat = st.sidebar.selectbox("Catégorie", cat_list)

    st.title("📖 Ma Bibliothèque Connectée")

    # Filtrage
    if choix_cat != "Toutes":
        df = df[df['catégorie'] == choix_cat]

    # Affichage des fiches
    for index, row in df.iterrows():
        with st.container():
            st.markdown(f"""
            <div style="background:white; padding:15px; border-radius:10px; border-left:5px solid #1E3A8A; margin-bottom:10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
                <small style="color:gray;">{row['catégorie']}</small>
                <h3 style="margin:5px 0;">{row['titre']}</h3>
                <p><b>🔍 Sens :</b> {row['sens']}</p>
                <p style="font-style:italic; color:#444;"><b>💡 Exemple :</b> {row['exemple']}</p>
            </div>
            """, unsafe_allow_html=True)

except Exception as e:
    st.error("Erreur de connexion à Google Sheets. Vérifiez l'URL et les droits de partage.")
