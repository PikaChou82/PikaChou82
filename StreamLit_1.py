import streamlit as st
import pandas as pd
from datetime import date,time
import seaborn as sns

# Load the dataset
taxis_df = sns.load_dataset('taxis')

st.set_page_config(page_title="Mon appikachou", page_icon=":bar_chart:")



st.markdown("<h1 style='color:darkblue; font-family:Arial; font-size:50px;'>Bienvenue sur le site Web de PikaChou82</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
arrondissement = st.selectbox("Indiquez votre arrondissement de récupération",
list(taxis_df['pickup_borough'].unique()))

st.markdown(f"<p style='color:darkblue; font-family:Arial; font-size:20px;'>Tu as choisi {arrondissement}</p>", unsafe_allow_html=True)

st.image(str(arrondissement)+".png")
