import streamlit as st
import pandas as pd

# ============================================================
# CONFIGURATION GÉNÉRALE
# ============================================================
SHEET_ID = "1RWQSre19ZmQl4rzxNcsIwvWlJuu_Nm9RMBKbBwPuYyE"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

st.set_page_config(
    page_title="Rosly — L'Art de l'Éloquence",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# STYLE VISUEL GLOBAL
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;1,400&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

h1, h2, h3 { font-family: 'Playfair Display', serif; }

.main { background: #F8F7F2; }

/* ---- CARTES GÉNÉRIQUES ---- */
.card {
    background: white;
    padding: 22px 26px;
    border-radius: 14px;
    border-left: 6px solid #1E3A8A;
    box-shadow: 0 3px 12px rgba(0,0,0,0.07);
    margin-bottom: 18px;
    transition: box-shadow 0.2s;
}
.card:hover { box-shadow: 0 6px 20px rgba(0,0,0,0.12); }

.card-gold  { border-left-color: #B8860B; }
.card-green { border-left-color: #1A6B3A; }
.card-red   { border-left-color: #8B1A1A; }
.card-purple{ border-left-color: #5B2D8E; }
.card-teal  { border-left-color: #0E7490; }
.card-orange{ border-left-color: #C05621; }

.cat-tag {
    font-weight: 700;
    font-size: 0.7em;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #1E3A8A;
    margin-bottom: 6px;
}
.cat-tag-gold   { color: #B8860B; }
.cat-tag-green  { color: #1A6B3A; }
.cat-tag-red    { color: #8B1A1A; }
.cat-tag-purple { color: #5B2D8E; }
.cat-tag-teal   { color: #0E7490; }
.cat-tag-orange { color: #C05621; }

.card-title { margin: 6px 0 10px; font-size: 1.15em; color: #1a1a2e; }
.sens-text  { color: #374151; font-weight: 500; margin: 8px 0; line-height: 1.6; }
.ex-box     { background: #F3F4F6; padding: 12px 16px; border-radius: 8px;
               font-style: italic; color: #4B5563; border-left: 3px solid #CBD5E1;
               margin-top: 10px; line-height: 1.6; }

/* ---- CARTES SPÉCIALES ---- */
.discourse-card {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    color: #E8D5B7;
    padding: 30px 36px;
    border-radius: 16px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
    margin-bottom: 20px;
    border: 1px solid #B8860B;
}
.discourse-card h3 { color: #F5DEB3; }
.discourse-body { line-height: 1.9; font-size: 1.02em; color: #EDE0C8; }
.discourse-annotation {
    background: rgba(184,134,11,0.15);
    border: 1px solid rgba(184,134,11,0.3);
    padding: 8px 14px;
    border-radius: 6px;
    font-size: 0.85em;
    color: #D4A84B;
    display: inline-block;
    margin: 2px 4px;
    font-weight: 600;
}

.book-card {
    background: white;
    padding: 22px 26px;
    border-radius: 14px;
    border-top: 5px solid #B8860B;
    box-shadow: 0 3px 12px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}

.tip-box {
    background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
    border: 1px solid #BFDBFE;
    border-radius: 12px;
    padding: 18px 22px;
    margin: 12px 0;
    color: #1E40AF;
}

.warning-box {
    background: linear-gradient(135deg, #FFF7ED 0%, #FFEDD5 100%);
    border: 1px solid #FED7AA;
    border-radius: 12px;
    padding: 18px 22px;
    margin: 12px 0;
    color: #7C2D12;
}

.section-header {
    background: linear-gradient(135deg, #1E3A8A 0%, #1e40af 100%);
    color: white;
    padding: 16px 24px;
    border-radius: 12px;
    margin-bottom: 24px;
    margin-top: 10px;
}
.section-header h2 { color: white; margin: 0; font-size: 1.4em; }
.section-header p  { color: #BFDBFE; margin: 6px 0 0; font-size: 0.9em; }

.progress-badge {
    background: #1E3A8A;
    color: white;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.78em;
    font-weight: 600;
}

/* ---- SIDEBAR ---- */
[data-testid="stSidebar"] { background: #1a1a2e; }
[data-testid="stSidebar"] * { color: #E8D5B7 !important; }
[data-testid="stSidebar"] .stSelectbox label { color: #B8B8D0 !important; }
</style>
""", unsafe_allow_html=True)


# ============================================================
# ======  BASE DE DONNÉES COMPLÈTE PAR SECTION  ==============
# ============================================================

# ---- SECTION 1 : EXPRESSIONS IDIOMATIQUES ------------------
expressions_idiomatiques = [
    {
        "titre": "Avoir l'apanage de",
        "sens": "Posséder un privilège exclusif ou une qualité propre à soi seul.",
        "exemple": "La rigueur n'est pas l'apanage des mathématiciens : elle est la marque de tout esprit d'élite.",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "Sortir de ses gonds",
        "sens": "Perdre son sang-froid et se mettre violemment en colère. Un leader efficace ne sort jamais de ses gonds.",
        "exemple": "Devant tant d'injustice manifeste, il a fini par sortir de ses gonds lors du conseil.",
        "niveau": "★★☆☆☆"
    },
    {
        "titre": "Une victoire à la Pyrrhus",
        "sens": "Une victoire obtenue au prix de pertes si lourdes qu'elle équivaut à une défaite. Référence au roi Pyrrhus d'Épire.",
        "exemple": "Il a remporté l'appel d'offres, mais à quel coût humain ? C'est une victoire à la Pyrrhus.",
        "niveau": "★★★★☆"
    },
    {
        "titre": "S'acquitter d'une tâche",
        "sens": "Accomplir et remplir une obligation ou un travail avec soin et diligence.",
        "exemple": "Il s'est acquitté de sa mission avec un professionnalisme exemplaire, nonobstant les contraintes.",
        "niveau": "★★☆☆☆"
    },
    {
        "titre": "Céder aux sirènes de...",
        "sens": "Se laisser séduire par une proposition attrayante mais potentiellement trompeuse ou dangereuse.",
        "exemple": "Beaucoup d'organisations ont cédé aux sirènes du profit facile, sacrifiant leur durabilité.",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "Canard boiteux",
        "sens": "Désigne un élément défaillant, inadapté ou en difficulté au sein d'un groupe ou d'un système.",
        "exemple": "Sans maintenance préventive, ce nœud réseau deviendra le canard boiteux de l'infrastructure.",
        "niveau": "★★☆☆☆"
    },
    {
        "titre": "Réagir au quart de tour",
        "sens": "Réagir avec une rapidité et une efficacité absolues à une sollicitation ou un événement imprévu.",
        "exemple": "Face à une panne secteur, l'équipe NOC doit être formée à réagir au quart de tour.",
        "niveau": "★★☆☆☆"
    },
    {
        "titre": "Tenir la dragée haute",
        "sens": "Résister à quelqu'un, ne pas lui céder facilement ; lui imposer des conditions exigeantes.",
        "exemple": "Lors de la négociation contractuelle, notre équipe a tenu la dragée haute aux fournisseurs.",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "Ménager la chèvre et le chou",
        "sens": "Chercher à satisfaire deux parties opposées sans prendre parti, au risque de ne satisfaire personne.",
        "exemple": "Un manager qui ménage constamment la chèvre et le chou finit par perdre toute crédibilité.",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "Brûler ses vaisseaux",
        "sens": "Prendre une décision irrévocable qui coupe tout chemin de retour. Référence à Hernán Cortés.",
        "exemple": "En lançant ce projet sans plan B, il a délibérément brûlé ses vaisseaux pour forcer l'engagement total.",
        "niveau": "★★★★☆"
    },
]

# ---- SECTION 2 : STRUCTURE & CONNECTEURS -------------------
expressions_structure = [
    {
        "titre": "En premier lieu / Tout d'abord",
        "sens": "Pour introduire une première idée de façon claire. Lance la progression logique de l'argumentaire.",
        "exemple": "Tout d'abord, procédons à l'analyse de l'état des équipements actifs sur le site.",
        "usage": "Introduction",
        "niveau": "★☆☆☆☆"
    },
    {
        "titre": "Force est de constater / de reconnaître",
        "sens": "Formule pour imposer un fait qui s'impose objectivement, sans que l'on puisse le nier.",
        "exemple": "Force est de constater que la qualité de service s'est détériorée depuis la dernière mise à jour firmware.",
        "usage": "Constat",
        "niveau": "★★☆☆☆"
    },
    {
        "titre": "De surcroît / Par ailleurs",
        "sens": "Pour ajouter une information complémentaire de manière fluide et formelle, sans rupture de rythme.",
        "exemple": "L'économie va ralentir ; de surcroît, les taux d'intérêt augmentent, réduisant notre marge de manœuvre.",
        "usage": "Ajout",
        "niveau": "★★☆☆☆"
    },
    {
        "titre": "Ceci étant dit / Toutefois",
        "sens": "Pour marquer une opposition, une nuance ou une réserve avec élégance. Transition dialectique majeure.",
        "exemple": "Le projet est validé par la direction. Ceci étant dit, il convient de rester prudents sur les délais d'exécution.",
        "usage": "Opposition",
        "niveau": "★★☆☆☆"
    },
    {
        "titre": "En définitive / Somme toute",
        "sens": "Pour conclure ou synthétiser une démonstration en ramenant à l'essentiel.",
        "exemple": "En définitive, la solution redondante est la plus pérenne et la plus économiquement rationnelle.",
        "usage": "Conclusion",
        "niveau": "★★☆☆☆"
    },
    {
        "titre": "Il convient toutefois de distinguer...",
        "sens": "Pour introduire une nuance importante qui empêche une généralisation hâtive. Marque la rigueur intellectuelle.",
        "exemple": "Il convient toutefois de distinguer la panne matérielle de la défaillance logicielle dans ce diagnostic.",
        "usage": "Nuance",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "Il en résulte mécaniquement que...",
        "sens": "Pour exprimer une conséquence logique et inéluctable. Donne une impression de loi naturelle.",
        "exemple": "La batterie de secours n'a pas été testée depuis 18 mois ; il en résulte mécaniquement que son autonomie est incertaine.",
        "usage": "Causalité",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "Ceci est le corollaire direct de...",
        "sens": "Désigne une conséquence qui découle naturellement et directement d'un premier fait établi.",
        "exemple": "La surcharge du lien microonde est le corollaire direct de l'absence de politique QoS sur ce segment.",
        "usage": "Causalité",
        "niveau": "★★★★☆"
    },
    {
        "titre": "Au demeurant / En dernière analyse",
        "sens": "Pour synthétiser avec hauteur de vue. 'Au demeurant' = d'ailleurs, pour le reste. Connote la sagesse.",
        "exemple": "Au demeurant, toutes les options présentent des risques ; en dernière analyse, c'est la robustesse qui prime.",
        "usage": "Synthèse",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "À l'aune de...",
        "sens": "En considération de / À la mesure de / À la lumière de. Donne une référence d'évaluation précise.",
        "exemple": "Il faut juger ce résultat à l'aune des contraintes budgétaires et humaines auxquelles l'équipe a fait face.",
        "usage": "Évaluation",
        "niveau": "★★★★☆"
    },
]

# ---- SECTION 3 : PERSUASION & NÉGOCIATION -----------------
expressions_persuasion = [
    {
        "titre": "Un levier déterminant",
        "sens": "Un facteur clé qui permet de faire basculer une situation, une décision ou un résultat de manière significative.",
        "exemple": "La formation continue des techniciens est un levier déterminant pour la réduction des MTTR sur le terrain.",
        "niveau": "★★☆☆☆"
    },
    {
        "titre": "Nonobstant",
        "sens": "Signifie 'malgré' ou 'en dépit de'. Très soutenu. Marque que l'on avance malgré un obstacle.",
        "exemple": "Nous maintenons notre engagement contractuel, nonobstant les difficultés logistiques rencontrées en décembre.",
        "niveau": "★★★★☆"
    },
    {
        "titre": "Sous réserve de...",
        "sens": "Poser une condition de manière diplomatique et professionnelle. Protège sans agresser.",
        "exemple": "Nous approuvons le démarrage des travaux, sous réserve de validation formelle du plan de sécurité.",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "Le statu quo n'est plus une option",
        "sens": "Formule d'urgence stratégique. Indique que l'immobilisme est désormais aussi dangereux que l'action.",
        "exemple": "Face à la dégradation continue des KPIs, le statu quo n'est plus une option viable pour notre département.",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "Je rejoins votre analyse sur le point X, toutefois...",
        "sens": "Concéder partiellement pour mieux imposer sa nuance. Technique de concession stratégique.",
        "exemple": "Je rejoins votre analyse sur l'urgence de la situation, toutefois la méthode proposée mérite d'être affinée.",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "Certes..., mais...",
        "sens": "Structure de la concession rhétorique : on accorde un point pour mieux imposer le sien. Très élégant.",
        "exemple": "Certes, cet investissement est conséquent, mais le coût d'une défaillance majeure serait exponentiellement plus élevé.",
        "niveau": "★★☆☆☆"
    },
    {
        "titre": "Ouvrons un débat à ce sujet",
        "sens": "Proposer une discussion structurée pour désamorcer un blocage ou une opposition. Marque l'ouverture.",
        "exemple": "Plutôt que de trancher unilatéralement, je propose que nous ouvrions un débat technique sur ce choix d'architecture.",
        "niveau": "★★☆☆☆"
    },
    {
        "titre": "En l'absence de position contraire documentée...",
        "sens": "Imposer son point de vue en l'absence d'une objection formelle et écrite de l'interlocuteur.",
        "exemple": "En l'absence de position contraire documentée avant vendredi, nous procéderons selon notre plan initial.",
        "niveau": "★★★★☆"
    },
]

# ---- SECTION 4 : RHÉTORIQUE JURIDIQUE ----------------------
expressions_juridiques = [
    {
        "titre": "En l'espèce",
        "sens": "Dans le cas présent, dans cette situation précise. Ramène le débat général aux faits concrets du dossier.",
        "exemple": "En l'espèce, aucune faute technique n'a été commise par le technicien de maintenance sur ce site.",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "Il est constant que...",
        "sens": "Pour présenter un fait comme indiscutable, reconnu de tous et qui ne souffre aucune contestation.",
        "exemple": "Il est constant que le protocole d'intervention n'a pas été respecté lors de cette maintenance corrective.",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "Un faisceau d'indices concordants",
        "sens": "Accumulation de preuves différentes qui, prises ensemble, mènent toutes vers une même conclusion.",
        "exemple": "C'est un faisceau d'indices concordants — logs, alarmes, rapports terrain — qui pointe vers un défaut du module RF.",
        "niveau": "★★★★☆"
    },
    {
        "titre": "Actori incumbit probatio",
        "sens": "Adage latin : la preuve incombe à celui qui affirme. C'est à l'accusateur de prouver, non à l'accusé.",
        "exemple": "Il nous accuse de mauvaise foi ? Actori incumbit probatio : qu'il produise les éléments de preuve correspondants.",
        "niveau": "★★★★★"
    },
    {
        "titre": "Sans préjudice de...",
        "sens": "Sans porter atteinte à / sans remettre en cause. Permet d'agir sur un point sans affecter un autre.",
        "exemple": "Cette décision est prise sans préjudice des droits de recours dont dispose chaque partie.",
        "niveau": "★★★★☆"
    },
    {
        "titre": "À titre conservatoire",
        "sens": "Mesure prise provisoirement pour préserver une situation en attendant une décision définitive.",
        "exemple": "Nous coupons ce lien à titre conservatoire, le temps que l'audit de sécurité soit finalisé.",
        "niveau": "★★★★☆"
    },
    {
        "titre": "De jure vs de facto",
        "sens": "De jure = en droit, selon les règles formelles. De facto = en fait, dans la réalité concrète.",
        "exemple": "De jure, le contrat stipule 4h d'intervention ; de facto, nos équipes atteignent 6h sur ce type de panne.",
        "niveau": "★★★☆☆"
    },
]

# ---- SECTION 5 : ARSENAL MATHÉMATIQUE ---------------------
expressions_mathematiques = [
    # Probabilités
    {
        "sous_section": "🎲 Probabilités & Incertitude",
        "titre": "L'Espérance Mathématique (E)",
        "sens": "Valeur moyenne attendue d'une décision en pondérant chaque résultat par sa probabilité. Transforme un pari en calcul rationnel.",
        "exemple": "Si l'on considère l'espérance mathématique de ce projet de modernisation, le gain potentiel justifie largement le risque d'échec estimé.",
        "formule": "E(X) = Σ [probabilité × valeur]",
        "niveau": "★★★☆☆"
    },
    {
        "sous_section": "🎲 Probabilités & Incertitude",
        "titre": "L'Inférence Bayésienne",
        "sens": "Mettre à jour sa probabilité a priori (ce que l'on croyait) en intégrant de nouvelles preuves pour obtenir une probabilité a posteriori.",
        "exemple": "À la lumière de ces nouveaux chiffres de trafic, ma probabilité a priori sur la viabilité de ce nœud doit être réévaluée.",
        "formule": "P(A|B) = P(B|A) × P(A) / P(B)",
        "niveau": "★★★★☆"
    },
    {
        "sous_section": "🎲 Probabilités & Incertitude",
        "titre": "L'Intervalle de Confiance",
        "sens": "Fourchette dans laquelle se situe un paramètre avec un niveau de certitude donné (95%, 99%). Nuance toute affirmation.",
        "exemple": "Nous ne sommes pas dans la certitude absolue, mais nos projections se situent dans un intervalle de confiance à 95 %.",
        "formule": "μ ± 1.96 × (σ/√n) pour 95%",
        "niveau": "★★★☆☆"
    },
    # Statistiques
    {
        "sous_section": "📊 Statistiques & Rigueur",
        "titre": "La Signification Statistique (p-value)",
        "sens": "Probabilité que le résultat observé soit dû au hasard. Si p < 0.05, le résultat est 'statistiquement significatif'.",
        "exemple": "Cet écart de performance entre les deux équipes n'est pas une anomalie, il est statistiquement significatif avec p < 0.01.",
        "formule": "Si p-value < 0.05 → résultat significatif",
        "niveau": "★★★★☆"
    },
    {
        "sous_section": "📊 Statistiques & Rigueur",
        "titre": "Corrélation ≠ Causalité",
        "sens": "L'argument ultime contre les conclusions hâtives. Deux phénomènes peuvent évoluer ensemble sans que l'un cause l'autre.",
        "exemple": "Il existe une corrélation entre ce pic de trafic et les pannes, mais cela n'implique en aucun cas un lien de causalité direct.",
        "formule": "Corrélation → r ; Causalité → nécessite une expérimentation contrôlée",
        "niveau": "★★★☆☆"
    },
    {
        "sous_section": "📊 Statistiques & Rigueur",
        "titre": "La Régression vers la Moyenne",
        "sens": "Après un résultat exceptionnel (très haut ou très bas), le suivant tend naturellement vers la moyenne. Loi fondamentale souvent ignorée.",
        "exemple": "Ce pic de performance est exceptionnel ; nous devons anticiper une régression naturelle vers la moyenne au prochain trimestre.",
        "formule": "x̄_n+1 ≈ μ lorsque n → ∞",
        "niveau": "★★★★☆"
    },
    # Logique
    {
        "sous_section": "🔬 Logique & Analyse",
        "titre": "Condition Nécessaire mais non Suffisante",
        "sens": "Limiter la portée d'un argument adverse. Quelque chose peut être indispensable sans garantir le résultat à lui seul.",
        "exemple": "Avoir un bon réseau est une condition nécessaire, mais elle n'est pas suffisante pour garantir la satisfaction client.",
        "formule": "A → B (A nécessaire pour B) ≠ A ↔ B (A suffisant pour B)",
        "niveau": "★★★☆☆"
    },
    {
        "sous_section": "🔬 Logique & Analyse",
        "titre": "Le Raisonnement par l'Absurde",
        "sens": "Démontrer qu'une idée est fausse en montrant qu'elle conduit à une conclusion impossible ou contradictoire.",
        "exemple": "Si nous suivions cette logique jusqu'au bout, nous arriverions à admettre qu'il vaut mieux ne pas intervenir du tout.",
        "formule": "Si (hypothèse P) → contradiction, alors P est fausse",
        "niveau": "★★★☆☆"
    },
    {
        "sous_section": "🔬 Logique & Analyse",
        "titre": "L'Analyse de Sensibilité",
        "sens": "Tester la robustesse d'un plan ou d'un modèle en faisant varier ses paramètres clés. Révèle les vraies fragilités.",
        "exemple": "Faisons une analyse de sensibilité : si notre variable principale change de 10 %, notre business case tient-il toujours ?",
        "formule": "ΔSortie / ΔEntrée = coefficient de sensibilité",
        "niveau": "★★★★☆"
    },
    # Thermodynamique & Systémique
    {
        "sous_section": "⚙️ Systémique & Thermodynamique",
        "titre": "L'Entropie",
        "sens": "Mesure du désordre naturel d'un système. Sans énergie d'entretien, tout système tend vers le chaos. Métaphore organisationnelle puissante.",
        "exemple": "Sans communication claire et management actif, l'entropie de ce projet augmentera jusqu'à rendre toute action collective inefficace.",
        "formule": "ΔS ≥ 0 (2ᵉ loi de thermodynamique)",
        "niveau": "★★★★☆"
    },
    {
        "sous_section": "⚙️ Systémique & Thermodynamique",
        "titre": "L'Homéostasie",
        "sens": "Capacité d'un système à maintenir son équilibre interne malgré les perturbations extérieures. Résilience structurelle.",
        "exemple": "Le marché est en crise, mais notre organisation possède une homéostasie interne qui nous permet d'absorber ces chocs.",
        "formule": "Système stable : perturbation → rétroaction → équilibre restauré",
        "niveau": "★★★★☆"
    },
    {
        "sous_section": "⚙️ Systémique & Thermodynamique",
        "titre": "Le Point de Bascule (Tipping Point)",
        "sens": "Moment où un petit changement supplémentaire entraîne une transformation radicale et souvent irréversible du système.",
        "exemple": "Nous approchons du point de bascule : une seule défaillance supplémentaire pourrait provoquer l'effondrement en cascade.",
        "formule": "Bifurcation : au-delà du seuil critique → changement d'état irréversible",
        "niveau": "★★★☆☆"
    },
    # Théorie des jeux
    {
        "sous_section": "♟️ Théorie des Jeux",
        "titre": "L'Équilibre de Nash",
        "sens": "Situation stable où aucun acteur n'a intérêt à changer unilatéralement sa stratégie, même si l'équilibre n'est pas optimal.",
        "exemple": "Nos concurrents et nous sommes dans un équilibre de Nash : personne ne baisse les prix car cela déclencherait une guerre perdante.",
        "formule": "∀i : stratégie_i est optimale étant donné les stratégies des autres",
        "niveau": "★★★★★"
    },
    {
        "sous_section": "♟️ Théorie des Jeux",
        "titre": "Le Jeu à Somme Nulle",
        "sens": "Vision dans laquelle le gain de l'un est exactement la perte de l'autre. Vision limitante qu'il faut parfois dépasser.",
        "exemple": "Sortons de cette logique de jeu à somme nulle ; cherchons ensemble une synergie qui crée de la valeur pour les deux parties.",
        "formule": "ΣGains = 0 → opposition totale",
        "niveau": "★★★☆☆"
    },
    {
        "sous_section": "♟️ Théorie des Jeux",
        "titre": "Le Dilemme du Prisonnier",
        "sens": "Situation où deux acteurs rationnels choisissent individuellement une option sous-optimale par manque de confiance mutuelle.",
        "exemple": "Nous sommes face à un dilemme du prisonnier : si nous ne coopérons pas par peur d'être trahis, nous perdons tous les deux.",
        "formule": "Coopérer + Coopérer > Trahir + Trahir",
        "niveau": "★★★★☆"
    },
    # Économie & Décision
    {
        "sous_section": "💰 Économie & Décision",
        "titre": "Le Coût d'Opportunité",
        "sens": "Ce que l'on sacrifice en faisant un choix : le bénéfice de la meilleure alternative non choisie. La vraie mesure d'un choix.",
        "exemple": "Le vrai risque n'est pas le coût direct du projet, mais le coût d'opportunité : ce que nous perdons en n'agissant pas maintenant.",
        "formule": "Coût d'opportunité = Valeur(meilleure alternative abandonnée)",
        "niveau": "★★★☆☆"
    },
    {
        "sous_section": "💰 Économie & Décision",
        "titre": "L'Effet de Levier",
        "sens": "Mécanisme par lequel une petite force génère un résultat disproportionnellement grand. Multiplication de l'impact.",
        "exemple": "Ce partenariat stratégique va créer un effet de levier sur notre croissance sans nécessiter de recrutement massif.",
        "formule": "Résultat = Levier × Effort initial",
        "niveau": "★★☆☆☆"
    },
    {
        "sous_section": "💰 Économie & Décision",
        "titre": "L'Asymétrie d'Information",
        "sens": "Déséquilibre où une partie possède plus ou de meilleures informations que l'autre. Source de nombreux conflits et mauvaises décisions.",
        "exemple": "La tension actuelle vient d'une asymétrie d'information entre la direction et le terrain ; rétablissons la transparence.",
        "formule": "Partie A : information I_A > I_B de Partie B → déséquilibre",
        "niveau": "★★★☆☆"
    },
]

# ---- SECTION 6 : FIGURES DE STYLE -------------------------
figures_de_style = [
    {
        "titre": "L'Anaphore",
        "definition": "Répétition d'un même mot ou groupe de mots en début de phrases ou propositions successives. Crée un rythme hypnotique et martèle l'esprit.",
        "effet": "Rythme hypnotique | Mémorisation | Force oratoire",
        "exemple_base": "Il nous faut de la rigueur pour analyser, de la rigueur pour décider, de la rigueur pour agir.",
        "exemple_avance": "Il nous faut briser ce dilemme. Il nous faut redéfinir notre stratégie. Il nous faut, enfin, agir avant qu'il ne soit trop tard.",
        "conseil": "Utilisez l'anaphore uniquement en conclusion ou pour un point culminant. Maximum 3 répétitions pour ne pas lasser.",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "L'Antithèse",
        "definition": "Opposition de deux idées, faits ou concepts pour souligner un contraste frappant. Donne de la profondeur et de la complexité.",
        "effet": "Profondeur | Contraste saisissant | Equilibre dialectique",
        "exemple_base": "Nous devons choisir entre la sécurité de l'immobilisme et le risque nécessaire du progrès.",
        "exemple_avance": "La prudence est une condition nécessaire, mais non suffisante à la survie d'un leader. L'audace, elle, est un pari sur l'avenir.",
        "conseil": "L'antithèse est efficace car elle simule le raisonnement dialectique (thèse / antithèse). Elle donne l'impression de tout peser.",
        "niveau": "★★☆☆☆"
    },
    {
        "titre": "La Prétérition",
        "definition": "Dire que l'on ne va pas parler d'une chose... pour en parler quand même. Art subtil de rappeler sans agresser.",
        "effet": "Rappel sans agressivité | Ironie subtile | Maîtrise de soi",
        "exemple_base": "Je ne reviendrai pas sur l'échec de l'an dernier, je préfère me concentrer sur les solutions d'avenir.",
        "exemple_avance": "Je ne m'étendrai pas ici sur les retards de livraison ni sur leurs conséquences opérationnelles — les chiffres parlent d'eux-mêmes.",
        "conseil": "Très utile en réunion : elle rappelle un problème sans paraître rancunier, tout en maintenant la pression.",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "L'Hypotypose",
        "definition": "Décrire une situation avec une vivacité et un réalisme si intenses que l'auditeur croit la voir se dérouler devant ses yeux.",
        "effet": "Visualisation forcée | Impact émotionnel | Présence dramatique",
        "exemple_base": "Voyez ces chiffres qui s'effondrent, ces serveurs qui saturent, ces clients qui nous quittent les uns après les autres.",
        "exemple_avance": "Imaginez : il est 3h du matin, la salle de crise est éclairée au néon, les téléphones sonnent sans relâche — c'est la réalité d'une panne non anticipée.",
        "conseil": "L'hypotypose doit rester sobre en milieu professionnel. Elle est redoutable pour introduire une problématique et créer l'urgence.",
        "niveau": "★★★★☆"
    },
    {
        "titre": "La Clausule",
        "definition": "Terminer une phrase par le mot le plus important, le plus fort, le plus percutant. La dernière impression est la plus durable.",
        "effet": "Impact maximal | Mémorisation | Puissance conclusive",
        "exemple_base": "Pour réussir, cette transformation est indispensable. (et non : 'Cette transformation indispensable nous fera réussir')",
        "exemple_avance": "Car dans cet intervalle de confiance où se joue notre destin, seule l'audace est statistiquement souveraine.",
        "conseil": "Règle d'or : ne finissez JAMAIS une phrase par un mot faible. Réorganisez toujours pour placer le mot clé en fin de proposition.",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "La Concession Stratégique",
        "definition": "Accorder un point à l'adversaire pour mieux imposer le sien. Marque la magnanimité et donne plus de force à la réfutation.",
        "effet": "Crédibilité | Désarmement de l'adversaire | Élégance dialectique",
        "exemple_base": "Certes, votre analyse est pertinente sur ce point ; je rejoins votre constat. Toutefois, la conclusion que vous en tirez me semble prématurée.",
        "exemple_avance": "Je vous accorde que le risque technique existe. Mais à l'aune du coût d'opportunité, ne pas agir est un risque bien supérieur.",
        "conseil": "La concession doit être sincère et précise. Une concession vague semble calculée. Une concession précise semble honnête.",
        "niveau": "★★★☆☆"
    },
    {
        "titre": "L'Euphémisme",
        "definition": "Adoucir une réalité difficile ou brutale par une expression plus douce. Permet de nommer l'inacceptable sans choquer.",
        "effet": "Diplomatie | Tension réduite | Maintien des relations",
        "exemple_base": "'Nos équipes ont rencontré des difficultés d'exécution' plutôt que 'L'équipe a complètement raté la livraison'.",
        "exemple_avance": "Il convient de parler d'un 'ajustement de trajectoire budgétaire' plutôt que d'un 'dépassement de coûts non maîtrisé'.",
        "conseil": "À utiliser avec parcimonie : l'euphémisme excessif finit par sembler hypocrite. Il sert à gérer les émotions, non à masquer la réalité.",
        "niveau": "★★☆☆☆"
    },
]

# ---- SECTION 7 : MÉTHODE RHÉTORIQUE CLASSIQUE -------------
methode_rhetorique = {
    "structure_aristote": [
        {
            "etape": "1. L'EXORDE",
            "role": "L'Accroche — Ethos",
            "description": "C'est l'ouverture du discours. Son but : établir votre légitimité (Ethos) et capter immédiatement l'attention de l'auditoire. Un exorde raté = un discours perdu.",
            "formule": "Commencez par un fait saisissant, une question, une prétérition ou une référence à votre expérience.",
            "exemple": "« En tant qu'ingénieur ayant géré plus de dix crises réseau majeures sur notre territoire, je suis en position de vous dire... »"
        },
        {
            "etape": "2. LA NARRATION",
            "role": "Les Faits — Objectivité",
            "description": "L'exposé des faits doit paraître objectif et incontestable. C'est ici que vous posez le décor que votre démonstration va explorer.",
            "formule": "Utilisez 'il est constant que', 'force est de constater', 'en l'espèce'. Restez factuel et précis.",
            "exemple": "« Force est de constater que depuis 6 mois, notre taux d'indisponibilité a augmenté de 40 %, un chiffre statistiquement significatif. »"
        },
        {
            "etape": "3. LA CONFIRMATION",
            "role": "La Preuve — Logos",
            "description": "C'est le cœur du discours. Votre thèse est démontrée ici avec tous vos outils logiques, mathématiques, statistiques. Le Logos prime.",
            "formule": "Insérez vos concepts : espérance mathématique, analyse de sensibilité, coût d'opportunité. Utilisez 'il en résulte mécaniquement que'.",
            "exemple": "« L'espérance mathématique de l'investissement préventif est positive dans 87% des scénarios simulés. »"
        },
        {
            "etape": "4. LA RÉFUTATION",
            "role": "Anticiper les Objections",
            "description": "Détruire les contre-arguments AVANT qu'ils ne soient formulés. L'art de la réfutation préventive. Marque la maîtrise absolue du sujet.",
            "formule": "Introduisez l'objection adverse vous-même (paradoxalement, cela vous renforce) puis démontrez-en la limite.",
            "exemple": "« Certains diront que le coût est prohibitif. Certes, l'investissement est lourd — mais le coût d'opportunité de l'inaction est bien supérieur. »"
        },
        {
            "etape": "5. LA PÉRORAISON",
            "role": "La Conclusion — Pathos",
            "description": "La conclusion émotionnelle qui pousse à l'action. Le Pathos entre en scène. C'est ici que vous touchez le cœur autant que la raison.",
            "formule": "Utilisez une anaphore puissante, une clausule mémorable, et un appel à la vision collective.",
            "exemple": "« Car en dernière analyse, le véritable risque n'est pas l'échec technique, mais le sacrifice de notre avenir sur l'autel de notre confort présent. »"
        },
    ],
    "trois_leviers": [
        {
            "levier": "ETHOS — La Crédibilité",
            "emoji": "🏛️",
            "description": "Votre autorité morale et professionnelle. Ce que vous êtes, ce que vous avez vécu, ce que vous représentez.",
            "construire": "Citez votre expérience concrète. Montrez votre connaissance du terrain. Adoptez un ton grave et posé.",
            "exemple": "« En tant que responsable de la cellule NOC depuis 5 ans, j'ai observé ce phénomène sur 3 générations d'équipements... »",
        },
        {
            "levier": "LOGOS — La Logique",
            "emoji": "🔬",
            "description": "La démonstration rationnelle. Les chiffres, les faits, les raisonnements logiques. C'est votre arsenal mathématique et analytique.",
            "construire": "Utilisez les concepts scientifiques, les statistiques, les causalités. Évitez les impressions : quantifiez.",
            "exemple": "« L'analyse de sensibilité démontre que même avec un écart de 15% sur nos hypothèses, le ROI reste positif. »",
        },
        {
            "levier": "PATHOS — L'Émotion",
            "emoji": "❤️",
            "description": "L'appel aux émotions de l'auditoire. Ce n'est pas la manipulation : c'est rappeler ce qui est en jeu pour les personnes concernées.",
            "construire": "Utilisez l'hypotypose, les métaphores humaines. Reliez le sujet technique à son impact sur les personnes réelles.",
            "exemple": "« Imaginez l'impact sur nos équipes terrain, sur leur sécurité, sur la continuité du service pour nos clients. »",
        },
    ],
    "trinite": {
        "thèse": "Le Constat objectif — CE QUI EST",
        "antithese": "La Limite ou l'Obstacle — CE QUI BLOQUE",
        "synthese": "La Solution proposée — CE QUI DOIT ÊTRE FAIT",
        "regle": "Le cerveau humain retient les informations groupées par 3. C'est une loi cognitive, pas une convention stylistique."
    }
}

# ---- SECTION 8 : CONFIANCE EN SOI & COACHING --------------
coaching_confiance = {
    "caracteristiques": [
        {
            "titre": "L'Indécision Chronique",
            "description": "Face à l'indécision, on est confronté à l'impossibilité de choisir. On étudie les conséquences d'un choix, puis d'un autre, sans jamais décider. Ce phénomène peut durer des années et engendrer une véritable souffrance.",
            "exemple": "Un salarié qui veut créer son entreprise mais n'ose pas quitter son poste par peur de l'échec reste paralysé des années.",
            "solution": "Acceptez qu'une décision imparfaite prise aujourd'hui vaut mieux qu'une décision parfaite jamais prise. L'action génère l'information que la réflexion ne peut pas produire.",
            "signe_alerte": "⚠️ Si vous remettez la même décision à plus tard depuis plus de 3 mois, c'est de l'indécision chronique."
        },
        {
            "titre": "La Gentillesse Excessive",
            "description": "Les personnes manquant de confiance évitent de contrarier l'autre à tout prix. Vouloir être 'toujours gentil' est en réalité un manque de respect envers soi-même.",
            "exemple": "'Je ne suis pas d'accord avec vous, je respecte votre idée, mais ma position est différente' — voilà l'affirmation saine vs la capitulation.",
            "solution": "S'affirmer n'est en rien un manque de respect de l'autre, c'est un respect de soi. Il existe 3 niveaux : trop gentil (manque de confiance) / affirmé (idéal) / obtus (manque de respect).",
            "signe_alerte": "⚠️ Si vous dites toujours 'oui' alors que vous pensez 'non', c'est un symptôme de manque de confiance."
        },
        {
            "titre": "Le Syndrome de la Promotion",
            "description": "Refuser une promotion ou une responsabilité supérieure par peur de ne pas être à la hauteur. Dix ans plus tard, la personne est au même poste.",
            "exemple": "Ceux qui acceptent les promotions malgré l'incertitude progressent. Ceux qui refusent par peur restent stationnaires.",
            "solution": "La compétence vient de l'expérience acquise dans le poste, pas de la maîtrise préalable. Personne n'est 100% prêt avant d'accepter une responsabilité nouvelle.",
            "signe_alerte": "⚠️ Si votre première réaction à une opportunité est 'je ne suis pas prêt', questionnez cette réaction."
        },
        {
            "titre": "Ne Pas Savoir Dire Non",
            "description": "Répondre 'oui' à une demande alors que l'on pense 'non'. Ce n'est pas de la politesse, c'est de la capitulation.",
            "exemple": "Face à une tâche imprévue : 'C'est une excellente idée, mais je ne peux pas car vous m'avez confié une priorité absolue. Souhaitez-vous que je réorganise mes priorités ?'",
            "solution": "Dire non s'apprend. Technique : présentez les faits objectifs, proposez une alternative. Jamais d'excuse excessive, jamais de justification excessive.",
            "signe_alerte": "⚠️ Dire non de manière diplomatique, c'est respecter l'autre autant que vous-même."
        },
    ],
    "causes": [
        {
            "cause": "Les Difficultés Vécues",
            "detail": "Notre passé peut être à la source d'une peur durable. Une tragédie personnelle peut laisser des traces dans le subconscient, et nous pouvons continuer d'associer notre présent à notre passé des années plus tard.",
        },
        {
            "cause": "Les Échecs Passés",
            "detail": "Un échec douloureux s'enregistre durablement en mémoire. Il génère un souvenir négatif qui resurface chaque fois que l'on se retrouve dans une situation approchante — même sans lien réel.",
        },
        {
            "cause": "L'Environnement Familial",
            "detail": "C'est souvent la cause principale. Des parents dévalorisants, des frères et sœurs qui collent des 'étiquettes négatives' créent un déficit profond d'estime de soi.",
        },
        {
            "cause": "L'Éducation Rigide",
            "detail": "'Il faut se faire discret', 'Ne parle pas quand les grandes personnes sont là' — ces injonctions peuvent faire des dégâts considérables sur la confiance personnelle à long terme.",
        },
        {
            "cause": "L'Imagination Exagérée",
            "detail": "Imaginer les pires scénarios avant un simple rendez-vous. L'imagination crée une peur panique qui déclenche un processus d'inhibition, souvent pire que la réalité elle-même.",
        },
    ],
    "chiffre_cle": "40% des personnes dans le monde manquent de confiance en elles, quel que soit leur milieu culturel. (Étude américaine citée dans le Master Coach en développement personnel)"
}

# ---- SECTION 9 : DISCOURS MODÈLE ANNOTÉ ------------------
discours_modele = {
    "titre": "L'Impératif de la Mutation",
    "contexte": "Simulation d'une intervention en comité de direction ou assemblée décisionnelle. Ce discours fusionne la rigueur mathématique (Logos) avec l'élégance rhétorique française (Ethos et Pathos).",
    "texte": """« Messieurs, Mesdames, je ne m'étendrai pas ici sur les succès passés qui, bien que glorieux, appartiennent désormais à une régression vers la moyenne que nous ne pouvons plus ignorer. [PRÉTÉRITION + LOGOS]

Regardez notre organisation : sans une impulsion nouvelle, l'entropie fait son œuvre, transformant notre agilité d'hier en une inertie bureaucratique qui nous consume. [HYPOTYPOSE + LOGOS] Certes, certains prônent la prudence ; mais la prudence est une condition nécessaire, mais non suffisante à la survie d'un leader. [ANTITHÈSE + LOGOS] Si nous suivions la logique de l'immobilisme jusqu'au bout, nous arriverions à admettre que pour ne pas couler, il suffirait de ne plus naviguer : c'est une absurdité que nos parts de marché démentent déjà. [RAISONNEMENT PAR L'ABSURDE]

Il nous faut aujourd'hui briser ce dilemme du prisonnier qui nous paralyse face à la concurrence.
Il nous faut redéfinir notre espace vectoriel des possibles.
Il nous faut, enfin, agir avant que le point de bascule ne rende toute décision caduque. [ANAPHORE]

Au-delà des chiffres, c'est une question de vision. Car en dernière analyse, le véritable risque n'est pas celui de l'échec technique, mais bien le coût d'opportunité de notre indécision : le sacrifice de notre avenir sur l'autel de notre confort présent. Choisissons la mutation, car dans cet intervalle de confiance où se joue notre destin, seule l'audace est statistiquement souveraine. » [PATHOS + CLAUSULE]""",
    "annotations": [
        ("EXORDE (Ethos)", "Ton grave et posé, prétérition pour rappeler le passé sans y rester coincé. Établit la crédibilité."),
        ("NARRATION (Logos)", "Entropie, régression vers la moyenne — des lois quasi-physiques pour prouver l'urgence de façon irréfutable."),
        ("RÉFUTATION", "Le passage sur la prudence anticipe l'objection des opposants et la disqualifie comme insuffisante."),
        ("ANAPHORE", "'Il nous faut... Il nous faut... Il nous faut...' — rythme de marteau qui s'imprime dans les esprits."),
        ("PÉRORAISON (Pathos)", "Le coût d'opportunité et le sacrifice de l'avenir provoquent un sentiment d'urgence morale. Action immédiate."),
        ("CLAUSULE", "Dernier mot : 'souveraine'. Fort, mémorable, inattendu. C'est l'image que l'auditoire emporte."),
    ]
}

# ---- SECTION 10 : BIBLIOTHÈQUE DE MAÎTRES ----------------
bibliotheque = [
    {
        "auteur": "Arthur Schopenhauer",
        "ouvrage": "L'Art d'avoir toujours raison (La Dialectique Éristique)",
        "objectif": "La Joute Verbale — Gagner le débat",
        "description": "L'ouvrage de référence absolu pour quiconque veut comprendre les dessous d'un débat. Schopenhauer y répertorie 38 stratagèmes pour l'emporter dans une discussion, que l'on ait raison ou non. Indispensable pour repérer les pièges adverses.",
        "pour_qui": "Tout orateur qui affronte des adversaires en réunion ou en négociation.",
        "niveau": "⭐⭐⭐⭐⭐ — INDISPENSABLE"
    },
    {
        "auteur": "Cicéron",
        "ouvrage": "De l'Orateur (De Oratore)",
        "objectif": "La Structure — Construire un plan infaillible",
        "description": "Le maître de la rhétorique antique. Cicéron pose que l'orateur parfait doit avoir la culture d'un historien, la précision d'un logicien et la voix d'un tragédien. Un programme complet d'éloquence.",
        "pour_qui": "Ceux qui veulent bâtir des discours architecturalement solides et adapter leur propos à l'auditoire.",
        "niveau": "⭐⭐⭐⭐⭐ — FONDAMENTAL"
    },
    {
        "auteur": "Nicolas Boileau",
        "ouvrage": "L'Art poétique",
        "objectif": "La Clarté — L'économie de mots",
        "description": "La citation fondatrice : 'Ce que l'on conçoit bien s'énonce clairement, et les mots pour le dire arrivent aisément.' L'enseignement central : une argumentation puissante est une argumentation débarrassée du superflu.",
        "pour_qui": "Ceux dont les argumentaires sont trop denses, trop complexes. L'art de la simplicité efficace.",
        "niveau": "⭐⭐⭐⭐☆ — CLASSIQUE"
    },
    {
        "auteur": "Robert Cialdini",
        "ouvrage": "Influence et Manipulation (Influence: The Psychology of Persuasion)",
        "objectif": "La Psychologie — Comprendre le 'oui'",
        "description": "La version moderne de la rhétorique appliquée à la psychologie sociale. Cialdini identifie les 6 mécanismes cognitifs qui font dire 'oui' : réciprocité, cohérence, preuve sociale, autorité, sympathie, rareté.",
        "pour_qui": "Ceux qui veulent comprendre POURQUOI les gens acceptent ou refusent, et adapter leur persuasion en conséquence.",
        "niveau": "⭐⭐⭐⭐⭐ — INDISPENSABLE"
    },
    {
        "auteur": "Aristote",
        "ouvrage": "Rhétorique",
        "objectif": "Le Fondement — Ethos, Logos, Pathos",
        "description": "L'œuvre fondatrice de toute la pensée rhétorique occidentale. Aristote y définit les trois leviers de persuasion (Ethos, Logos, Pathos) qui restent, 25 siècles plus tard, le cadre de référence de tout discours efficace.",
        "pour_qui": "Ceux qui veulent comprendre les fondations théoriques sur lesquelles repose toute rhétorique efficace.",
        "niveau": "⭐⭐⭐⭐☆ — FONDATEUR"
    },
]

# ============================================================
# ======  CHARGEMENT GOOGLE SHEETS (données distantes)  ======
# ============================================================
@st.cache_data(ttl=60)
def load_remote_data():
    try:
        data = pd.read_csv(URL)
        data.columns = [str(c).strip().lower() for c in data.columns]
        rename_dict = {'categorie': 'catégorie', 'category': 'catégorie', 'thème': 'catégorie'}
        data = data.rename(columns=rename_dict)
        return data.fillna("").to_dict('records')
    except Exception:
        return []

remote_data = load_remote_data()

# ============================================================
# ======  INTERFACE PRINCIPALE  ==============================
# ============================================================

# --- SIDEBAR ---
st.sidebar.markdown("## ⚖️ Rosly Éloquence")
st.sidebar.markdown("*L'Art de Parler avec Puissance*")
st.sidebar.markdown("---")

sections = {
    "🏠 Accueil & Vue d'Ensemble": "accueil",
    "💬 Expressions Idiomatiques": "idiomatique",
    "🔗 Structure & Connecteurs": "structure",
    "🎯 Persuasion & Négociation": "persuasion",
    "⚖️ Rhétorique Juridique": "juridique",
    "🔢 Arsenal Mathématique": "mathematique",
    "🎭 Figures de Style": "figures",
    "🏛️ Méthode Rhétorique Classique": "methode",
    "💪 Confiance en Soi & Coaching": "coaching",
    "📜 Discours Modèle Annoté": "discours",
    "📚 Bibliothèque des Maîtres": "bibliotheque",
    "➕ Mes Expressions (Google Sheets)": "remote",
}

section_choisie = st.sidebar.radio(
    "Navigation",
    list(sections.keys()),
    label_visibility="collapsed"
)
section_id = sections[section_choisie]

st.sidebar.markdown("---")
total_expressions = (
    len(expressions_idiomatiques)
    + len(expressions_structure)
    + len(expressions_persuasion)
    + len(expressions_juridiques)
    + len(expressions_mathematiques)
    + len(figures_de_style)
    + len(bibliotheque)
    + len(remote_data)
)
st.sidebar.metric("📦 Ressources totales", total_expressions)
st.sidebar.markdown("---")
st.sidebar.info("💡 **Conseil du Pro**\n\nLe silence stratégique de 2 secondes avant de répondre donne une impression de maîtrise absolue. Toujours plus élégant qu'un 'euh' sonore.")


# ============================================================
# === RENDU DES SECTIONS =====================================
# ============================================================

def card(color, icon, titre, sous_titre, corps, note=None):
    note_html = f'<p class="ex-box">💡 <b>Exemple :</b> {note}</p>' if note else ""
    st.markdown(f"""
    <div class="card card-{color}">
        <div class="cat-tag cat-tag-{color}">{icon} {sous_titre}</div>
        <h3 class="card-title">{titre}</h3>
        <p class="sens-text">{corps}</p>
        {note_html}
    </div>
    """, unsafe_allow_html=True)


# -------- ACCUEIL --------
if section_id == "accueil":
    st.markdown("""
    <div class="section-header">
        <h2>⚖️ Rosly — L'Art de l'Éloquence</h2>
        <p>Votre bibliothèque personnelle pour parler avec puissance, précision et élégance</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("💬 Idiomes & Phrases", len(expressions_idiomatiques))
    col2.metric("🔢 Outils Mathématiques", len(expressions_mathematiques))
    col3.metric("🎭 Figures de Style", len(figures_de_style))
    col4.metric("📚 Ouvrages de Référence", len(bibliotheque))

    st.markdown("---")
    st.markdown("### 🗺️ Plan de la Bibliothèque")

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        **MAÎTRISER LA LANGUE**
        - 💬 Expressions Idiomatiques — le style
        - 🔗 Structure & Connecteurs — la logique
        - ⚖️ Rhétorique Juridique — l'autorité
        - 🎯 Persuasion & Négociation — l'impact
        """)
    with col_b:
        st.markdown("""
        **MAÎTRISER L'ESPRIT**
        - 🔢 Arsenal Mathématique — la rigueur
        - 🎭 Figures de Style — la forme
        - 🏛️ Méthode Rhétorique — la structure
        - 💪 Confiance en Soi — le fondement
        """)

    st.markdown("""
    <div class="tip-box">
    <b>🎯 Comment utiliser cette bibliothèque ?</b><br>
    Commencez par <b>Méthode Rhétorique Classique</b> pour comprendre la structure.
    Puis parcourez les <b>Figures de Style</b> pour habiller vos arguments.
    Enfin, l'<b>Arsenal Mathématique</b> vous donnera une autorité intellectuelle imbattable.
    </div>
    """, unsafe_allow_html=True)


# -------- IDIOMATIQUE --------
elif section_id == "idiomatique":
    st.markdown("""<div class="section-header"><h2>💬 Expressions Idiomatiques</h2>
    <p>Enrichissez votre registre avec des formules qui marquent les esprits</p></div>""", unsafe_allow_html=True)
    for exp in expressions_idiomatiques:
        card("blue", "💬", exp["titre"], f"IDIOME · {exp['niveau']}",
             exp["sens"], exp["exemple"])

# -------- STRUCTURE --------
elif section_id == "structure":
    st.markdown("""<div class="section-header"><h2>🔗 Structure & Connecteurs</h2>
    <p>Les mots qui guident la pensée de votre interlocuteur</p></div>""", unsafe_allow_html=True)
    for exp in expressions_structure:
        card("teal", "🔗", exp["titre"], f"{exp['usage']} · {exp['niveau']}",
             exp["sens"], exp["exemple"])

# -------- PERSUASION --------
elif section_id == "persuasion":
    st.markdown("""<div class="section-header"><h2>🎯 Persuasion & Négociation</h2>
    <p>L'art de convaincre sans contraindre</p></div>""", unsafe_allow_html=True)
    for exp in expressions_persuasion:
        card("green", "🎯", exp["titre"], f"PERSUASION · {exp['niveau']}",
             exp["sens"], exp["exemple"])

# -------- JURIDIQUE --------
elif section_id == "juridique":
    st.markdown("""<div class="section-header"><h2>⚖️ Rhétorique Juridique</h2>
    <p>Le vocabulaire du droit pour imposer une autorité intellectuelle irréfutable</p></div>""", unsafe_allow_html=True)
    for exp in expressions_juridiques:
        card("red", "⚖️", exp["titre"], f"JURIDIQUE · {exp['niveau']}",
             exp["sens"], exp["exemple"])

# -------- MATHÉMATIQUE --------
elif section_id == "mathematique":
    st.markdown("""<div class="section-header"><h2>🔢 Arsenal Mathématique</h2>
    <p>Transformez vos opinions subjectives en démonstrations structurelles</p></div>""", unsafe_allow_html=True)

    sous_sections_order = [
        "🎲 Probabilités & Incertitude",
        "📊 Statistiques & Rigueur",
        "🔬 Logique & Analyse",
        "⚙️ Systémique & Thermodynamique",
        "♟️ Théorie des Jeux",
        "💰 Économie & Décision",
    ]
    color_map = {
        "🎲 Probabilités & Incertitude": "purple",
        "📊 Statistiques & Rigueur": "teal",
        "🔬 Logique & Analyse": "blue",
        "⚙️ Systémique & Thermodynamique": "orange",
        "♟️ Théorie des Jeux": "red",
        "💰 Économie & Décision": "green",
    }

    for ss in sous_sections_order:
        items = [e for e in expressions_mathematiques if e["sous_section"] == ss]
        if not items:
            continue
        st.markdown(f"### {ss}")
        for exp in items:
            formule_html = f'<p style="font-family:monospace;background:#F3F4F6;padding:6px 12px;border-radius:6px;color:#374151;font-size:0.88em;">∑ {exp["formule"]}</p>'
            col = color_map.get(ss, "blue")
            st.markdown(f"""
            <div class="card card-{col}">
                <div class="cat-tag cat-tag-{col}">{ss} · {exp['niveau']}</div>
                <h3 class="card-title">{exp['titre']}</h3>
                <p class="sens-text">{exp['sens']}</p>
                {formule_html}
                <p class="ex-box">💡 <b>Exemple :</b> {exp['exemple']}</p>
            </div>
            """, unsafe_allow_html=True)

# -------- FIGURES DE STYLE --------
elif section_id == "figures":
    st.markdown("""<div class="section-header"><h2>🎭 Figures de Style</h2>
    <p>La forme donne de la force au fond — maîtrisez les outils du style</p></div>""", unsafe_allow_html=True)
    colors = ["blue", "gold", "green", "red", "purple", "teal", "orange"]
    for i, fig in enumerate(figures_de_style):
        col = colors[i % len(colors)]
        st.markdown(f"""
        <div class="card card-{col}">
            <div class="cat-tag cat-tag-{col}">🎭 FIGURE DE STYLE · {fig['niveau']}</div>
            <h3 class="card-title">{fig['titre']}</h3>
            <p class="sens-text"><b>Définition :</b> {fig['definition']}</p>
            <p style="color:#6B7280;font-size:0.88em;margin:6px 0;"><b>Effet :</b> {fig['effet']}</p>
            <p class="ex-box">📌 <b>Exemple simple :</b> {fig['exemple_base']}</p>
            <p class="ex-box" style="border-left-color:#B8860B;background:#FFFBEB;">🌟 <b>Exemple avancé :</b> {fig['exemple_avance']}</p>
            <div class="tip-box" style="margin-top:10px;font-size:0.88em;">💡 <b>Conseil d'expert :</b> {fig['conseil']}</div>
        </div>
        """, unsafe_allow_html=True)

# -------- MÉTHODE RHÉTORIQUE --------
elif section_id == "methode":
    st.markdown("""<div class="section-header"><h2>🏛️ Méthode Rhétorique Classique</h2>
    <p>La structure aristotélicienne adaptée au monde professionnel moderne</p></div>""", unsafe_allow_html=True)

    st.markdown("### 📐 Les 5 Étapes du Discours Classique")
    step_colors = ["blue", "teal", "green", "orange", "red"]
    for i, etape in enumerate(methode_rhetorique["structure_aristote"]):
        col = step_colors[i % len(step_colors)]
        st.markdown(f"""
        <div class="card card-{col}">
            <div class="cat-tag cat-tag-{col}">{etape['etape']}</div>
            <h3 class="card-title">{etape['role']}</h3>
            <p class="sens-text">{etape['description']}</p>
            <p class="ex-box">📌 <b>Formule :</b> {etape['formule']}</p>
            <p class="ex-box" style="border-left-color:#B8860B;background:#FFFBEB;">💬 {etape['exemple']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ⚡ Les 3 Leviers de Persuasion (Ethos, Logos, Pathos)")
    c1, c2, c3 = st.columns(3)
    for col_ui, levier in zip([c1, c2, c3], methode_rhetorique["trois_leviers"]):
        with col_ui:
            st.markdown(f"""
            <div class="card card-blue" style="text-align:center;">
                <div style="font-size:2.5em;">{levier['emoji']}</div>
                <h3 class="card-title" style="text-align:center;">{levier['levier']}</h3>
                <p class="sens-text">{levier['description']}</p>
                <p style="color:#6B7280;font-size:0.85em;">{levier['construire']}</p>
                <p class="ex-box">{levier['exemple']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🔺 La Trinité Rhétorique (Plan en 3 Points)")
    tr = methode_rhetorique["trinite"]
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.success(f"**THÈSE**\n\n{tr['thèse']}")
    with col_b:
        st.warning(f"**ANTITHÈSE**\n\n{tr['antithese']}")
    with col_c:
        st.info(f"**SYNTHÈSE**\n\n{tr['synthese']}")
    st.markdown(f"""<div class="tip-box">🧠 <b>Pourquoi 3 ?</b> {tr['regle']}</div>""", unsafe_allow_html=True)

# -------- COACHING --------
elif section_id == "coaching":
    st.markdown("""<div class="section-header"><h2>💪 Confiance en Soi & Coaching</h2>
    <p>Les fondements psychologiques de la prise de parole et du leadership</p></div>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="warning-box">
    <b>📊 Chiffre Clé</b><br>{coaching_confiance['chiffre_cle']}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔍 Les 4 Symptômes du Manque de Confiance")
    symp_colors = ["red", "orange", "purple", "teal"]
    for i, carac in enumerate(coaching_confiance["caracteristiques"]):
        col = symp_colors[i % 4]
        st.markdown(f"""
        <div class="card card-{col}">
            <div class="cat-tag cat-tag-{col}">🔍 SYMPTÔME #{i+1}</div>
            <h3 class="card-title">{carac['titre']}</h3>
            <p class="sens-text">{carac['description']}</p>
            <p class="ex-box">💬 <b>Exemple :</b> {carac['exemple']}</p>
            <div class="tip-box" style="margin-top:10px;font-size:0.88em;">✅ <b>Solution :</b> {carac['solution']}</div>
            <p style="color:#DC2626;font-size:0.85em;margin-top:8px;">{carac['signe_alerte']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🌱 Les 5 Causes Profondes")
    for cause in coaching_confiance["causes"]:
        st.markdown(f"""
        <div class="card card-blue" style="border-left-color:#6B7280;">
            <div class="cat-tag" style="color:#6B7280;">CAUSE</div>
            <h3 class="card-title">{cause['cause']}</h3>
            <p class="sens-text">{cause['detail']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tip-box">
    <b>💡 Principe fondamental</b><br>
    Nous ne sommes pas <i>nés</i> confiants ou non-confiants. La confiance est une compétence qui s'apprend, se cultive et se renforce — exactement comme l'éloquence.
    </div>
    """, unsafe_allow_html=True)

# -------- DISCOURS MODÈLE --------
elif section_id == "discours":
    st.markdown("""<div class="section-header"><h2>📜 Discours Modèle Annoté</h2>
    <p>Une démonstration de force oratoire complète, analysée pas à pas</p></div>""", unsafe_allow_html=True)

    dm = discours_modele
    st.markdown(f"""
    <div class="discourse-card">
        <h3>🎤 {dm['titre']}</h3>
        <p style="color:#A08040;font-size:0.88em;margin-bottom:20px;">📌 {dm['contexte']}</p>
        <div class="discourse-body">
            {dm['texte'].replace(chr(10), '<br>')}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔬 Analyse Structurelle du Discours")
    for ann_titre, ann_detail in dm["annotations"]:
        st.markdown(f"""
        <div class="card card-gold">
            <div class="cat-tag cat-tag-gold">🔬 TECHNIQUE</div>
            <h3 class="card-title">{ann_titre}</h3>
            <p class="sens-text">{ann_detail}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tip-box">
    <b>🎯 Ce que ce discours démontre</b><br>
    Un discours puissant ne se contente pas de donner un avis : il <b>démontre une nécessité structurelle</b> tout en emportant l'adhésion par la forme. Logos + Pathos + structure Aristote = impact maximal.
    </div>
    """, unsafe_allow_html=True)

# -------- BIBLIOTHÈQUE --------
elif section_id == "bibliotheque":
    st.markdown("""<div class="section-header"><h2>📚 Bibliothèque des Maîtres</h2>
    <p>Les ouvrages fondamentaux pour maîtriser l'art de convaincre</p></div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="tip-box">
    <b>📖 Combo recommandé</b><br>
    Commencez par <b>Schopenhauer</b> pour le combat (défense et attaque), puis lisez <b>Cicéron</b> pour voir ces techniques appliquées dans des situations de vie ou de mort politique. Terminez par <b>Cialdini</b> pour la dimension psychologique moderne.
    </div>
    """, unsafe_allow_html=True)

    stars_colors = ["gold", "blue", "teal", "green", "purple"]
    for i, livre in enumerate(bibliotheque):
        col = stars_colors[i % len(stars_colors)]
        st.markdown(f"""
        <div class="book-card">
            <div class="cat-tag" style="color:#B8860B;">📚 {livre['objectif']}</div>
            <h3 style="margin:8px 0 4px;font-family:'Playfair Display',serif;">{livre['ouvrage']}</h3>
            <p style="color:#6B7280;font-size:0.9em;margin:0 0 12px;">par <b>{livre['auteur']}</b></p>
            <p style="color:#374151;line-height:1.7;">{livre['description']}</p>
            <div style="display:flex;gap:16px;margin-top:14px;flex-wrap:wrap;">
                <div class="tip-box" style="flex:1;min-width:200px;padding:10px 14px;font-size:0.85em;">
                    👤 <b>Pour qui :</b> {livre['pour_qui']}
                </div>
                <div style="padding:10px 14px;background:#FFFBEB;border:1px solid #FDE68A;border-radius:8px;flex:1;min-width:160px;font-size:0.85em;color:#92400E;">
                    ⭐ {livre['niveau']}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# -------- REMOTE / GOOGLE SHEETS --------
elif section_id == "remote":
    st.markdown("""<div class="section-header"><h2>➕ Mes Expressions Personnelles</h2>
    <p>Expressions chargées depuis votre Google Sheets personnel</p></div>""", unsafe_allow_html=True)

    if remote_data:
        st.success(f"✅ {len(remote_data)} expression(s) chargée(s) depuis Google Sheets")
        for exp in remote_data:
            cat = str(exp.get("catégorie", "Général")).strip()
            card("teal", "📎", exp.get("titre", "Expression"),
                 cat,
                 exp.get("sens", "Définition non renseignée"),
                 exp.get("exemple", "Aucun exemple disponible."))
    else:
        st.warning("⚠️ Aucune donnée distante chargée. Vérifiez que votre Google Sheet est public et correctement structuré (colonnes : catégorie, titre, sens, exemple).")
        st.markdown("""
        **Structure attendue du Google Sheet :**

        | catégorie | titre | sens | exemple |
        |---|---|---|---|
        | Idiomatique | Mon expression | Ma définition | Mon exemple |
        """)
