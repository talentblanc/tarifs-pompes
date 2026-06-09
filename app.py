import streamlit as st

st.set_page_config(page_title="Gestion Gamme YOSHIMI", page_icon="🚰", layout="centered")

st.title("📋 Catalogue & Tarifs Hors Taxe")
st.write("Marque : **YOSHIMI** | Certification : **Standard Europe CE**")

# Liste finale des produits et tarifs DA HT
produits = {
    "Pompe APM37": 5200,
    "Pompe APM30": 4500,
    "Pompe Jet 100": 14200,
    "Pompe à deux turbines": 12200,
    "Pompe à trois turbines": 14000,
    "Pompe à quatre turbines": 16500,
    "Pompe à cinq turbines": 19000,
    "Pompe submersible V2200F": 34000,
    "Pompe submersible V1500F": 38000,
    "Pompe submersible V750F": 42000,
    "Pompe PW750": 20000,
    "Pompe PCM158": 14200,
    "Servo-presse contrôle modèle PC10": 4500,
    "Presse-contrôle modèle EPC1": 3300,
    "Cassette de servo modèle PC10": 1750,
    "Cassette de servo modèle EPC1": 1950,
    "Carte mère servo standard": 1000
}

st.subheader("Liste Intégrale des Tarifs (DA HT)")
for nom, prix in produits.items():
    st.write(f"🔹 **{nom}** : `{prix:,} DA`".replace(",", " "))
