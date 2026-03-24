import streamlit as st

# Configuration de la page
st.set_page_config(page_title="L'Art de l'Éloquence", page_icon="⚖️", layout="wide")

# --- STYLE CSS PERSONNALISÉ ---
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
    .conseil-pro { background-color: #fff7ed; border: 1px dashed #ed8936; padding: 15px; border-radius: 10px; color: #9a3412; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LATÉRALE ---
st.sidebar.title("💎 Menu de Maîtrise")
menu = [
    "Expressions Idiomatiques",
    "Connecteurs Logiques",
    "Persuasion & Influence",
    "Rhétorique Juridique",
    "Philosophie & Éloquence",
    "La Métaphore Physique"
]
choix = st.sidebar.radio("Navigation", menu)

# --- FONCTIONS D'AFFICHAGE ---
def fiche(titre, sens, exemple):
    st.markdown(f"""<div class="card">
        <h3>{titre}</h3>
        <p class="sens">🔍 Sens : {sens}</p>
        <p class="exemple">💡 Exemple : {exemple}</p>
    </div>""", unsafe_allow_html=True)

# --- CONTENU ---

if choix == "Expressions Idiomatiques":
    st.title("🗣️ Expressions Idiomatiques & Vocabulaire")
    fiche("Avoir l'apanage de quelque chose", "Posséder un privilège exclusif ou une qualité propre à soi seul.", "La rigueur n'est pas l'apanage des mathématiciens.")
    fiche("Sortir de ses gonds", "Perdre son sang-froid, se mettre violemment en colère.", "Devant tant d'injustice, il a fini par sortir de ses gonds.")
    fiche("Une victoire à la Pyrrhus", "Une victoire obtenue au prix de pertes si lourdes qu'elle équivaut presque à une défaite.", "Il a gagné son procès, mais ses frais d'avocat l'ont ruiné : c'est une victoire à la Pyrrhus.")
    fiche("S'acquitter d'une tâche", "Accomplir, remplir une obligation ou un travail avec soin.", "Il s'est acquitté de sa mission avec un professionnalisme exemplaire.")
    fiche("Céder aux sirènes de quelque chose", "Se laisser séduire par une proposition attrayante mais potentiellement trompeuse ou dangereuse.", "Beaucoup de pays ont cédé aux sirènes du protectionnisme.")
    
    st.markdown("---")
    st.subheader("Vocabulaire de situation")
    st.warning("⚠️ Attention à la dégradation : *Canard boiteux, trahison, crédibilité détruite, qualité détériorée.*")
    st.info("💡 À utiliser : *Besoin de cohérence, adoucir le ton, réagir au quart de tour, ce qui est certain.*")

elif choix == "Connecteurs Logiques":
    st.title("🔗 L'Art de lier les Idées")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏁 Introduire")
        st.write("- **Tout d'abord...** / **Pour commencer...**")
        st.write("- **En premier lieu...** (Très soutenu)")
        st.write("- **À vrai dire...** (Avis personnel)")
        
        st.subheader("⏳ Gagner du temps")
        st.write("- **Il convient de préciser que...**")
        st.write("- **Soulignons également que...**")
        st.write("- **Force est de constater que...**")
    
    with col2:
        st.subheader("➕ Ajouter / Nuancer")
        st.write("- **De surcroît...** / **Par ailleurs...**")
        st.write("- **Ceci étant dit...** / **Toutefois...**")
        st.write("- **Néanmoins...** / **En revanche...**")

        st.subheader("🔚 Conclure")
        st.write("- **En définitive...** / **Somme toute...**")
        st.write("- **En résumé...**")

    st.markdown("""<div class="conseil-pro">
        <b>💡 Le Conseil "Pro" : Le silence stratégique</b><br>
        Le secret des grands orateurs est de marquer une pause silencieuse de 2 secondes au lieu de dire "euh". 
        Cela donne une impression de maîtrise et de réflexion.
    </div>""", unsafe_allow_html=True)

elif choix == "Persuasion & Influence":
    st.title("🎯 Convaincre, Négocier & Apaiser")
    
    tab1, tab2, tab3 = st.tabs(["Négocier", "Apaiser", "Vendre une Idée"])
    
    with tab1:
        st.subheader("L'assurance sans agression")
        st.write("- **Il est manifeste que...** (Évidence logique)")
        st.write("- **Porter à votre connaissance...** (Donne de l'importance)")
        st.write("- **Sous réserve de...** (Condition diplomatique)")
        st.write("- **À l'aune de...** (À la lumière de)")
        
    with tab2:
        st.subheader("Reconnaître sans céder")
        st.write("- **Je mesure pleinement votre préoccupation** (Empathie)")
        st.write("- **Mettons de côté, pour un instant...** (Recentrer)")
        st.write("- **Cherchons un terrain d'entente**")
        st.info("💡 Technique du miroir : 'Si je vous ai bien suivi, votre priorité est...'")

    with tab3:
        st.subheader("Rendre le projet inévitable")
        st.write("- **Le statu quo n'est plus une option viable.**")
        st.write("- **L'état des lieux est sans appel.**")
        st.write("- **Une solution pérenne / Approche modulaire.**")
        st.success("🧠 Argument du 'Nous' : Ne dites pas 'Mon projet', dites 'Notre vision'.")

elif choix == "Rhétorique Juridique":
    st.title("⚖️ Rhétorique & Droit")
    
    fiche("Il est constant que...", "S'utilise pour un fait que personne ne peut nier.", "Il est constant que le contrat a été signé librement.")
    fiche("En l'espèce...", "Ramener le débat aux faits précis du dossier.", "En l'espèce, aucun retard n'a été constaté.")
    fiche("Argument inopérant", "Argument qui n'a aucun impact juridique sur la solution.", "Ce point est vrai, mais il est inopérant en l'espèce.")
    fiche("À titre subsidiaire", "Proposer une alternative si l'argument principal est rejeté.", "À titre subsidiaire, nous demandons une réduction de peine.")
    
    st.markdown("---")
    st.subheader("🏛️ Adages Latins")
    st.code("Actori incumbit probatio (La preuve incombe au demandeur)")
    st.code("Fraus omnia corrumpit (La fraude corrompt tout)")
    st.code("In dubio pro reo (Le doute profite à l'accusé)")

elif choix == "Philosophie & Éloquence":
    st.title("🏛️ Fondations Philosophiques")
    st.subheader("La Triade d'Aristote")
    st.write("1. **Ethos** (Crédibilité) : Qui êtes-vous pour parler ?")
    st.write("2. **Logos** (Logique) : L'ossature de votre raisonnement.")
    st.write("3. **Pathos** (Émotion) : Faire vibrer l'auditoire.")
    
    st.markdown("---")
    st.subheader("Figures de Style")
    st.table({
        "Figure": ["Prétérition", "Anaphore", "Antithèse"],
        "Définition": ["Dire qu'on ne va pas parler d'un sujet pour mieux le souligner", "Répétition d'un mot en début de phrase", "Opposer deux termes contraires"],
        "Exemple": ["Je ne rappellerai pas son passé...", "C'est l'honneur d'un homme, c'est la vie d'une famille...", "La force des faibles."]
    })

elif choix == "La Métaphore Physique":
    st.title("⚡ Électricité & Convalescence")
    st.info("Réconcilier le corps humain avec les lois de la physique.")
    
    st.markdown("""
    ### 1. Loi d'Ohm (U = R · I)
    **Analogie :** Votre corps a une résistance (R) élevée pendant la maladie. Si vous maintenez une intensité (I) élevée, vous créez une surtension (U).
    **Argument :** "Baissons l'intensité le temps que votre résistance diminue naturellement."

    ### 2. Le Condensateur (τ = R · C)
    **Analogie :** Vos réserves sont un condensateur vidé. La charge prend un temps incompressible.
    **Argument :** "On ne demande pas à une batterie vide de démarrer un moteur instantanément."

    ### 3. Loi de Joule (P = R · I²)
    **Analogie :** L'énergie se dissipe en chaleur (inflammation) avec le carré de l'intensité.
    **Argument :** "Chaque effort prématuré dissipe l'énergie nécessaire à la reconstruction."

    ### 4. Court-Circuit & Isolation
    **Analogie :** La convalescence est la phase de 'ré-isolation' de vos circuits.
    **Argument :** "Le repos est l'isolant qui empêche le court-circuit général."
    """)

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write("👤 **Utilisateur : Rosly**")
st.sidebar.caption("République du Congo | Télécom & Éloquence")
