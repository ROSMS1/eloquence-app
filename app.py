import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="Rosly — Éloquence, Ingénierie & Coaching", 
    page_icon="⚖️", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ================================================================
# SYSTÈME DE STYLE (CSS)
# ================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;1,400&family=Inter:wght@300;400;500;600&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif;}
h1,h2,h3{font-family:'Playfair Display',serif;}
.main{background:#F8F7F2;}
.card{background:white;padding:22px 26px;border-radius:14px;border-left:6px solid #1E3A8A;box-shadow:0 3px 12px rgba(0,0,0,0.07);margin-bottom:18px;transition:box-shadow 0.2s;}
.card:hover{box-shadow:0 6px 20px rgba(0,0,0,0.12);}
.card-gold{border-left-color:#B8860B;}.card-green{border-left-color:#1A6B3A;}.card-red{border-left-color:#8B1A1A;}
.card-purple{border-left-color:#5B2D8E;}.card-teal{border-left-color:#0E7490;}.card-orange{border-left-color:#C05621;}
.cat-tag{font-weight:700;font-size:0.7em;text-transform:uppercase;letter-spacing:0.12em;color:#1E3A8A;margin-bottom:6px;}
.card-title{margin:6px 0 10px;font-size:1.15em;color:#1a1a2e;font-weight:bold;}
.sens-text{color:#374151;font-weight:500;margin:8px 0;line-height:1.6;}
.ex-box{background:#F3F4F6;padding:12px 16px;border-radius:8px;font-style:italic;color:#4B5563;border-left:3px solid #CBD5E1;margin-top:10px;}
.solution-box{background:#F0FDF4;padding:14px 18px;border-radius:10px;border-left:4px solid #16A34A;margin-top:10px;color:#14532D;}
.warning-box{background:linear-gradient(135deg,#FFF7ED 0%,#FFEDD5 100%);border:1px solid #FED7AA;border-radius:12px;padding:18px 22px;margin:12px 0;color:#7C2D12;}
.section-header{background:linear-gradient(135deg,#1E3A8A 0%,#1e40af 100%);color:white;padding:16px 24px;border-radius:12px;margin-bottom:24px;}
.section-header h2{color:white !important;margin:0;}
.coach-header{background:linear-gradient(135deg,#14532D 0%,#166534 100%);}
.stress-header{background:linear-gradient(135deg,#7C2D12 0%,#991B1B 100%);}
[data-testid="stSidebar"]{background:#1a1a2e;}
[data-testid="stSidebar"] *{color:#E8D5B7 !important;}
</style>
""", unsafe_allow_html=True)

# ================================================================
# BASE DE DONNÉES (ARGUMENTS AJOUTÉS)
# ================================================================

IDIOMES = [
    {"titre":"Avoir l'apanage de","sens":"Posséder un privilège exclusif ou une qualité propre à soi seul.","exemple":"La rigueur n'est pas l'apanage des mathématiciens.","niveau":"★★★☆☆"},
    {"titre":"Une victoire à la Pyrrhus","sens":"Victoire obtenue au prix de pertes si lourdes qu'elle équivaut à une défaite.","exemple":"Il a remporté l'appel d'offres, mais à quel coût humain ?","niveau":"★★★★☆"},
    {"titre":"Brûler ses vaisseaux","sens":"Prendre une décision irrévocable qui coupe tout chemin de retour.","exemple":"En lançant ce projet sans plan B, il a brûlé ses vaisseaux.","niveau":"★★★★☆"}
]

MATHS = [
    {"ss":"🎲 Probabilités","titre":"L'Inférence Bayésienne","sens":"Mettre à jour sa probabilité a priori en intégrant de nouvelles preuves.","exemple":"À la lumière de ces chiffres, ma probabilité a priori doit être réévaluée.","formule":"P(A|B) = P(B|A) × P(A) / P(B)"},
    {"ss":"⚙️ Systémique","titre":"L'Entropie","sens":"Mesure du désordre naturel d'un système. Sans entretien, tout tend vers le chaos.","exemple":"Sans communication, l'entropie de ce projet augmentera inévitablement.","formule":"ΔS ≥ 0"},
    {"ss":"♟️ Théorie des Jeux","titre":"L'Équilibre de Nash","sens":"Situation stable où aucun acteur n'a intérêt à changer seul sa stratégie.","exemple":"Nous sommes dans un équilibre de Nash : personne ne baisse les prix.","formule":"Stratégie optimale collective"}
]

SYMPTOMES = [
    {"titre":"L'Indécision Chronique","description":"L'impossibilité de choisir, engendrant une paralysie par l'analyse.","solution":"Une décision imparfaite prise aujourd'hui vaut mieux qu'une décision parfaite jamais prise.","alerte":"Plus de 3 mois de réflexion sur le même sujet."},
    {"titre":"La Gentillesse Excessive","description":"Éviter de contrarier l'autre au détriment de son propre respect.","solution":"Dire 'ma position est différente' n'est pas une agression, c'est de l'intégrité.","alerte":"Dire 'oui' quand on pense 'non'."}
]

OUTILS_COACH = [
    {"titre":"Visualisation Mentale","description":"Le cerveau ne fait pas la différence entre réalité et imagination vive.","protocole":"Créez un film mental où vous réussissez l'action redoutée.","quand":"Avant tout événement stressant."},
    {"titre":"Le Plan de 5 Minutes","description":"Vaincre l'inertie en s'engageant sur une durée infime.","protocole":"Décider de travailler uniquement 5 minutes, puis s'auto-féliciter.","quand":"Pour vaincre la procrastination."}
]

STRESS_FONDEMENTS = [
    {"titre":"Le Stress est un AMI","description":"C'est une réaction d'adaptation nécessaire à la survie (Hans Selye).","fonctions":["Stimule l'énergie","Aiguise les sens","Permet la réaction rapide"],"chiffre":"1 salarié sur 3 en UE est affecté."}
]

# ================================================================
# LOGIQUE DE L'INTERFACE (SIDEBAR)
# ================================================================

st.sidebar.title("💎 Menu Principal")
page = st.sidebar.radio("Navigation", ["Éloquence & Logique", "Coaching & Psychologie", "Gestion du Stress"])

# ================================================================
# PAGE 1 : ÉLOQUENCE & LOGIQUE
# ================================================================
if page == "Éloquence & Logique":
    st.markdown('<div class="section-header"><h2>🏛️ Rhétorique & Idiomes</h2><p>L\'art du verbe et de la précision</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    for i, item in enumerate(IDIOMES):
        target = col1 if i % 2 == 0 else col2
        with target:
            st.markdown(f"""
            <div class="card">
                <div class="cat-tag">Idiome {item['niveau']}</div>
                <div class="card-title">{item['titre']}</div>
                <div class="sens-text">{item['sens']}</div>
                <div class="ex-box">Exemple : {item['exemple']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-header"><h2>📊 Logique & Mathématiques</h2><p>Modèles mentaux pour la décision</p></div>', unsafe_allow_html=True)
    for m in MATHS:
        st.markdown(f"""
        <div class="card card-purple">
            <div class="cat-tag">{m['ss']}</div>
            <div class="card-title">{m['titre']}</div>
            <div class="sens-text">{m['sens']}</div>
            <div class="solution-box"><strong>Formule :</strong> {m['formule']}</div>
            <div class="ex-box">{m['exemple']}</div>
        </div>
        """, unsafe_allow_html=True)

# ================================================================
# PAGE 2 : COACHING
# ================================================================
elif page == "Coaching & Psychologie":
    st.markdown('<div class="section-header coach-header"><h2>🧠 Coaching & Estime de Soi</h2><p>Identifier et vaincre les blocages</p></div>', unsafe_allow_html=True)
    
    st.subheader("🚩 Symptômes de Blocage")
    for s in SYMPTOMES:
        st.markdown(f"""
        <div class="card card-red">
            <div class="card-title">{s['titre']}</div>
            <div class="sens-text">{s['description']}</div>
            <div class="solution-box"><strong>Solution :</strong> {s['solution']}</div>
            <div class="warning-box"><strong>Alerte :</strong> {s['alerte']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("🛠️ Outils Pratiques")
    for o in OUTILS_COACH:
        st.markdown(f"""
        <div class="card card-green">
            <div class="card-title">{o['titre']}</div>
            <div class="sens-text">{o['description']}</div>
            <div class="ex-box"><strong>Protocole :</strong> {o['protocole']}</div>
            <div class="cat-tag" style="margin-top:10px;">Usage : {o['quand']}</div>
        </div>
        """, unsafe_allow_html=True)

# ================================================================
# PAGE 3 : STRESS
# ================================================================
else:
    st.markdown('<div class="section-header stress-header"><h2>⚡ Gestion du Stress</h2><p>Transformer la tension en moteur</p></div>', unsafe_allow_html=True)
    
    for f in STRESS_FONDEMENTS:
        st.markdown(f"""
        <div class="card card-orange">
            <div class="card-title">{f['titre']}</div>
            <div class="sens-text">{f['description']}</div>
            <div class="ex-box">
                <strong>Pourquoi c'est utile :</strong><br>
                {'<br>'.join(f['fonctions'])}
            </div>
            <div class="warning-box">Statistique : {f['chiffre']}</div>
        </div>
        """, unsafe_allow_html=True)
