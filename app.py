import streamlit as st
import pandas as pd

# --- CONFIGURATION ---
SHEET_ID = "1RWQSre19ZmQl4rzxNcsIwvWlJuu_Nm9RMBKbBwPuYyE"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

st.set_page_config(page_title="Rosly - L'Art de l'Éloquence", page_icon="⚖️", layout="wide")

# --- BASE DE DONNÉES INITIALE (Expressions pré-chargées) ---
expressions_fixes = [
    # 1. Expressions Idiomatiques
    {"catégorie": "Idiomatique", "titre": "Avoir l'apanage de", "sens": "Posséder un privilège exclusif ou une qualité propre à soi seul.", "exemple": "La rigueur n'est pas l'apanage des mathématiciens."},
    {"catégorie": "Idiomatique", "titre": "Sortir de ses gonds", "sens": "Perdre son sang-froid, se mettre violemment en colère.", "exemple": "Devant tant d'injustice, il a fini par sortir de ses gonds."},
    {"catégorie": "Idiomatique", "titre": "Une victoire à la Pyrrhus", "sens": "Une victoire obtenue au prix de pertes si lourdes qu'elle équivaut à une défaite.", "exemple": "Il a gagné son procès, mais ses frais d'avocat l'ont ruiné : c'est une victoire à la Pyrrhus."},
    {"catégorie": "Idiomatique", "titre": "S'acquitter d'une tâche", "sens": "Accomplir, remplir une obligation ou un travail avec soin.", "exemple": "Il s'est acquitté de sa mission avec un professionnalisme exemplaire."},
    {"catégorie": "Idiomatique", "titre": "Céder aux sirènes de...", "sens": "Se laisser séduire par une proposition attrayante mais potentiellement trompeuse.", "exemple": "Beaucoup ont cédé aux sirènes du profit facile."},
    {"catégorie": "Idiomatique", "titre": "Canard boiteux", "sens": "Désigne un élément défaillant ou inadapté au sein d'un groupe.", "exemple": "Sans maintenance, ce site deviendra le canard boiteux du réseau."},
    {"catégorie": "Idiomatique", "titre": "Réagir au quart de tour", "sens": "Réagir très rapidement à une sollicitation ou un événement.", "exemple": "Face à une panne secteur, l'équipe doit réagir au quart de tour."},

    # 2. Structure & Connecteurs (L'Art de la Transition)
    {"catégorie": "Structure", "titre": "En premier lieu / Tout d'abord", "sens": "Pour introduire une idée ou commencer son propos.", "exemple": "Tout d'abord, analysons l'état des redresseurs."},
    {"catégorie": "Structure", "titre": "Force est de constater / de reconnaître", "sens": "Pour imposer un fait qui semble s'imposer d'eux-mêmes.", "exemple": "Force est de constater que la qualité s'est détériorée."},
    {"catégorie": "Structure", "titre": "De surcroît / Par ailleurs", "sens": "Pour ajouter une information de manière fluide et formelle.", "exemple": "L'économie va ralentir ; de surcroît, l'inflation augmente."},
    {"catégorie": "Structure", "titre": "Ceci étant dit / Toutefois", "sens": "Pour marquer une opposition ou une nuance avec élégance.", "exemple": "Le projet est validé. Ceci étant dit, restons prudents sur les délais."},
    {"catégorie": "Structure", "titre": "En définitive / Somme toute", "sens": "Pour conclure ou synthétiser une démonstration.", "exemple": "En définitive, cette solution est la plus pérenne."},

    # 3. Convaincre & Négocier (Le Plaidoyer)
    {"catégorie": "Persuasion", "titre": "Un levier déterminant", "sens": "Un élément clé qui permet de faire basculer une situation.", "exemple": "La formation est un levier déterminant pour la réussite du projet."},
    {"catégorie": "Persuasion", "titre": "Nonobstant", "sens": "Signifie 'malgré' ou 'bien que'. Très soutenu.", "exemple": "Nous avançons, nonobstant les difficultés logistiques."},
    {"catégorie": "Persuasion", "titre": "Sous réserve de...", "sens": "Poser une condition de manière diplomatique.", "exemple": "Nous acceptons, sous réserve d'un audit technique préalable."},
    {"catégorie": "Persuasion", "titre": "À l'aune de...", "sens": "En considération de / À la lumière de.", "exemple": "Il faut juger ce résultat à l'aune des efforts fournis."},
    {"catégorie": "Persuasion", "titre": "Le statu quo n'est plus une option", "sens": "Indique que l'immobilisme est devenu dangereux.", "exemple": "Face à la concurrence, le statu quo n'est plus une option viable."},

    # 4. Rhétorique Juridique
    {"catégorie": "Juridique", "titre": "En l'espèce", "sens": "Dans le cas présent (pour ramener le débat aux faits).", "exemple": "En l'espèce, aucune faute n'a été commise par le technicien."},
    {"catégorie": "Juridique", "titre": "Il est constant que...", "sens": "Pour présenter un fait comme indiscutable et reconnu par tous.", "exemple": "Il est constant que le contrat n'a pas été respecté."},
    {"catégorie": "Juridique", "titre": "Un faisceau d'indices concordants", "sens": "Accumulation de preuves qui mènent à une conclusion unique.", "exemple": "C'est un faisceau d'indices concordants qui prouve la trahison."},
    {"catégorie": "Juridique", "titre": "Actori incumbit probatio", "sens": "La preuve incombe à celui qui affirme (Adage latin).", "exemple": "Il nous accuse ? Actori incumbit probatio : qu'il montre ses preuves."},

    # 5. Physique & Convalescence (Métaphores)
    {"catégorie": "Physique", "titre": "Loi d'Ohm (U=RI)", "sens": "Gérer la résistance interne lors de la guérison.", "exemple": "Votre résistance est haute : baissons l'intensité pour ne pas griller vos circuits."},
    {"catégorie": "Physique", "titre": "Analogie du Condensateur", "sens": "Temps nécessaire pour recharger ses batteries d'énergie.", "exemple": "Le repos est le temps de charge nécessaire pour votre condensateur interne."},
    {"catégorie": "Physique", "titre": "Effet de Résonance", "sens": "Retrouver son propre rythme biologique.", "exemple": "La guérison est une synchronisation avec votre fréquence propre."}
]

