import streamlit as st

# Configuration
st.set_page_config(page_title="L'Art de l'Éloquence", page_icon="⚖️")

# Menu sur le côté
menu = ["Expressions Idiomatiques", "Rhétorique & Droit", "Convaincre", "Physique & Santé"]
choix = st.sidebar.selectbox("Menu", menu)

st.title(f"📚 {choix}")

if choix == "Expressions Idiomatiques":
    st.info("Avoir l'apanage de : Posséder un privilège exclusif.")
    st.info("Sortir de ses gonds : Perdre son sang-froid.")
    st.info("Victoire à la Pyrrhus : Succès trop coûteux.")
    st.info("Céder aux sirènes : Se laisser séduire par un danger.")

elif choix == "Rhétorique & Droit":
    st.success("**En l'espèce** : Dans ce cas précis.")
    st.success("**A fortiori** : À plus forte raison.")
    st.warning("*Fraus omnia corrumpit* (La fraude corrompt tout)")

elif choix == "Convaincre":
    st.write("- **Le statu quo n'est plus une option**")
    st.write("- **Générer une valeur ajoutée immédiate**")

elif choix == "Physique & Santé":
    st.error("U = R · I (Loi d'Ohm)")
    st.write("Respectez votre 'résistance' interne pour éviter la surchauffe !")
