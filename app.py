import streamlit as st
import pandas as pd

# --- CONFIGURATION DE LA CONNEXION GOOGLE SHEETS ---
# Votre ID de feuille extrait de l'URL
SHEET_ID = "1RWQSre19ZmQl4rzxNcsIwvWlJuu_Nm9RMBKbBwPuYyE"
# Cette URL permet à Python de lire la feuille comme un fichier CSV
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

# Configuration de l'affichage Streamlit
st.set_page_config(page_title="L'Art de l'Éloquence", page_icon="⚖️", layout="wide")

# --- STYLE CSS POUR LES FICHES ---
st.markdown("""
    <style>
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #1E3A8A;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .sens { color: #1E3A8A; font-weight: bold; font-size: 1.1em; }
    .exemple { color: #374151; font-style: italic; background: #f9fafb; padding: 10px; border-radius: 5px; margin-top: 10px; }
    .categorie-tag { color: #6B7280; font-size: 0.8em; text-transform: uppercase; letter-spacing: 1px; }
    </style>
    """, unsafe_allow_html=True)

# --- FONCTION DE CHARGEMENT DES DONNÉES ---
@st.cache_data(ttl=300)  # Rafraîchit les données toutes les 5 minutes
def load_data():
    try:
        # Lecture du Google Sheet
        data = pd.read_csv(URL)
        # Nettoyage des noms de colonnes (enlève les espaces vides)
        data.columns = [c.strip().lower() for c in data.columns]
        return data
    except Exception as e:
        st.error(f"Erreur de connexion : {e}")
        return None

# --- EXECUTION ---
df = load_data()

if df is not None:
    st.sidebar.title("💎 Rosly Eloquence")
    st.sidebar.markdown("---")
    
    # Menu de filtrage par catégorie
    if 'catégorie' in df.columns:
        liste_cat = ["Toutes"] + sorted(df['catégorie'].unique().tolist())
        choix_cat = st.sidebar.selectbox("Choisir une catégorie", liste_cat)
    else:
        st.sidebar.warning("Attention : Colonne 'catégorie' non trouvée dans le Sheets.")
        choix_cat = "Toutes"

    st.title("📖 Ma Bibliothèque d'Éloquence")
    st.caption("Connectée en temps réel à Google Sheets")

    # Filtrage des données
    if choix_cat != "Toutes":
        df_final = df[df['catégorie'] == choix_cat]
    else:
        df_final = df

    # Affichage des fiches
    if not df_final.empty:
        for index, row in df_final.iterrows():
            # On vérifie que les colonnes existent avant d'afficher
            titre = row.get('titre', 'Sans titre')
            sens = row.get('sens', 'Non défini')
            exemple = row.get('exemple', 'Aucun exemple')
            cat = row.get('catégorie', 'Général')

            st.markdown(f"""
                <div class="card">
                    <div class="categorie-tag">{cat}</div>
                    <h3>{titre}</h3>
                    <p class="sens">🔍 Sens : {sens}</p>
                    <p class="exemple">💡 Exemple : {exemple}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Aucune expression trouvée dans cette catégorie.")

else:
    st.warning("⚠️ Impossible de charger les données. Vérifiez que votre Google Sheet est partagé en 'Tous les utilisateurs disposant du lien : Lecteur'.")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write(f"📍 **Lieu :** Pointe-Noire, Congo")
st.sidebar.button("🔄 Rafraîchir les données")
