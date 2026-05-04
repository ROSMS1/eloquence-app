import streamlit as st
import pandas as pd

SHEET_ID = "1RWQSre19ZmQl4rzxNcsIwvWlJuu_Nm9RMBKbBwPuYyE"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

st.set_page_config(page_title="Rosly — Éloquence & Développement", page_icon="⚖️", layout="wide", initial_sidebar_state="expanded")

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
.card-blue{border-left-color:#1E3A8A;}.card-pink{border-left-color:#9D174D;}
.cat-tag{font-weight:700;font-size:0.7em;text-transform:uppercase;letter-spacing:0.12em;color:#1E3A8A;margin-bottom:6px;}
.cat-tag-gold{color:#B8860B;}.cat-tag-green{color:#1A6B3A;}.cat-tag-red{color:#8B1A1A;}
.cat-tag-purple{color:#5B2D8E;}.cat-tag-teal{color:#0E7490;}.cat-tag-orange{color:#C05621;}
.card-title{margin:6px 0 10px;font-size:1.15em;color:#1a1a2e;}
.sens-text{color:#374151;font-weight:500;margin:8px 0;line-height:1.6;}
.ex-box{background:#F3F4F6;padding:12px 16px;border-radius:8px;font-style:italic;color:#4B5563;border-left:3px solid #CBD5E1;margin-top:10px;line-height:1.6;}
.solution-box{background:#F0FDF4;padding:14px 18px;border-radius:10px;border-left:4px solid #16A34A;margin-top:10px;color:#14532D;}
.warning-box{background:linear-gradient(135deg,#FFF7ED 0%,#FFEDD5 100%);border:1px solid #FED7AA;border-radius:12px;padding:18px 22px;margin:12px 0;color:#7C2D12;}
.tip-box{background:linear-gradient(135deg,#EFF6FF 0%,#DBEAFE 100%);border:1px solid #BFDBFE;border-radius:12px;padding:18px 22px;margin:12px 0;color:#1E40AF;}
.key-box{background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);color:#E8D5B7;padding:20px 26px;border-radius:14px;border:1px solid #B8860B;margin:16px 0;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.section-header{background:linear-gradient(135deg,#1E3A8A 0%,#1e40af 100%);color:white;padding:16px 24px;border-radius:12px;margin-bottom:24px;margin-top:10px;}
.section-header h2{color:white;margin:0;font-size:1.4em;}
.section-header p{color:#BFDBFE;margin:6px 0 0;font-size:0.9em;}
.stress-header{background:linear-gradient(135deg,#7C2D12 0%,#991B1B 100%);}
.coach-header{background:linear-gradient(135deg,#14532D 0%,#166534 100%);}
.discourse-card{background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);color:#E8D5B7;padding:30px 36px;border-radius:16px;box-shadow:0 8px 30px rgba(0,0,0,0.25);margin-bottom:20px;border:1px solid #B8860B;}
.discourse-body{line-height:1.9;font-size:1.02em;color:#EDE0C8;}
.book-card{background:white;padding:22px 26px;border-radius:14px;border-top:5px solid #B8860B;box-shadow:0 3px 12px rgba(0,0,0,0.08);margin-bottom:18px;}
[data-testid="stSidebar"]{background:#1a1a2e;}
[data-testid="stSidebar"] *{color:#E8D5B7 !important;}
</style>
""", unsafe_allow_html=True)

# ================================================================
# BASE DE DONNÉES
# ================================================================

IDIOMES = [
    {"titre":"Avoir l'apanage de","sens":"Posséder un privilège exclusif ou une qualité propre à soi seul.","exemple":"La rigueur n'est pas l'apanage des mathématiciens : elle est la marque de tout esprit d'élite.","niveau":"★★★☆☆"},
    {"titre":"Sortir de ses gonds","sens":"Perdre son sang-froid et se mettre violemment en colère.","exemple":"Devant tant d'injustice manifeste, il a fini par sortir de ses gonds lors du conseil.","niveau":"★★☆☆☆"},
    {"titre":"Une victoire à la Pyrrhus","sens":"Victoire obtenue au prix de pertes si lourdes qu'elle équivaut à une défaite. Référence au roi Pyrrhus d'Épire.","exemple":"Il a remporté l'appel d'offres, mais à quel coût humain ? C'est une victoire à la Pyrrhus.","niveau":"★★★★☆"},
    {"titre":"S'acquitter d'une tâche","sens":"Accomplir une obligation ou un travail avec soin et diligence.","exemple":"Il s'est acquitté de sa mission avec un professionnalisme exemplaire, nonobstant les contraintes.","niveau":"★★☆☆☆"},
    {"titre":"Céder aux sirènes de...","sens":"Se laisser séduire par une proposition attrayante mais potentiellement trompeuse.","exemple":"Beaucoup d'organisations ont cédé aux sirènes du profit facile, sacrifiant leur durabilité.","niveau":"★★★☆☆"},
    {"titre":"Canard boiteux","sens":"Élément défaillant ou inadapté au sein d'un groupe ou d'un système.","exemple":"Sans maintenance préventive, ce nœud réseau deviendra le canard boiteux de l'infrastructure.","niveau":"★★☆☆☆"},
    {"titre":"Réagir au quart de tour","sens":"Réagir avec une rapidité absolue à une sollicitation ou un événement imprévu.","exemple":"Face à une panne secteur, l'équipe NOC doit être formée à réagir au quart de tour.","niveau":"★★☆☆☆"},
    {"titre":"Tenir la dragée haute","sens":"Résister à quelqu'un, ne pas lui céder facilement ; lui imposer des conditions exigeantes.","exemple":"Lors de la négociation contractuelle, notre équipe a tenu la dragée haute aux fournisseurs.","niveau":"★★★☆☆"},
    {"titre":"Brûler ses vaisseaux","sens":"Prendre une décision irrévocable qui coupe tout chemin de retour. Référence à Hernán Cortés.","exemple":"En lançant ce projet sans plan B, il a délibérément brûlé ses vaisseaux pour forcer l'engagement total.","niveau":"★★★★☆"},
]

CONNECTEURS = [
    {"titre":"En premier lieu / Tout d'abord","sens":"Introduire une première idée de façon claire.","exemple":"Tout d'abord, procédons à l'analyse de l'état des équipements actifs sur le site.","usage":"Introduction","niveau":"★☆☆☆☆"},
    {"titre":"Force est de constater","sens":"Imposer un fait qui s'impose objectivement, sans possibilité de le nier.","exemple":"Force est de constater que la qualité de service s'est détériorée depuis la dernière mise à jour.","usage":"Constat","niveau":"★★☆☆☆"},
    {"titre":"De surcroît / Par ailleurs","sens":"Ajouter une information complémentaire de manière fluide et formelle.","exemple":"L'économie va ralentir ; de surcroît, les taux augmentent, réduisant notre marge de manœuvre.","usage":"Ajout","niveau":"★★☆☆☆"},
    {"titre":"Ceci étant dit / Toutefois","sens":"Marquer une opposition ou une nuance avec élégance.","exemple":"Le projet est validé. Ceci étant dit, il convient de rester prudents sur les délais d'exécution.","usage":"Opposition","niveau":"★★☆☆☆"},
    {"titre":"En définitive / Somme toute","sens":"Conclure ou synthétiser une démonstration en ramenant à l'essentiel.","exemple":"En définitive, la solution redondante est la plus pérenne et la plus économiquement rationnelle.","usage":"Conclusion","niveau":"★★☆☆☆"},
    {"titre":"Il en résulte mécaniquement que","sens":"Exprimer une conséquence logique et inéluctable — comme une loi naturelle.","exemple":"La batterie n'a pas été testée depuis 18 mois ; il en résulte mécaniquement que son autonomie est incertaine.","usage":"Causalité","niveau":"★★★☆☆"},
    {"titre":"Ceci est le corollaire direct de","sens":"Conséquence qui découle naturellement et directement d'un premier fait établi.","exemple":"La surcharge du lien microonde est le corollaire direct de l'absence de politique QoS.","usage":"Causalité","niveau":"★★★★☆"},
    {"titre":"À l'aune de...","sens":"En considération de / À la mesure de / À la lumière de.","exemple":"Il faut juger ce résultat à l'aune des contraintes budgétaires auxquelles l'équipe a fait face.","usage":"Évaluation","niveau":"★★★★☆"},
]

PERSUASION = [
    {"titre":"Un levier déterminant","sens":"Facteur clé qui permet de faire basculer une situation de manière significative.","exemple":"La formation continue des techniciens est un levier déterminant pour la réduction des MTTR.","niveau":"★★☆☆☆"},
    {"titre":"Nonobstant","sens":"Signifie 'malgré' ou 'en dépit de'. Très soutenu. Marque l'avance malgré un obstacle.","exemple":"Nous maintenons notre engagement contractuel, nonobstant les difficultés logistiques rencontrées.","niveau":"★★★★☆"},
    {"titre":"Sous réserve de...","sens":"Poser une condition de manière diplomatique et professionnelle.","exemple":"Nous approuvons le démarrage des travaux, sous réserve de validation formelle du plan de sécurité.","niveau":"★★★☆☆"},
    {"titre":"Le statu quo n'est plus une option","sens":"L'immobilisme est désormais aussi dangereux que l'action.","exemple":"Face à la dégradation continue des KPIs, le statu quo n'est plus une option viable.","niveau":"★★★☆☆"},
    {"titre":"Certes..., mais...","sens":"Accorder un point à l'adversaire pour mieux imposer le sien. Structure de la concession rhétorique.","exemple":"Certes, cet investissement est conséquent, mais le coût d'une défaillance majeure serait bien supérieur.","niveau":"★★☆☆☆"},
    {"titre":"En l'absence de position contraire documentée","sens":"Imposer son point de vue en l'absence d'une objection formelle et écrite.","exemple":"En l'absence de position contraire documentée avant vendredi, nous procéderons selon notre plan initial.","niveau":"★★★★☆"},
]

JURIDIQUE = [
    {"titre":"En l'espèce","sens":"Dans le cas présent, dans cette situation précise. Ramène le débat général aux faits concrets.","exemple":"En l'espèce, aucune faute technique n'a été commise par le technicien de maintenance sur ce site.","niveau":"★★★☆☆"},
    {"titre":"Il est constant que...","sens":"Pour présenter un fait comme indiscutable, reconnu de tous.","exemple":"Il est constant que le protocole d'intervention n'a pas été respecté lors de cette maintenance corrective.","niveau":"★★★☆☆"},
    {"titre":"Un faisceau d'indices concordants","sens":"Accumulation de preuves différentes qui mènent toutes vers une même conclusion.","exemple":"C'est un faisceau d'indices concordants — logs, alarmes, rapports terrain — qui pointe vers un défaut RF.","niveau":"★★★★☆"},
    {"titre":"Actori incumbit probatio","sens":"Adage latin : la preuve incombe à celui qui affirme.","exemple":"Il nous accuse de mauvaise foi ? Actori incumbit probatio : qu'il produise les éléments de preuve.","niveau":"★★★★★"},
    {"titre":"Sans préjudice de...","sens":"Sans porter atteinte à / sans remettre en cause. Permet d'agir sur un point sans affecter un autre.","exemple":"Cette décision est prise sans préjudice des droits de recours dont dispose chaque partie.","niveau":"★★★★☆"},
    {"titre":"De jure vs de facto","sens":"De jure = en droit, selon les règles formelles. De facto = en fait, dans la réalité concrète.","exemple":"De jure, le contrat stipule 4h d'intervention ; de facto, nos équipes atteignent 6h sur ce type de panne.","niveau":"★★★☆☆"},
]

MATHS = [
    {"ss":"🎲 Probabilités","titre":"L'Espérance Mathématique (E)","sens":"Valeur moyenne attendue en pondérant chaque résultat par sa probabilité.","exemple":"L'espérance mathématique du projet justifie largement le risque d'échec estimé.","formule":"E(X) = Σ [probabilité × valeur]","niveau":"★★★☆☆"},
    {"ss":"🎲 Probabilités","titre":"L'Inférence Bayésienne","sens":"Mettre à jour sa probabilité a priori en intégrant de nouvelles preuves.","exemple":"À la lumière de ces nouveaux chiffres, ma probabilité a priori doit être réévaluée.","formule":"P(A|B) = P(B|A) × P(A) / P(B)","niveau":"★★★★☆"},
    {"ss":"🎲 Probabilités","titre":"L'Intervalle de Confiance","sens":"Fourchette dans laquelle se situe un paramètre avec un niveau de certitude donné.","exemple":"Nos projections se situent dans un intervalle de confiance à 95 %.","formule":"μ ± 1.96 × (σ/√n) pour 95%","niveau":"★★★☆☆"},
    {"ss":"📊 Statistiques","titre":"La Signification Statistique (p-value)","sens":"Probabilité que le résultat observé soit dû au hasard. Si p<0.05, résultat significatif.","exemple":"Cet écart de performance est statistiquement significatif avec p < 0.01.","formule":"p-value < 0.05 → significatif","niveau":"★★★★☆"},
    {"ss":"📊 Statistiques","titre":"Corrélation ≠ Causalité","sens":"L'argument ultime contre les conclusions hâtives. Deux phénomènes peuvent coévoluer sans lien causal.","exemple":"Il existe une corrélation entre ces facteurs, mais aucun lien de causalité direct.","formule":"Corrélation → r ; Causalité → expérimentation contrôlée","niveau":"★★★☆☆"},
    {"ss":"📊 Statistiques","titre":"La Régression vers la Moyenne","sens":"Après un résultat exceptionnel, le suivant tend naturellement vers la moyenne.","exemple":"Ce pic de performance est exceptionnel ; anticiper une régression naturelle.","formule":"x̄_n+1 ≈ μ lorsque n → ∞","niveau":"★★★★☆"},
    {"ss":"🔬 Logique","titre":"Condition Nécessaire mais non Suffisante","sens":"Quelque chose peut être indispensable sans garantir le résultat à lui seul.","exemple":"Avoir un bon réseau est nécessaire, mais pas suffisant pour garantir la satisfaction client.","formule":"A → B (nécessaire) ≠ A ↔ B (suffisant)","niveau":"★★★☆☆"},
    {"ss":"🔬 Logique","titre":"Le Raisonnement par l'Absurde","sens":"Démontrer qu'une idée est fausse en montrant qu'elle conduit à une contradiction.","exemple":"Si nous suivions cette logique, nous arriverions à admettre qu'il vaut mieux ne pas intervenir du tout.","formule":"Si (hypothèse P) → contradiction, alors P est fausse","niveau":"★★★☆☆"},
    {"ss":"⚙️ Systémique","titre":"L'Entropie","sens":"Mesure du désordre naturel d'un système. Sans entretien, tout tend vers le chaos.","exemple":"Sans communication claire, l'entropie de ce projet augmentera jusqu'à rendre toute action inefficace.","formule":"ΔS ≥ 0 (2ᵉ loi de thermodynamique)","niveau":"★★★★☆"},
    {"ss":"⚙️ Systémique","titre":"Le Point de Bascule (Tipping Point)","sens":"Moment où un petit changement entraîne une transformation radicale et irréversible.","exemple":"Nous approchons du point de bascule : une seule défaillance supplémentaire pourrait tout effondrer.","formule":"Au-delà du seuil critique → changement d'état irréversible","niveau":"★★★☆☆"},
    {"ss":"♟️ Théorie des Jeux","titre":"L'Équilibre de Nash","sens":"Situation stable où aucun acteur n'a intérêt à changer unilatéralement sa stratégie.","exemple":"Nos concurrents et nous sommes dans un équilibre de Nash : personne ne baisse les prix.","formule":"∀i : stratégie_i est optimale étant donné les autres","niveau":"★★★★★"},
    {"ss":"♟️ Théorie des Jeux","titre":"Le Dilemme du Prisonnier","sens":"Deux acteurs rationnels choisissent une option sous-optimale par manque de confiance mutuelle.","exemple":"Si nous ne coopérons pas par peur d'être trahis, nous perdons tous les deux.","formule":"Coopérer + Coopérer > Trahir + Trahir","niveau":"★★★★☆"},
    {"ss":"💰 Économie","titre":"Le Coût d'Opportunité","sens":"Ce que l'on sacrifice en faisant un choix : le bénéfice de la meilleure alternative non choisie.","exemple":"Le vrai risque est le coût d'opportunité : ce que nous perdons en n'agissant pas maintenant.","formule":"Coût d'opportunité = Valeur(meilleure alternative abandonnée)","niveau":"★★★☆☆"},
    {"ss":"💰 Économie","titre":"L'Asymétrie d'Information","sens":"Déséquilibre où une partie possède de meilleures informations que l'autre.","exemple":"La tension vient d'une asymétrie d'information entre la direction et le terrain.","formule":"Partie A : information I_A > I_B → déséquilibre","niveau":"★★★☆☆"},
]

FIGURES = [
    {"titre":"L'Anaphore","definition":"Répétition d'un même mot en début de phrases successives. Crée un rythme hypnotique et martèle l'esprit.","effet":"Rythme hypnotique | Mémorisation | Force oratoire","ex_simple":"Il nous faut de la rigueur pour analyser, de la rigueur pour décider, de la rigueur pour agir.","ex_avance":"Il nous faut briser ce dilemme. Il nous faut redéfinir notre stratégie. Il nous faut agir.","conseil":"Maximum 3 répétitions. À utiliser uniquement aux moments culminants.","niveau":"★★★☆☆"},
    {"titre":"L'Antithèse","definition":"Opposition de deux idées pour souligner un contraste frappant. Donne de la profondeur.","effet":"Profondeur | Contraste | Équilibre dialectique","ex_simple":"Nous devons choisir entre la sécurité de l'immobilisme et le risque nécessaire du progrès.","ex_avance":"La prudence est une condition nécessaire, mais non suffisante à la survie d'un leader.","conseil":"Simule le raisonnement dialectique. Donne l'impression de tout peser.","niveau":"★★☆☆☆"},
    {"titre":"La Prétérition","definition":"Dire que l'on ne va pas parler d'une chose... pour en parler quand même.","effet":"Rappel sans agressivité | Ironie subtile | Maîtrise","ex_simple":"Je ne reviendrai pas sur l'échec de l'an dernier, je préfère me concentrer sur l'avenir.","ex_avance":"Je ne m'étendrai pas sur les retards — les chiffres parlent d'eux-mêmes.","conseil":"Rappelle un problème sans paraître rancunier. Très utile en réunion.","niveau":"★★★☆☆"},
    {"titre":"L'Hypotypose","definition":"Décrire une situation avec une vivacité si intense que l'auditeur croit la voir.","effet":"Visualisation forcée | Impact émotionnel | Présence dramatique","ex_simple":"Voyez ces chiffres qui s'effondrent, ces serveurs qui saturent, ces clients qui nous quittent.","ex_avance":"Imaginez : il est 3h du matin, la salle de crise est éclairée au néon, les téléphones sonnent sans relâche.","conseil":"Redoutable pour créer l'urgence. Rester sobre en milieu professionnel.","niveau":"★★★★☆"},
    {"titre":"La Clausule","definition":"Terminer une phrase par le mot le plus fort. La dernière impression est la plus durable.","effet":"Impact maximal | Mémorisation | Puissance conclusive","ex_simple":"'Pour réussir, cette transformation est INDISPENSABLE.' (et non 'Cette transformation nous fera réussir'.)","ex_avance":"Car dans cet intervalle de confiance où se joue notre destin, seule l'audace est statistiquement souveraine.","conseil":"Règle d'or : ne finissez JAMAIS une phrase par un mot faible.","niveau":"★★★☆☆"},
]

BIBLIOTHEQUE = [
    {"auteur":"Arthur Schopenhauer","ouvrage":"L'Art d'avoir toujours raison","objectif":"La Joute Verbale","description":"38 stratagèmes pour l'emporter dans une discussion, que l'on ait raison ou non. Indispensable pour repérer les pièges adverses et verrouiller vos arguments.","pour_qui":"Tout orateur qui affronte des adversaires en réunion ou en négociation.","niveau":"⭐⭐⭐⭐⭐ — INDISPENSABLE"},
    {"auteur":"Cicéron","ouvrage":"De l'Orateur (De Oratore)","objectif":"La Structure","description":"L'orateur parfait doit avoir la culture d'un historien, la précision d'un logicien et la voix d'un tragédien. Apprendre à adapter son propos à l'auditoire.","pour_qui":"Ceux qui veulent bâtir des discours architecturalement solides.","niveau":"⭐⭐⭐⭐⭐ — FONDAMENTAL"},
    {"auteur":"Nicolas Boileau","ouvrage":"L'Art poétique","objectif":"La Clarté","description":"'Ce que l'on conçoit bien s'énonce clairement.' L'art de la simplicité efficace. Une argumentation puissante est débarrassée du superflu.","pour_qui":"Ceux dont les argumentaires sont trop denses ou trop complexes.","niveau":"⭐⭐⭐⭐☆ — CLASSIQUE"},
    {"auteur":"Robert Cialdini","ouvrage":"Influence et Manipulation","objectif":"La Psychologie","description":"Les 6 mécanismes cognitifs qui font dire 'oui' : réciprocité, cohérence, preuve sociale, autorité, sympathie, rareté.","pour_qui":"Ceux qui veulent comprendre POURQUOI les gens acceptent ou refusent.","niveau":"⭐⭐⭐⭐⭐ — INDISPENSABLE"},
    {"auteur":"Aristote","ouvrage":"Rhétorique","objectif":"Le Fondement","description":"L'œuvre fondatrice de toute la pensée rhétorique occidentale. Ethos, Logos, Pathos — le cadre de référence universel.","pour_qui":"Ceux qui veulent comprendre les fondations théoriques de l'éloquence.","niveau":"⭐⭐⭐⭐☆ — FONDATEUR"},
]

# COACHING DATA
SYMPTOMES = [
    {"titre":"L'Indécision Chronique","description":"L'impossibilité de choisir. On étudie les conséquences d'un choix, puis d'un autre, sans jamais décider. Ce phénomène peut durer des années et engendrer une véritable souffrance.","exemple":"Un salarié qui veut créer son entreprise mais reste paralysé des années par peur de l'échec.","solution":"Une décision imparfaite prise aujourd'hui vaut mieux qu'une décision parfaite jamais prise.","alerte":"Si vous remettez la même décision à plus tard depuis plus de 3 mois, c'est de l'indécision chronique."},
    {"titre":"La Gentillesse Excessive","description":"Éviter de contrarier l'autre à tout prix. S'affirmer n'est en rien un manque de respect de l'autre — c'est un respect de soi. 3 niveaux : trop gentil (manque de confiance) / affirmé (idéal) / obtus (manque de respect).","exemple":"'Je ne suis pas d'accord avec vous, je respecte votre idée, mais ma position est différente' — voilà l'affirmation saine.","solution":"Dire 'ma position est différente' n'est pas une agression. C'est l'expression de votre intégrité intellectuelle.","alerte":"Si vous dites toujours 'oui' alors que vous pensez 'non', c'est un symptôme de manque de confiance."},
    {"titre":"Le Syndrome de la Promotion","description":"Refuser une promotion par peur de ne pas être à la hauteur. Dix ans plus tard, la personne est au même poste. Ceux qui acceptent progressent ; ceux qui refusent par peur restent stationnaires.","exemple":"La compétence vient de l'expérience dans le poste, pas de la maîtrise préalable.","solution":"Personne n'est 100% prêt avant d'accepter une nouvelle responsabilité.","alerte":"Si votre première réaction à une opportunité est 'je ne suis pas prêt', questionnez cette réaction."},
    {"titre":"Ne Pas Savoir Dire Non","description":"Répondre 'oui' alors qu'on pense 'non'. Ce n'est pas de la politesse, c'est de la capitulation. Chaque 'oui' contraint envoie un message négatif à son propre cerveau : 'Je suis faible'.","exemple":"Méthode du 'disque rayé' : reprendre les arguments de l'interlocuteur mot pour mot, puis maintenir fermement son refus.","solution":"Dire non s'apprend. Commencer par des situations de faible importance, puis monter en niveau.","alerte":"Chaque fois que vous cédez sans vouloir céder, vous affaiblissez votre estime de soi."},
]

CAUSES = [
    {"cause":"Les Difficultés Vécues","detail":"Notre passé peut être à la source d'une peur durable. Même plusieurs années plus tard, nous pouvons continuer d'associer notre présent à notre passé — sans le réaliser."},
    {"cause":"Les Échecs Passés (Dr Lozanov)","detail":"Un échec douloureux s'enregistre durablement en mémoire. Le cerveau-ressource ne connaît pas la notion du temps : il perçoit un souvenir d'échec ancien comme une expérience présente. D'où la découverte : 'Réfléchir sur un problème passé est le plus sûr moyen d'en attirer un autre du même ordre.'"},
    {"cause":"L'Environnement Familial","detail":"C'est souvent la cause principale. Des parents dévalorisants, des frères et sœurs qui collent des 'étiquettes négatives' créent un déficit profond d'estime de soi qui peut durer toute une vie adulte."},
    {"cause":"Les Étiquettes de l'Enfance","detail":"'Tu es un bon à rien', 'Tu ne feras rien de ta vie', 'Tais-toi quand les grands parlent'... Ces étiquettes sont majoritairement fausses, mais si on y croit, elles deviennent une réalité. Elles peuvent empêcher quelqu'un de prendre la parole en réunion 20 ans plus tard."},
    {"cause":"Le Perfectionnisme","detail":"30% de la population est atteinte de perfectionnisme. Ils veulent que tout soit parfait dès la première fois. Résultat : ils ne démarrent jamais. Ils restent à jamais au stade du projet."},
    {"cause":"L'Imagination Exagérée","detail":"Imaginer les pires scénarios avant un simple rendez-vous. L'imagination crée une peur panique qui déclenche un processus d'inhibition, souvent bien pire que la réalité."},
    {"cause":"La Peur d'Être Jugé","detail":"Souffrir de la peur d'être jugé, c'est donner systématiquement le pouvoir de sa vie à l'autre. On perd le contrôle de son existence. 15 à 20% des adultes vivent émotionnellement comme des enfants de 3 à 7 ans — en recherche permanente d'approbation."},
]

OUTILS_COACH = [
    {"titre":"Le Mécanisme Interne de Succès (Dr Maxwell Maltz)","description":"Le cerveau ne distingue pas le temps : un souvenir de réussite passée est perçu comme une expérience présente. Puiser dans ses réussites passées active un puissant mécanisme de confiance.","protocole":"1. Fermez les yeux. 2. Listez une réussite passée, aussi modeste soit-elle. 3. Revivez-la avec toutes les émotions. 4. Répétez avec d'autres réussites (intellectuelles, relationnelles, professionnelles). 5. Demandez-vous : 'Qu'est-ce que je sais bien faire ?'","quand":"Avant tout événement stressant. Dès qu'un doute s'installe."},
    {"titre":"La Visualisation Mentale","description":"Des basketteurs s'entraînant mentalement 20 min/matin et 20 min/soir progressent de 19% — presque autant que ceux qui s'entraînent physiquement (21%). Le cerveau-ressource ne fait pas la différence entre réalité et imagination.","protocole":"Créez un film mental où vous êtes l'acteur principal. Visualisez-vous réussir avec confiance ce qui vous fait peur. RÈGLE : Les personnes confiantes SE VOIENT réussir. Les autres SE VOIENT échouer. Choisissez votre film.","quand":"Avant tout événement stressant. Répéter régulièrement pour que le cerveau 'encode' la réussite."},
    {"titre":"Le Plan de Cinq Minutes","description":"La peur d'agir crée une force d'inertie. Une fois la balle mise en mouvement, la force nécessaire pour la maintenir est minime. Le plan de 5 minutes vainc la force d'inertie initiale. Dans 9 cas sur 10, la personne continue spontanément après les 5 minutes.","protocole":"1. Décider de travailler UNIQUEMENT pendant 5 minutes. 2. Se fixer un minuteur. 3. Agir. 4. S'auto-féliciter : 'Bravo, j'ai réussi mon plan de 5 minutes !' 5. Le lendemain : plan de 10 min, puis 15 min. La capitalisation des petits succès déclenche un processus vertueux.","quand":"Pour tout projet que l'on remet à plus tard. Pour toute action que l'on redoute."},
    {"titre":"Les Questions Fécondes (Carnet)","description":"Le cerveau répond infiniment mieux à des questions qu'à des affirmations. Une question féconde mobilise des ressources de confiance. Une question dévalorisante mobilise des ressources de peur. Plus on a de questions fécondes, plus on mobilise de potentiel.","protocole":"Construire un carnet de 300+ questions fécondes : 'Pourquoi je me sens fort maintenant ?' / 'En quoi suis-je capable ici ?' / 'Où sont les forces de confiance en moi ?' / 'Qu'est-ce qui me rend capable de ?' ATTENTION : Éviter 'Pourquoi je n'ai pas peur ?' → la notion de peur est présente = mauvais déclencheur.","quand":"Porter le carnet partout. Le sortir dès qu'une situation crée du doute ou de la peur."},
    {"titre":"Le Cerveau Reptilien vs Néocortical","description":"Cerveau reptilien = cerveau de la peur, centré sur l'avenir anxieux (héritage de -400 000 ans). Cerveau néocortical = cerveau du bonheur, centré sur l'instant présent. Ces deux cerveaux ne fonctionnent pas simultanément — comme un interrupteur.","protocole":"Technique du 'compte à rebours' : Penser à un événement stressant futur. Remonter dans le temps jusqu'à maintenant, en listant à chaque étape : 'Les choses se déroulaient normalement.' Conclure : 'Dans l'instant présent, tout va bien.' À répéter 3 fois par jour au début.","quand":"Lors de chaque montée d'anxiété. Lors de toute pensée d'avenir anxieuse."},
    {"titre":"Le Disque Rayé (Apprendre à Dire Non)","description":"Pour dire non sans blesser : reprendre les arguments de l'interlocuteur presque mot pour mot, puis maintenir fermement son refus. On lui montre qu'on le comprend, tout en tenant sa position. Cela protège l'estime de soi et l'autorité naturelle.","protocole":"'Je comprends bien que tu as envie d'aller au cinéma ce soir. Mais ce soir, j'ai un dîner en famille.' Si insistance : 'Je sais qu'il se garde bien ton fils. Mais ce soir, j'ai ce dîner et c'est très important pour moi.' Répéter : arguments de l'autre + maintenir son refus.","quand":"Dans toute situation de pression sociale. S'entraîner avec un ami d'abord."},
    {"titre":"Le Principe d'Unicité (Je Suis Unique)","description":"Deux personnes totalement identiques n'existent pas sur Terre. Ce qui est rare est précieux. Vous êtes donc précieux. Chaque fois qu'on cherche à être ce que les autres veulent qu'on soit, on perd la face précieuse de soi-même. La confiance en soi, c'est d'abord être soi-même.","protocole":"Mantra quotidien : 'Je suis unique, donc précieux. Ma propre approbation est plus importante que celle des autres. Si ce que je fais apporte satisfaction aux autres, c'est très bien. Sinon, c'est tout aussi bien.'","quand":"Avant toute situation de prise de parole ou de jugement social."},
]

MISSIONS_COACH = [
    {"num":"1","titre":"Le Changement est Nécessaire","detail":"Dans 9 cas sur 10, vous devrez dire à votre coaché qu'il doit CHANGER. Or, paradoxe : le coaché attend des solutions mais peu de changements. Sans accepter de changer, aucune solution n'est possible."},
    {"num":"2","titre":"Définir les Actions de Changement","detail":"Définir avec le coaché les actions concrètes à effectuer avec des étapes précises et des délais précis. Jamais de simples intentions. 'Les bonnes intentions sont souvent des chèques sans provision.'"},
    {"num":"3","titre":"Lancer le Processus","detail":"Comme une fusée sur son pas de tir, le plus dur est le décollage initial. Aider à lancer le processus ICI et MAINTENANT — pas dans une semaine. Le momentum initial est crucial."},
    {"num":"4","titre":"Apporter un Feedback Régulier","detail":"Comme les ingénieurs qui corrigent la trajectoire d'une fusée, le coach donne régulièrement un feedback. Quelques centimètres d'écart au départ = plusieurs kilomètres d'erreur à l'arrivée."},
    {"num":"5","titre":"Répéter — 'Répéter c'est Enseigner'","detail":"Une idée ne s'incruste pas en l'entendant une seule fois. Il faut répéter, en utilisant des images, des métaphores, des exemples concrets. Le message doit s'ancrer profondément."},
    {"num":"6","titre":"Concentrer l'Attention du Coaché","detail":"L'ennemi du changement est la dispersion. L'esprit non maîtrisé est un obstacle au changement. Le coach doit veiller à la FOCALISATION constante sur les actions définies ensemble."},
    {"num":"7","titre":"Développer la Volonté de Gagner","detail":"Aider le coaché à croire en lui-même, en ses forces, en ses ressources. C'est la démarche la plus difficile — et la plus importante. 'Rien n'est possible à celui qui ne croit pas.'"},
    {"num":"8","titre":"Choisir des Modèles Adaptés","detail":"Chaque coaché est unique. L'écoute profonde permet de déterminer quels outils sont réellement adaptés à sa situation. Jamais le même protocole pour tout le monde."},
]

# STRESS DATA
STRESS_FONDEMENTS = [
    {"titre":"Le Stress est un AMI (Prof. Hans Selye)","description":"Le stress n'est pas le problème. C'est son absence de gestion qui pose problème. Le stress est une 'réaction d'adaptation' — un 'syndrome général d'adaptation'. Sans stress, notre espèce n'aurait pas survécu.","fonctions":["✅ Il STIMULE : donne un surplus d'énergie physique et mentale.","✅ Il permet de RÉAGIR : face à l'urgence, il nous rend plus réactifs.","✅ Il AIGUISE les sens : vigilance décuplée, concentration renforcée."],"chiffre":"8 personnes sur 10 se disent stressées. 1 salarié sur 3 en UE est affecté par le stress."},
    {"titre":"Stress Passager vs Anxiété Chronique","description":"Le stress est momentané (déclenché par un facteur identifiable qui disparaît). L'anxiété est un état quasi permanent. La différence est cruciale : le coach traite le stress ; le médecin ou thérapeute traite l'anxiété.","question":"'Qu'est-ce qui a déclenché votre anxiété ?' Si facteur précis non répétitif → stress gérable. Si 'chaque fois qu'un problème arrive' → anxiété chronique → orientation médicale.","chiffre":"95% du temps d'une journée se passe dans le calme. Seulement 5% en état de tension."},
    {"titre":"Le Cerveau Reptilien — La Cause Physiologique","description":"Les stressés chroniques utilisent leur cerveau reptilien (cerveau de la peur, hérité de -400 000 ans) en quasi permanence. Ce cerveau ne connaît que l'avenir anxieux. Or aujourd'hui, 1% de notre temps est en vrai danger (vs 99% à la préhistoire).","consequence":"L'adrénaline et le cortisol s'accumulent sans être consommés. Ils deviennent des poisons dans le sang, accélèrent le vieillissement, fragilisent l'immunité.","solution":"Activer le cerveau NÉOCORTICAL (cerveau du bonheur, centré sur le présent). Ces deux cerveaux ne fonctionnent pas simultanément — comme un interrupteur."},
]

TYPES_STRESSES = [
    {"type":"TYPE A 🔴","desc":"Très stressé chroniquement. Tout devient dramatique. Utilise des expressions catastrophistes. Amplifie et interprète les faits. Les effets du stress sur sa santé sont importants (hypertension, insomnies, troubles cardiaques, migraines, ulcères).","attention":"DÉCONSEILLER tout sport compétitif. Uniquement marche active ou sport détente.","col":"red"},
    {"type":"TYPE B 🟢","desc":"Stressé comme tout le monde, MAIS il s'en tient aux faits précis. Il passe à l'action immédiatement pour consumer son adrénaline. Il se crée des compensations quotidiennes. Aucun symptôme psychosomatique malgré les mêmes situations que le Type A.","attention":"Le MODÈLE à reproduire. Il gère 2,5 fois mieux les situations délicates que les autres.","col":"green"},
    {"type":"TYPE C 🟡","desc":"Stressé moyen, tendance à amplifier. Intermédiaire entre A et B. Susceptible d'évoluer vers le Type B avec le bon accompagnement. Symptômes modérés.","attention":"Accompagnement possible avec les protocoles standards. Surveiller les généralisations.","col":"orange"},
]

PROTOCOLES = [
    {"titre":"🥗 La Diète Médiatique (7 Jours)","description":"La source cachée principale du stress chronique. Chaque mauvaise nouvelle médiatique déclenche une montée de consultations médicales de 20 à 25%. Ce n'est pas l'information qui stresse — c'est l'INTERPRÉTATION que l'on en fait.","protocole":"Pendant 7 jours : zéro TV d'actualité, zéro radio d'info, zéro journal. Remplacer par des programmes choisis (culture, musique, films). Après 7 jours : état radicalement transformé.","avantages":["Voir plus clair en soi-même — pensée plus limpide.","Relativiser ce qui arrive — prise de distance plus grande.","Meilleur contrôle des émotions.","Calme intérieur qui s'installe dès 3 jours.","Baisse significative du niveau d'anxiété."]},
    {"titre":"🧠 Le Focusing (Dr Kobasa)","description":"Prendre conscience de son état de stress AVANT qu'il devienne inconscient. Le stressé pathologique ne se rend même plus compte qu'il est stressé — c'est devenu sa seconde nature. C'est le grand danger.","protocole":"1. Stopper 1 minute. 2. Demander : 'Que se passe-t-il en moi maintenant ?' 3. Scanner son corps de bas en haut : tensions, douleurs, rythme cardiaque. 4. Décrire verbalement à voix haute ce que l'on ressent. 5. Répéter 3x par jour si nécessaire.","avantages":["Dans 8 cas sur 10, la personne se sent plus forte après seulement ce protocole de prise de conscience."]},
    {"titre":"⚡ Agir Immédiatement — Consommer l'Adrénaline","description":"En état de stress, l'adrénaline est un carburant. Si elle n'est pas consommée par l'action, elle se transforme en mauvais stress et empoisonne l'organisme. Le seul moyen de transformer le mauvais stress en bon stress : AGIR.","protocole":"BON STRESS : 'Je ressens de l'adrénaline → c'est un surplus d'énergie → j'agis immédiatement.' MAUVAIS STRESS : 'Je me sens mal → j'attends → l'adrénaline s'accumule → ça empire.' Dès que le stress monte : passer à l'action physique ou mentale dans les minutes qui suivent.","avantages":["L'action libère les énergies | réduit le stress | évacue les hormones | apaise corps et esprit."]},
    {"titre":"🏃 Sport / Marche Active","description":"La marche soutenue de 45-60 minutes réduit le niveau de stress de 50%. Elle déclenche la production d'endorphines (hormones du bien-être). Elle consomme l'excès d'adrénaline. Elle contrôle l'hypertension sans médicament.","protocole":"IMPORTANT pour les Type A : UNIQUEMENT sport-détente, jamais sport de compétition. La marche soutenue dans un lieu calme est suffisante. 45 min/jour minimum. L'étudiant en chimie stressé : après 4 jours de marche quotidienne, son angoisse avait fortement diminué.","avantages":["Brûle le carburant-stress | Produit des endorphines | Contrôle l'hypertension"]},
    {"titre":"⏰ La Colère Différée (5 Minutes)","description":"La colère est une source de grand stress. Le refoulement aussi. La solution : différer la colère de 5 minutes. En 5 minutes, le cerveau néocortical reprend le contrôle et relativise la situation. Le niveau passe de 10/10 à 2/10.","protocole":"Dès que la colère monte : 'Je vais me mettre en colère... dans 5 minutes.' Attendre. En général, la colère a perdu sa raison d'être. Le cerveau néocortical a pris le contrôle. La professeur de mathématiques : en quelques semaines, quasiment plus de colères, et ses élèves travaillaient mieux.","avantages":["Passe du mode reptilien au mode néocortical | Réduit le stress de la colère | Maintient les relations"]},
    {"titre":"⏱️ Le Compte à Rebours (Reptilien → Néocortical)","description":"Pour passer du cerveau de la peur (reptilien) au cerveau du bonheur (néocortical). Le néocortical ne vit que dans l'instant présent. Le reptilien vit dans l'avenir anxieux.","protocole":"1. Penser à l'événement stressant dans X jours. 2. Remonter mentalement jusqu'à maintenant : 'Il y a X jours, les choses se déroulaient normalement. Hier soir, normalement. Ce matin, normalement. Maintenant — tout va bien.' 3. Répéter 3x par jour.","avantages":["Formule : 'Rien, absolument rien, ne m'oblige à me projeter dans le futur de façon anxieuse.'"]},
    {"titre":"🔤 Les Mots qui Soignent les Maux (Sémantique)","description":"Les stressés utilisent des mots à FORTE charge émotionnelle collective : 'terrorisé', 'catastrophe', 'désastre', 'c'est un enfer'. Ces mots déclenchent des réactions biochimiques dans le cerveau qui AMPLIFIENT le stress. Et la loi : 'Le niveau de stress est proportionnel à la concentration en mots à forte charge émotionnelle.'","protocole":"Étape 1 : Revenir au FAIT objectif ('J'ai 45 minutes de retard'). Étape 2 : Réduire progressivement la charge émotionnelle (NE PAS passer d'un coup à une expression très douce — le cerveau résistera). EXEMPLES : 'Catastrophe' → 'Situation peu aisée' → 'Problème'. 'Je suis paniqué' → 'Je suis préoccupé'. 'C'est terrible' → 'C'est difficile'.","avantages":["Réduction quasi immédiate du stress | Accessible partout | Sans aucun outil"]},
    {"titre":"🔬 La Reconstitution (Dr Kobasa)","description":"Imaginer 'ce qu'aurait pu être le pire' permet de relativiser la situation réelle et de dédramatiser. Le pire n'est pas arrivé, et si on peut imaginer pire, c'est qu'on est encore dans une situation gérable.","protocole":"Lors d'un événement stressant, se demander : 'Si les circonstances avaient été encore pires, à quoi auraient-elles pu ressembler ?' Constater que la situation réelle est moins grave. Revenir aux faits avec plus de sérénité.","avantages":["Prendre de la hauteur sur la situation | Dédramatiser | Reprendre le contrôle"]},
    {"titre":"🔌 La Compensation (Reprendre le Contrôle)","description":"Le stress pathologique est déclenché par la SENSATION de ne plus contrôler sa vie. 50% de la gestion du stress = reprendre un sentiment de contrôle, même partiel. Leçon des rats de laboratoire : les rats qui avaient un sentiment de contrôle (même partiel) ne développaient pas les symptômes du stress, malgré les mêmes stimuli.","protocole":"Chaque jour, réserver 45 minutes INVIOLABLES pour une activité choisie librement (lecture, jardinage, sport, musique...). Pendant ce temps, le cerveau reçoit un message puissant : 'Je contrôle encore une partie de ma vie → le stress n'affecte plus mon corps.'","avantages":["Sentiment de contrôle = protection contre les effets négatifs du stress | 45 min/jour suffisent"]},
    {"titre":"👁️ Le Coping (Dr Osten)","description":"Une situation stressante vécue plusieurs fois perd son pouvoir stressant. Le cerveau 'copie' l'expérience et l'encode comme connue. Même visualiser la situation produit un effet similaire. Découverte par Dr Osten en observant des patients en IRM claustrophobes.","protocole":"Avant un événement stressant : visiter les lieux, rencontrer les personnes, simuler la situation. Plus on s'expose à la situation (réellement ou mentalement), moins elle stresse.","avantages":["L'orateur nerveux qui visite la salle avant de parler : le cerveau reconnaît l'environnement et le stress diminue."]},
    {"titre":"🌀 L'Effet Zeigarnik (Stress Inconscient)","description":"Les tâches non terminées créent un stress inconscient, indéfinissable. On ressent un malaise sans en comprendre la cause. La procrastination génère un stress chronique sous-jacent qui s'accumule silencieusement et peut à terme être aussi nocif que le stress conscient.","protocole":"Question au client : 'Avez-vous tendance à remettre à demain ce que vous devriez faire ?' Si oui : agir immédiatement quand possible, ou inscrire dans un agenda précis. Supprimer les 'dossiers mentaux en suspens'.","avantages":["Supprime un stress invisible mais dévastateur | Améliore le bien-être général"]},
]

SOLUTIONS_NAT = [
    {"sol":"La Mélisse","desc":"Favorise le sommeil profond. Agit comme un 'tranquillisant naturel'. Relaxant du système nerveux."},
    {"sol":"Le Ginseng","desc":"Maintient le niveau de sérotonine stable même quand l'adrénaline monte. Permet de dormir normalement malgré le stress."},
    {"sol":"La Valériane","desc":"Efficace quand le stress rend grincheux ou de mauvaise humeur. Améliore la qualité du sommeil profond."},
    {"sol":"La Vitamine C","desc":"Puissant antistress naturel. Sources : orange, kiwi, citron, mangue, goyave, cassis, papaye, pamplemousse. Peut réduire jusqu'à 80% les effets du stress selon les cas."},
    {"sol":"Méthode Dr William James (30 jours)","desc":"Chaque soir : identifier 3 séquences positives de la journée (petites joies, satisfactions, réussites). Les revivre quelques instants avant de dormir. Résultats : propension au positif, esprit apaisé, baisse de l'anxiété."},
]

# ================================================================
# GOOGLE SHEETS
# ================================================================
@st.cache_data(ttl=60)
def load_remote():
    try:
        d = pd.read_csv(URL)
        d.columns = [str(c).strip().lower() for c in d.columns]
        d = d.rename(columns={'categorie':'catégorie','category':'catégorie','thème':'catégorie'})
        return d.fillna("").to_dict('records')
    except:
        return []

remote_data = load_remote()

# ================================================================
# INTERFACE
# ================================================================
st.sidebar.markdown("## ⚖️ Rosly Éloquence")
st.sidebar.markdown("*Éloquence • Confiance • Sérénité*")
st.sidebar.markdown("---")

PAGES = {
    "🏠 Accueil":"accueil",
    "── ÉLOQUENCE ──":"sep",
    "💬 Expressions Idiomatiques":"idiomes",
    "🔗 Structure & Connecteurs":"connecteurs",
    "🎯 Persuasion & Négociation":"persuasion",
    "⚖️ Rhétorique Juridique":"juridique",
    "🔢 Arsenal Mathématique":"maths",
    "🎭 Figures de Style":"figures",
    "🏛️ Méthode Rhétorique":"methode",
    "📜 Discours Modèle Annoté":"discours",
    "📚 Bibliothèque des Maîtres":"biblio",
    "── CONFIANCE EN SOI ──":"sep",
    "💪 Symptômes & Causes":"coaching_bases",
    "🛠️ Outils & Techniques":"coaching_outils",
    "🎯 Les 8 Missions du Coach":"missions",
    "── GESTION DU STRESS ──":"sep",
    "🔴 Fondements du Stress":"stress_bases",
    "📋 Protocoles Anti-Stress":"stress_protocoles",
    "🧑‍⚕️ Types & Solutions Naturelles":"stress_solutions",
    "── MES DONNÉES ──":"sep",
    "➕ Mes Expressions (Google Sheets)":"remote",
}

choices = [k for k,v in PAGES.items() if not k.startswith("──")]
choice = st.sidebar.radio("Navigation", choices, label_visibility="collapsed")
page = PAGES.get(choice,"accueil")

total = (len(IDIOMES)+len(CONNECTEURS)+len(PERSUASION)+len(JURIDIQUE)+len(MATHS)
         +len(FIGURES)+len(SYMPTOMES)+len(OUTILS_COACH)+len(PROTOCOLES)+len(remote_data))
st.sidebar.markdown("---")
st.sidebar.metric("📦 Ressources totales", total)
st.sidebar.markdown("---")
st.sidebar.info("💡 **Conseil du Pro**\n\nLe silence de 2 secondes avant de répondre donne une impression de maîtrise absolue.")


def sh(icon, titre, sous="", extra=""):
    st.markdown(f'<div class="section-header {extra}"><h2>{icon} {titre}</h2><p>{sous}</p></div>', unsafe_allow_html=True)

def card(col, icon, titre, tag, corps, note=None, sol=None):
    n = f'<p class="ex-box">💡 <b>Exemple :</b> {note}</p>' if note else ""
    s = f'<div class="solution-box">✅ <b>Solution :</b> {sol}</div>' if sol else ""
    st.markdown(f"""<div class="card card-{col}">
        <div class="cat-tag cat-tag-{col}">{icon} {tag}</div>
        <h3 class="card-title">{titre}</h3>
        <p class="sens-text">{corps}</p>{n}{s}
    </div>""", unsafe_allow_html=True)


# ====== PAGES ======

if page == "accueil":
    sh("⚖️","Rosly — Éloquence & Développement","Votre bibliothèque personnelle pour parler avec puissance, confiance et sérénité")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("💬 Expressions",len(IDIOMES)+len(CONNECTEURS)+len(PERSUASION)+len(JURIDIQUE))
    c2.metric("🔢 Concepts Maths",len(MATHS))
    c3.metric("💪 Outils Confiance",len(SYMPTOMES)+len(OUTILS_COACH))
    c4.metric("🔴 Protocoles Stress",len(PROTOCOLES))
    st.markdown("---")
    ca,cb,cc = st.columns(3)
    with ca:
        st.markdown("**🎙️ MAÎTRISER L'ÉLOQUENCE**\n\n- Expressions & Idiomes\n- Structure & Connecteurs\n- Figures de Style\n- Méthode Rhétorique\n- Arsenal Mathématique\n- Bibliothèque des Maîtres")
    with cb:
        st.markdown("**💪 BÂTIR LA CONFIANCE**\n\n- Identifier les symptômes\n- Comprendre les causes profondes\n- Mécanisme interne de succès\n- Visualisation mentale\n- Plan de 5 minutes\n- Questions fécondes\n- Disque rayé")
    with cc:
        st.markdown("**🔴 GÉRER LE STRESS**\n\n- Diète médiatique 7 jours\n- Focusing (Dr Kobasa)\n- Sémantique anti-stress\n- Compte à rebours\n- Technique de compensation\n- Coping (Dr Osten)\n- Effet Zeigarnik")
    st.markdown("""<div class="tip-box">🎯 <b>Comment utiliser cette bibliothèque ?</b><br>
    Commencez par <b>Méthode Rhétorique</b> pour la structure. Puis <b>Figures de Style</b> pour habiller vos arguments. <b>Arsenal Mathématique</b> pour l'autorité intellectuelle. 
    Et <b>Confiance en Soi + Gestion du Stress</b> pour que votre discours s'exprime depuis un état intérieur solide.
    </div>""", unsafe_allow_html=True)

elif page == "idiomes":
    sh("💬","Expressions Idiomatiques","Enrichissez votre registre avec des formules qui marquent les esprits")
    for e in IDIOMES:
        card("blue","💬",e["titre"],f"IDIOME • {e['niveau']}",e["sens"],e["exemple"])

elif page == "connecteurs":
    sh("🔗","Structure & Connecteurs","Les mots qui guident la pensée de votre interlocuteur")
    for e in CONNECTEURS:
        card("teal","🔗",e["titre"],f"{e['usage']} • {e['niveau']}",e["sens"],e["exemple"])

elif page == "persuasion":
    sh("🎯","Persuasion & Négociation","L'art de convaincre sans contraindre")
    for e in PERSUASION:
        card("green","🎯",e["titre"],f"PERSUASION • {e['niveau']}",e["sens"],e["exemple"])

elif page == "juridique":
    sh("⚖️","Rhétorique Juridique","Le vocabulaire du droit pour imposer une autorité irréfutable")
    for e in JURIDIQUE:
        card("red","⚖️",e["titre"],f"JURIDIQUE • {e['niveau']}",e["sens"],e["exemple"])

elif page == "maths":
    sh("🔢","Arsenal Mathématique","Transformez vos opinions subjectives en démonstrations structurelles")
    ss_map = {"🎲 Probabilités":"purple","📊 Statistiques":"teal","🔬 Logique":"blue","⚙️ Systémique":"orange","♟️ Théorie des Jeux":"red","💰 Économie":"green"}
    cur = None
    for e in MATHS:
        ss = e["ss"]
        if ss != cur:
            cur = ss
            st.markdown(f"### {ss}")
        col = ss_map.get(ss,"blue")
        f_html = f'<p style="font-family:monospace;background:#F3F4F6;padding:6px 12px;border-radius:6px;color:#374151;font-size:0.88em;">∑ {e["formule"]}</p>'
        st.markdown(f"""<div class="card card-{col}">
            <div class="cat-tag cat-tag-{col}">{ss} • {e['niveau']}</div>
            <h3 class="card-title">{e['titre']}</h3>
            <p class="sens-text">{e['sens']}</p>{f_html}
            <p class="ex-box">💡 <b>Exemple :</b> {e['exemple']}</p>
        </div>""", unsafe_allow_html=True)

elif page == "figures":
    sh("🎭","Figures de Style","La forme donne de la force au fond — maîtrisez les outils du style")
    colors = ["blue","gold","green","red","purple"]
    for i,f in enumerate(FIGURES):
        col = colors[i % len(colors)]
        st.markdown(f"""<div class="card card-{col}">
            <div class="cat-tag cat-tag-{col}">🎭 FIGURE • {f['niveau']}</div>
            <h3 class="card-title">{f['titre']}</h3>
            <p class="sens-text"><b>Définition :</b> {f['definition']}</p>
            <p style="color:#6B7280;font-size:0.88em;"><b>Effet :</b> {f['effet']}</p>
            <p class="ex-box">📌 <b>Simple :</b> {f['ex_simple']}</p>
            <p class="ex-box" style="border-left-color:#B8860B;background:#FFFBEB;">🌟 <b>Avancé :</b> {f['ex_avance']}</p>
            <div class="tip-box" style="margin-top:10px;font-size:0.88em;">💡 {f['conseil']}</div>
        </div>""", unsafe_allow_html=True)

elif page == "methode":
    sh("🏛️","Méthode Rhétorique Classique","La structure aristotélicienne adaptée au monde professionnel moderne")
    st.markdown("### 📐 Les 5 Étapes du Discours")
    steps = [
        ("1. L'EXORDE","L'Accroche — Ethos","Établir votre légitimité et capter immédiatement l'attention. Un exorde raté = un discours perdu.","Commencez par un fait saisissant, une question ou une prétérition.","'En tant qu'ingénieur ayant géré dix crises réseau majeures...'","blue"),
        ("2. LA NARRATION","Les Faits — Objectivité","Exposé des faits devant paraître objectif et incontestable.","Utilisez 'il est constant que', 'force est de constater'. Restez factuel.","'Force est de constater que depuis 6 mois, notre taux d'indisponibilité a augmenté de 40%.'","teal"),
        ("3. LA CONFIRMATION","La Preuve — Logos","Cœur du discours. Démontrez votre thèse avec vos outils logiques et mathématiques.","Insérez espérance mathématique, analyse de sensibilité, coût d'opportunité.","'L'espérance mathématique de l'investissement préventif est positive dans 87% des scénarios.'","green"),
        ("4. LA RÉFUTATION","Anticiper les Objections","Détruire les contre-arguments AVANT qu'ils ne soient formulés.","Introduisez l'objection adverse vous-même, puis démontrez-en la limite.","'Certains diront que le coût est prohibitif. Certes — mais le coût d'inaction est supérieur.'","orange"),
        ("5. LA PÉRORAISON","La Conclusion — Pathos","La conclusion émotionnelle qui pousse à l'action. Le Pathos entre en scène.","Utilisez une anaphore puissante, une clausule mémorable.","'Car le véritable risque est le sacrifice de notre avenir sur l'autel de notre confort présent.'","red"),
    ]
    for step in steps:
        st.markdown(f"""<div class="card card-{step[5]}">
            <div class="cat-tag cat-tag-{step[5]}">{step[0]}</div>
            <h3 class="card-title">{step[1]}</h3>
            <p class="sens-text">{step[2]}</p>
            <p class="ex-box">📌 <b>Formule :</b> {step[3]}</p>
            <p class="ex-box" style="border-left-color:#B8860B;background:#FFFBEB;">💬 {step[4]}</p>
        </div>""", unsafe_allow_html=True)
    st.markdown("---\n### ⚡ Les 3 Leviers de Persuasion")
    c1,c2,c3 = st.columns(3)
    leviers = [("🏛️","ETHOS — La Crédibilité","Votre autorité morale et professionnelle. Ce que vous êtes, ce que vous avez vécu.","Citez votre expérience concrète. Adoptez un ton grave et posé.","'En tant que responsable de la cellule NOC depuis 5 ans...'"),
               ("🔬","LOGOS — La Logique","La démonstration rationnelle. Les chiffres, les faits, les raisonnements logiques.","Utilisez les concepts scientifiques, les statistiques. Quantifiez.","'L'analyse de sensibilité démontre que même avec 15% d'écart, le ROI reste positif.'"),
               ("❤️","PATHOS — L'Émotion","L'appel aux émotions. Rappeler ce qui est en jeu pour les personnes concernées.","Utilisez l'hypotypose. Reliez le sujet technique à son impact humain.","'Imaginez l'impact sur nos équipes terrain, sur leur sécurité, sur nos clients.'")]
    for col_ui, lev in zip([c1,c2,c3], leviers):
        with col_ui:
            st.markdown(f"""<div class="card card-blue" style="text-align:center;">
                <div style="font-size:2.5em;">{lev[0]}</div>
                <h3 class="card-title">{lev[1]}</h3>
                <p class="sens-text">{lev[2]}</p>
                <p style="color:#6B7280;font-size:0.85em;">{lev[3]}</p>
                <p class="ex-box">{lev[4]}</p>
            </div>""", unsafe_allow_html=True)

elif page == "discours":
    sh("📜","Discours Modèle Annoté","Une démonstration de force oratoire complète, analysée pas à pas")
    st.markdown("""<div class="discourse-card">
        <h3>🎤 L'Impératif de la Mutation</h3>
        <p style="color:#A08040;font-size:0.88em;margin-bottom:20px;">📌 Simulation d'une intervention en comité de direction. Fusion Logos (mathématique) + Ethos + Pathos (rhétorique française).</p>
        <div class="discourse-body">
        « Messieurs, Mesdames, je ne m'étendrai pas ici sur les succès passés qui, bien que glorieux, appartiennent désormais à une <b>régression vers la moyenne</b> que nous ne pouvons plus ignorer. <em>[PRÉTÉRITION + LOGOS]</em><br><br>
        Regardez notre organisation : sans une impulsion nouvelle, <b>l'entropie</b> fait son œuvre, transformant notre agilité d'hier en une inertie bureaucratique qui nous consume. <em>[HYPOTYPOSE + LOGOS]</em> Certes, certains prônent la prudence ; mais la prudence est une <b>condition nécessaire, mais non suffisante</b> à la survie d'un leader. <em>[ANTITHÈSE + LOGOS]</em> Si nous suivions la logique de l'immobilisme jusqu'au bout, nous arriverions à admettre que pour ne pas couler, il suffirait de ne plus naviguer : c'est une absurdité que nos parts de marché démentent déjà. <em>[RAISONNEMENT PAR L'ABSURDE]</em><br><br>
        Il nous faut aujourd'hui briser ce <b>dilemme du prisonnier</b> qui nous paralyse face à la concurrence.<br>
        Il nous faut redéfinir notre <b>espace vectoriel des possibles</b>.<br>
        Il nous faut, enfin, agir avant que le <b>point de bascule</b> ne rende toute décision caduque. <em>[ANAPHORE]</em><br><br>
        Au-delà des chiffres, c'est une question de vision. Car en dernière analyse, le véritable risque n'est pas celui de l'échec technique, mais bien le <b>coût d'opportunité</b> de notre indécision : le sacrifice de notre avenir sur l'autel de notre confort présent. Choisissons la mutation, car dans cet <b>intervalle de confiance</b> où se joue notre destin, seule l'audace est statistiquement souveraine. » <em>[PATHOS + CLAUSULE]</em>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown("### 🔬 Analyse Structurelle")
    annots = [("EXORDE (Ethos)","Prétérition pour rappeler le passé sans y rester coincé. Établit la crédibilité.","gold"),
              ("NARRATION (Logos)","Entropie, régression vers la moyenne — des lois quasi-physiques pour prouver l'urgence.","teal"),
              ("RÉFUTATION","'Nécessaire mais non suffisante' anticipe et disqualifie l'objection adverse.","orange"),
              ("ANAPHORE","'Il nous faut... Il nous faut... Il nous faut...' — rythme de marteau.","blue"),
              ("PÉRORAISON (Pathos)","Le coût d'opportunité et le sacrifice de l'avenir provoquent un sentiment d'urgence morale.","red"),
              ("CLAUSULE","Dernier mot : 'souveraine'. Fort, mémorable, inattendu.","purple")]
    for a_titre,a_detail,a_col in annots:
        card(a_col,"🔬",a_titre,"TECHNIQUE",a_detail)

elif page == "biblio":
    sh("📚","Bibliothèque des Maîtres","Les ouvrages fondamentaux pour maîtriser l'art de convaincre")
    st.markdown("""<div class="tip-box">📖 <b>Combo recommandé :</b> Commencez par <b>Schopenhauer</b> (le combat), puis <b>Cicéron</b> (la structure), et terminez par <b>Cialdini</b> (la psychologie moderne).</div>""", unsafe_allow_html=True)
    for l in BIBLIOTHEQUE:
        st.markdown(f"""<div class="book-card">
            <div class="cat-tag" style="color:#B8860B;">📚 {l['objectif']}</div>
            <h3 style="margin:8px 0 4px;font-family:'Playfair Display',serif;">{l['ouvrage']}</h3>
            <p style="color:#6B7280;font-size:0.9em;margin:0 0 12px;">par <b>{l['auteur']}</b></p>
            <p style="color:#374151;line-height:1.7;">{l['description']}</p>
            <div style="display:flex;gap:16px;margin-top:14px;flex-wrap:wrap;">
                <div class="tip-box" style="flex:1;min-width:200px;padding:10px 14px;font-size:0.85em;">👤 <b>Pour qui :</b> {l['pour_qui']}</div>
                <div style="padding:10px 14px;background:#FFFBEB;border:1px solid #FDE68A;border-radius:8px;flex:1;min-width:160px;font-size:0.85em;color:#92400E;">{l['niveau']}</div>
            </div>
        </div>""", unsafe_allow_html=True)

# ====== COACHING ======

elif page == "coaching_bases":
    sh("💪","Confiance en Soi — Symptômes & Causes","Identifier pour mieux agir","coach-header")
    st.markdown(f"""<div class="warning-box">📊 <b>Chiffre Clé :</b> 40% des personnes dans le monde manquent de confiance en elles, quel que soit leur milieu culturel. (Étude américaine — Master Coach en développement personnel)</div>""", unsafe_allow_html=True)
    st.markdown("### 🔍 Les 4 Symptômes Principaux")
    col_s = ["red","orange","purple","teal"]
    for i,s in enumerate(SYMPTOMES):
        col = col_s[i%4]
        st.markdown(f"""<div class="card card-{col}">
            <div class="cat-tag cat-tag-{col}">🔍 SYMPTÔME #{i+1}</div>
            <h3 class="card-title">{s['titre']}</h3>
            <p class="sens-text">{s['description']}</p>
            <p class="ex-box">💬 <b>Exemple :</b> {s['exemple']}</p>
            <div class="solution-box">✅ <b>Solution :</b> {s['solution']}</div>
            <p style="color:#DC2626;font-size:0.85em;margin-top:8px;">⚠️ {s['alerte']}</p>
        </div>""", unsafe_allow_html=True)
    st.markdown("---\n### 🌱 Les 7 Causes Profondes")
    for cause in CAUSES:
        st.markdown(f"""<div class="card card-blue" style="border-left-color:#6B7280;">
            <div class="cat-tag" style="color:#6B7280;">CAUSE PROFONDE</div>
            <h3 class="card-title">{cause['cause']}</h3>
            <p class="sens-text">{cause['detail']}</p>
        </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="key-box">
        <h3 style="color:#F5DEB3;margin-top:0;">🔑 Principe Fondamental</h3>
        <p style="color:#EDE0C8;line-height:1.8;">La confiance est une compétence qui s'apprend, se cultive et se renforce. Le manque de confiance en soi, c'est simplement <b>avoir peur</b>. La question clé à poser au coaché : <b>'Vous avez peur de quoi précisément ?'</b></p>
    </div>""", unsafe_allow_html=True)

elif page == "coaching_outils":
    sh("🛠️","Confiance en Soi — Outils & Techniques","Les protocoles concrets pour reconstruire la confiance","coach-header")
    tool_cols = ["green","blue","teal","purple","orange","red","gold"]
    for i,t in enumerate(OUTILS_COACH):
        col = tool_cols[i%len(tool_cols)]
        st.markdown(f"""<div class="card card-{col}">
            <div class="cat-tag cat-tag-{col}">🛠️ OUTIL #{i+1}</div>
            <h3 class="card-title">{t['titre']}</h3>
            <p class="sens-text">{t['description']}</p>
            <div style="background:#F8FAFC;padding:14px;border-radius:8px;margin:10px 0;border-left:3px solid #CBD5E1;">
                <b>📋 Protocole :</b><br>{t['protocole'].replace(chr(10),'<br>')}
            </div>
            <p class="ex-box">🎯 <b>Quand l'utiliser :</b> {t['quand']}</p>
        </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="tip-box">💡 <b>Citation fondatrice (Dr Georgi Lozanov) :</b><br>
    <em>'Réfléchir et repenser à un problème passé est le plus sûr moyen de le reproduire à l'identique.'</em><br>
    <b>Et son corollaire (la bonne nouvelle) :</b> <em>'Le souvenir de nos réussites passées est une source de confiance que nous pouvons activer à volonté.'</em></div>""", unsafe_allow_html=True)

elif page == "missions":
    sh("🎯","Les 8 Missions du Coach","Le cadre d'intervention professionnelle","coach-header")
    for m in MISSIONS_COACH:
        st.markdown(f"""<div class="card card-green">
            <div class="cat-tag cat-tag-green">🎯 MISSION {m['num']}</div>
            <h3 class="card-title">{m['titre']}</h3>
            <p class="sens-text">{m['detail']}</p>
        </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="tip-box">📋 <b>Après chaque session :</b> Envoyer par email un compte-rendu des points-forts. Cela aide le coaché à ancrer les apprentissages et appliquer les conseils entre les sessions.</div>""", unsafe_allow_html=True)

# ====== STRESS ======

elif page == "stress_bases":
    sh("🔴","Gestion du Stress — Fondements","Comprendre le stress pour ne plus le subir","stress-header")
    for fond in STRESS_FONDEMENTS:
        st.markdown(f"""<div class="card card-red">
            <div class="cat-tag cat-tag-red">🔴 FONDEMENT</div>
            <h3 class="card-title">{fond['titre']}</h3>
            <p class="sens-text">{fond['description']}</p>""", unsafe_allow_html=True)
        if "fonctions" in fond:
            for f in fond["fonctions"]:
                st.markdown(f"<p style='margin:4px 0 4px 16px;color:#374151;'>{f}</p>",unsafe_allow_html=True)
        if "chiffre" in fond:
            st.markdown(f"<p class='ex-box'>📊 {fond['chiffre']}</p>",unsafe_allow_html=True)
        if "question" in fond:
            st.markdown(f"<p class='ex-box'>❓ {fond['question']}</p>",unsafe_allow_html=True)
        if "consequence" in fond:
            st.markdown(f"<p class='ex-box'>⚠️ {fond['consequence']}</p>",unsafe_allow_html=True)
        if "solution" in fond:
            st.markdown(f"<div class='solution-box'>✅ {fond['solution']}</div>",unsafe_allow_html=True)
        st.markdown("</div>",unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""<div class="key-box">
        <h3 style="color:#F5DEB3;margin-top:0;">🧬 L'Expérience des Rats — La Révolution</h3>
        <p style="color:#EDE0C8;line-height:1.9;">
        Deux groupes de rats reçoivent des décharges électriques. Le premier groupe n'a aucun contrôle. Le deuxième peut appuyer sur un bouton pour réduire l'intensité — mais ne l'utilise pas toujours.<br><br>
        Résultat : le premier groupe développe tous les symptômes du stress chronique (ulcères, troubles cardiaques, insomnies). Le deuxième groupe : <b>quasiment aucun symptôme</b>, malgré le même nombre de décharges.<br><br>
        La conclusion : ce n'est pas le stress qui est nocif. C'est l'<b>absence de sentiment de contrôle</b> sur la situation. Dès que l'on a conscience qu'on peut — même partiellement — agir, les effets négatifs du stress disparaissent.
        </p>
        <p style="color:#B8860B;font-weight:700;font-size:1.1em;">"Le stress n'est rien. Sa gestion est tout."</p>
    </div>""", unsafe_allow_html=True)
    st.markdown("---\n### 📊 Les 3 Types de Stressés")
    c1,c2,c3 = st.columns(3)
    for col_ui,t in zip([c1,c2,c3],TYPES_STRESSES):
        with col_ui:
            st.markdown(f"""<div class="card card-{t['col']}">
                <h3 class="card-title">{t['type']}</h3>
                <p class="sens-text">{t['desc']}</p>
                <div class="tip-box" style="font-size:0.85em;padding:10px;margin-top:10px;">{t['attention']}</div>
            </div>""",unsafe_allow_html=True)

elif page == "stress_protocoles":
    sh("📋","Gestion du Stress — Protocoles","Les outils concrets pour reprendre le contrôle","stress-header")
    cols_p = ["red","orange","purple","green","teal","blue","gold","red","orange","purple","green"]
    for i,p in enumerate(PROTOCOLES):
        col = cols_p[i%len(cols_p)]
        extras = ""
        if "avantages" in p:
            avs = "".join([f"<p style='margin:4px 0 4px 16px;color:#14532D;font-size:0.9em;'>✅ {a}</p>" for a in p["avantages"]])
            extras += f"<div class='solution-box' style='margin-top:10px;'>{avs}</div>"
        st.markdown(f"""<div class="card card-{col}">
            <div class="cat-tag cat-tag-{col}">📋 PROTOCOLE #{i+1}</div>
            <h3 class="card-title">{p['titre']}</h3>
            <p class="sens-text">{p['description']}</p>
            <div style="background:#F8FAFC;padding:14px;border-radius:8px;margin:10px 0;border-left:3px solid #CBD5E1;">
                <b>📋 Protocole :</b><br>{p['protocole'].replace(chr(10),'<br>')}
            </div>{extras}
        </div>""",unsafe_allow_html=True)

elif page == "stress_solutions":
    sh("🧑‍⚕️","Gestion du Stress — Types & Solutions Naturelles","Compléments et ressources supplémentaires","stress-header")
    st.markdown("### 🌿 Solutions Naturelles Anti-Stress")
    for s in SOLUTIONS_NAT:
        card("green","🌿",s["sol"],"SOLUTION NATURELLE",s["desc"])
    st.markdown("---")
    st.markdown("""<div class="tip-box">
    <b>💊 Remèdes homéopathiques de fond (Dr Michel Galobardès) :</b><br>
    • <b>Gelsemium 30 CH</b> → Semaine 1 &nbsp; • <b>Arsenicum album 30 CH</b> → Semaine 2 &nbsp; • <b>Pulsatilla 30 CH</b> → Semaine 3<br>
    • <b>Phosphorus 5 ou 7 CH</b> → Pour les caractères explosifs (Type A) : 3 granules 2x/jour.<br>
    <em>Ces remèdes agissent sur le comportement, non sur les faits stressants. Toujours consulter un médecin pour les dosages.</em>
    </div>""",unsafe_allow_html=True)
    st.markdown("---\n### 🧘 Les 5 Grands Principes Anti-Stress")
    principes = [
        ("1️⃣ Le stress est un AMI","Il vous fournit de l'énergie supplémentaire. Changez de perspective : 'J'ai de l'adrénaline → je vais être meilleur dans cette situation.'"),
        ("2️⃣ AGIR consomme l'adrénaline","Le seul moyen de transformer le mauvais stress en bon stress : agir immédiatement. L'attente aggrave systématiquement."),
        ("3️⃣ 99% du temps, tout va bien","Prenez conscience de cela chaque jour. Le cerveau reptilien extrapole sur 1% des situations. Le néocortical vit dans le présent réel."),
        ("4️⃣ Vos mots créent votre stress","Réduire la charge émotionnelle de votre vocabulaire = réduire votre stress quasi instantanément. 'Désastre' → 'Problème'."),
        ("5️⃣ Reprendre le contrôle","45 minutes d'activité choisie librement chaque jour = sentiment de contrôle = protection contre les effets négatifs du stress."),
    ]
    for titre_p,desc_p in principes:
        card("orange","⚡",titre_p,"PRINCIPE FONDAMENTAL",desc_p)

elif page == "remote":
    sh("➕","Mes Expressions Personnelles","Expressions chargées depuis votre Google Sheets personnel")
    if remote_data:
        st.success(f"✅ {len(remote_data)} expression(s) chargée(s) depuis Google Sheets")
        for exp in remote_data:
            cat = str(exp.get("catégorie","Général")).strip()
            card("teal","📎",exp.get("titre","Expression"),cat,
                 exp.get("sens","Définition non renseignée"),
                 exp.get("exemple","Aucun exemple disponible."))
    else:
        st.warning("⚠️ Aucune donnée distante chargée. Vérifiez que votre Google Sheet est public.")
        st.markdown("**Structure attendue :** colonnes `catégorie`, `titre`, `sens`, `exemple`")
