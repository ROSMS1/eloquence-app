import streamlit as st

# Configuration de la page pour un look pro
st.set_page_config(page_title="L'Art de l'Éloquence", page_icon="⚖️", layout="wide")

# --- STYLE CSS POUR LES FICHES ---
st.markdown("""
    <style>
    .card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1E3A8A;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }
    .sens { color: #1E3A8A; font-weight: bold; }
    .exemple { color: #4B5563; font-style: italic; border-top: 1px solid #eee; margin-top: 10px; padding-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
st.sidebar.title("📚 Ma Bibliothèque")
menu = [
    "Expressions Idiomatiques", 
    "Connecteurs & Transitions", 
    "Convaincre & Négocier", 
    "Rhétorique Juridique", 
    "La Métaphore Physique",
    "➕ Ajouter une Note"
]
choix = st.sidebar.radio("Navigation", menu)

# --- FONCTION POUR AFFICHER UNE FICHE ---
def afficher_fiche(titre, sens, exemple):
    st.markdown(f"""
        <div class="card">
            <h3>{titre}</h3>
            <p class="sens">🔍 Sens : {sens}</p>
            <p class="exemple">💡 Exemple : {exemple}</p>
        </div>
    """, unsafe_allow_html=True)

# --- CONTENU DES CATÉGORIES ---

if choix == "Expressions Idiomatiques":
    st.title("🗣️ Expressions Idiomatiques")
    afficher_fiche("Avoir l'apanage de quelque chose", "Posséder un privilège exclusif ou une qualité propre à soi seul.", "La rigueur n'est pas l'apanage des mathématiciens.")
    afficher_fiche("Sortir de ses gonds", "Perdre son sang-froid, se mettre violemment en colère.", "Devant tant d'injustice, il a fini par sortir de ses gonds.")
    afficher_fiche("Une victoire à la Pyrrhus", "Une victoire obtenue au prix de pertes si lourdes qu'elle équivaut presque à une défaite.", "Il a gagné son procès, mais ses frais d'avocat l'ont ruiné.")
    afficher_fiche("S'acquitter d'une tâche", "Accomplir, remplir une obligation ou un travail avec soin.", "Il s'est acquitté de sa mission avec un professionnalisme exemplaire.")

elif choix == "Connecteurs & Transitions":
    st.title("🔗 L'Art de la Transition")
    st.info("Utilisez ces connecteurs pour remplacer les 'euh...' et structurer votre pensée.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Introduire / Débuter")
        st.write("- **Tout d'abord...**")
        st.write("- **En premier lieu...** (Soutenu)")
        st.write("- **À vrai dire...** (Avis personnel)")
    with col2:
        st.subheader("Gagner du temps")
        st.write("- **Il convient de préciser que...**")
        st.write("- **Force est de constater que...**")
        st.write("- **Autrement dit...** (Reformulation)")

elif choix == "Convaincre & Négocier":
    st.title("🎯 Influence & Négociation")
    afficher_fiche("L'Argument de la Nécessité", "Valider le problème avant de proposer la solution pour créer l'urgence.", "L'état des lieux est sans appel : le statu quo n'est plus une option viable.")
    afficher_fiche("Le 'Nous' Stratégique", "Inclure l'autre dans la paternité de l'idée pour réduire la résistance.", "Dans l'intérêt de notre département, voici notre défi commun.")
    st.success("💡 **Le conseil pro :** Le silence de 2 secondes donne une impression de maîtrise totale.")

elif choix == "Rhétorique Juridique":
    st.title("⚖️ Rhétorique Juridique")
    afficher_fiche("En l'espèce", "Expression reine pour ramener le débat aux faits précis du dossier.", "En l'espèce, la preuve du manquement n'est pas rapportée.")
    afficher_fiche("Fraus omnia corrumpit", "La fraude corrompt tout. Puissant pour dénoncer la mauvaise foi.", "La signature a été obtenue par tromperie : fraus omnia corrumpit.")
    afficher_fiche("Argument A Fortiori", "À plus forte raison. Si la règle s'applique à un cas simple, elle s'applique mieux au vôtre.", "Si l'accès est interdit aux vélos, il l'est a fortiori aux voitures.")

elif choix == "La Métaphore Physique":
    st.title("⚡ Physique & Convalescence")
    st.warning("Utilisez les lois de l'électricité pour expliquer la guérison.")
    afficher_fiche("Loi d'Ohm (U=R·I)", "Gérer la résistance. Si la résistance (fatigue) est haute, baissez l'intensité.", "Pour ne pas griller vos circuits, baissons l'intensité le temps que la résistance diminue.")
    afficher_fiche("L'Effet Joule", "Éviter la surchauffe. Forcer trop tôt dissipe l'énergie en dégâts (inflammation).", "Restons en basse consommation pour éviter la surchauffe inflammatoire.")

elif choix == "➕ Ajouter une Note":
    st.title("📝 Ajouter une nouvelle expression")
    st.write("Pour l'instant, ajoutez vos notes ici pour les copier plus tard dans votre fichier GitHub.")
    titre_nouveau = st.text_input("Titre de l'expression")
    sens_nouveau = st.text_area("Sens / Définition")
    ex_nouveau = st.text_area("Exemple d'utilisation")
    
    if st.button("Générer le code pour GitHub"):
        st.code(f'afficher_fiche("{titre_nouveau}", "{sens_nouveau}", "{ex_nouveau}")')
        st.info("Copiez cette ligne et collez-la dans votre fichier app.py sur GitHub pour la sauvegarder définitivement.")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.caption("Rosly - Expertise & Éloquence")