# --- STYLE VISUEL ---
st.markdown("""
    <style>
    .card { background: white; padding: 20px; border-radius: 15px; border-left: 6px solid #1E3A8A; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom: 15px; }
    .cat-tag { color: #1E3A8A; font-weight: bold; font-size: 0.8em; text-transform: uppercase; }
    .sens-text { color: #2D3748; font-weight: 600; margin: 10px 0; }
    .ex-text { background: #F3F4F6; padding: 12px; border-radius: 8px; font-style: italic; color: #4B5563; border-left: 3px solid #cbd5e1; }
    </style>
    """, unsafe_allow_html=True)

# --- CHARGEMENT DES DONNÉES GOOGLE SHEETS ---
@st.cache_data(ttl=60)
def load_remote_data():
    try:
        data = pd.read_csv(URL)
        data.columns = [str(c).strip().lower() for c in data.columns]
        rename_dict = {'categorie': 'catégorie', 'category': 'catégorie', 'thème': 'catégorie'}
        data = data.rename(columns=rename_dict)
        return data.fillna("").to_dict('records')
    except:
        return []

# Fusion des données fixes et des données distantes
remote_data = load_remote_data()
toutes_expressions = expressions_fixes + remote_data

# --- INTERFACE ---
st.sidebar.title("💎 Rosly Eloquence")
st.sidebar.markdown("---")

# Extraction des catégories uniques
liste_brute = [str(exp.get('catégorie', 'Général')).strip() for exp in toutes_expressions]
liste_categories = sorted(list(set([c for c in liste_brute if c and c != "nan"])))

choix = st.sidebar.selectbox("Filtrer par Thématique", ["Toutes"] + liste_categories)

st.title("📖 Ma Bibliothèque d'Éloquence")
st.caption(f"📍 Basé à Pointe-Noire — {len(toutes_expressions)} expressions enregistrées")

# Affichage filtré
for exp in toutes_expressions:
    cat_actuelle = str(exp.get('catégorie', 'Général')).strip()
    if choix == "Toutes" or choix == cat_actuelle:
        st.markdown(f"""
            <div class="card">
                <div class="cat-tag">{cat_actuelle}</div>
                <h3 style="margin:5px 0;">{exp.get('titre', 'Expression')}</h3>
                <p class="sens-text">🔍 {exp.get('sens', 'Définition non renseignée')}</p>
                <p class="ex-text">💡 <b>Exemple :</b> {exp.get('exemple', 'Aucun exemple disponible.')}</p>
            </div>
        """, unsafe_allow_html=True)

# --- CONSEIL DANS LA SIDEBAR ---
st.sidebar.markdown("---")
st.sidebar.subheader("💡 Le conseil du Pro")
st.sidebar.write("**Le silence stratégique :** Un silence de 2 secondes donne une impression de maîtrise. C'est toujours plus élégant qu'un 'euh' sonore.")
