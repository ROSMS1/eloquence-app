import streamlit as st
import pandas as pd

# --- CONFIGURATION ---
SHEET_ID = "1RWQSre19ZmQl4rzxNcsIwvWlJuu_Nm9RMBKbBwPuYyE"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

st.set_page_config(page_title="Rosly - L'Art de l'Éloquence", page_icon="⚖️", layout="wide")

# --- BASE DE DONNÉES INITIALE ---
expressions_fixes = [
    {"catégorie": "Idiomatique", "titre": "Avoir l'apanage de", "sens": "Posséder un privilège exclusif.", "exemple": "La rigueur n'est pas l'apanage des mathématiciens."},
    {"catégorie": "Idiomatique", "titre": "Sortir de ses gonds", "sens": "Perdre son sang-froid.", "exemple": "Il a fini par sortir de ses gonds."},
    {"catégorie": "Idiomatique", "titre": "Une victoire à la Pyrrhus", "sens": "Une victoire qui équivaut à une défaite.", "exemple": "C'est une victoire à la Pyrrhus : il est ruiné."},
    {"catégorie": "Structure", "titre": "De surcroît / Par ailleurs", "sens": "Ajouter une information avec élégance.", "exemple": "Ce projet est rentable ; de surcroît, il est écologique."},
    {"catégorie": "Structure", "titre": "Force est de constater", "sens": "Présenter un fait comme indiscutable.", "exemple": "Force est de constater que le réseau est instable."},
    {"catégorie": "Persuasion", "titre": "Un levier déterminant", "sens": "Un élément clé pour réussir.", "exemple": "Cette mise à jour est un levier déterminant pour la maintenance."},
    {"catégorie": "Persuasion", "titre": "Sous réserve de...", "sens": "Poser une condition diplomatique.", "exemple": "Accordé, sous réserve d'un rapport technique complet."},
    {"catégorie": "Juridique", "titre": "En l'espèce", "sens": "Dans le cas présent / Précisément.", "exemple": "En l'espèce, la clause de garantie s'applique."},
    {"catégorie": "Juridique", "titre": "Nonobstant", "sens": "Malgré / Bien que.", "exemple": "Il a agi nonobstant les avertissements."},
    {"catégorie": "Physique", "titre": "La Loi d'Ohm (Convalescence)", "sens": "Gérer sa résistance interne.", "exemple": "Baissons l'intensité le temps que votre résistance diminue."},
    {"catégorie": "Physique", "titre": "Effet de Résonance", "sens": "Retrouver son propre rythme.", "exemple": "La guérison est une synchronisation avec son horloge biologique."}
]

# --- STYLE VISUEL ---
st.markdown("""
    <style>
    .card { background: white; padding: 20px; border-radius: 15px; border-left: 6px solid #1E3A8A; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom: 15px; }
    .cat-tag { color: #1E3A8A; font-weight: bold; font-size: 0.8em; text-transform: uppercase; }
    .sens-text { color: #2D3748; font-weight: 500; margin: 10px 0; }
    .ex-text { background: #F3F4F6; padding: 10px; border-radius: 8px; font-style: italic; color: #4B5563; }
    </style>
    """, unsafe_allow_html=True)

# --- CHARGEMENT DES DONNÉES GOOGLE SHEETS ---
@st.cache_data(ttl=60)
def load_remote_data():
    try:
        data = pd.read_csv(URL)
        # Nettoyage des colonnes (minuscules, pas d'espaces)
        data.columns = [str(c).strip().lower() for c in data.columns]
        
        # Renommage flexible
        rename_dict = {'categorie': 'catégorie', 'category': 'catégorie', 'thème': 'catégorie'}
        data = data.rename(columns=rename_dict)
        
        # On ne garde que les lignes qui ont au moins un titre
        data = data.dropna(subset=['titre']) if 'titre' in data.columns else data
        
        # Conversion en liste de dictionnaires propre
        return data.fillna("").to_dict('records')
    except:
        return []

# Fusion
remote_data = load_remote_data()
toutes_expressions = expressions_fixes + remote_data

# --- INTERFACE ---
st.sidebar.title("💎 Rosly Eloquence")

# Extraction sécurisée et propre des catégories pour le menu
liste_brute = [str(exp.get('catégorie', 'Général')).strip() for exp in toutes_expressions]
# On enlève les doublons et les textes vides
liste_categories = sorted(list(set([c for c in liste_brute if c and c != "nan"])))

choix = st.sidebar.selectbox("Thématique", ["Toutes"] + liste_categories)

st.title("📖 Ma Bibliothèque d'Éloquence")

# Affichage filtré
count = 0
for exp in toutes_expressions:
    cat_actuelle = str(exp.get('catégorie', 'Général')).strip()
    if choix == "Toutes" or choix == cat_actuelle:
        st.markdown(f"""
            <div class="card">
                <div class="cat-tag">{cat_actuelle}</div>
                <h3 style="margin:5px 0;">{exp.get('titre', 'Expression')}</h3>
                <p class="sens-text">🔍 {exp.get('sens', 'Définition...')}</p>
                <p class="ex-text">💡 <b>Exemple :</b> {exp.get('exemple', 'Aucun exemple disponible.')}</p>
            </div>
        """, unsafe_allow_html=True)
        count += 1

st.sidebar.write(f"📊 {count} expressions affichées")
st.sidebar.markdown("---")
st.sidebar.caption("Rosly - Pointe-Noire 🇨🇬")
