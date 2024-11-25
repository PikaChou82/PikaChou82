import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Mon appikachou 3", page_icon=":bar_chart:")

st.markdown("<h1 style='color:darkblue; font-family:Arial; font-size:50px;'>Bienvenue sur l'autre site Web de PikaChou82</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("On va commencer par choisir un jeu de données à regarder :")

# Chargement de datasets
titanic = sns.load_dataset('titanic')
car_crashes = sns.load_dataset('car_crashes')
flights = sns.load_dataset('flights')
healthexp = sns.load_dataset('healthexp')

datasets = {
    'titanic': titanic,
    'car_crashes': car_crashes,
    'flights': flights,
    'healthexp': healthexp
}

Analyse = {
    'titanic': "le Titanic",
    'car_crashes': "les accidents de voiture",
    'flights': "les statistiques de vol",
    'healthexp': "les statistiques santé par pays"
}

selection = st.selectbox("Choix du dataset", list(datasets))

selected_dataset = datasets[selection]
st.dataframe(selected_dataset)

st.write(f"Super ! Bravo pour ce choix, moi aussi je veux en savoir plus sur {Analyse[selection]} !")
x = st.selectbox("Choix de la colonne X :", list(selected_dataset.columns))
y = st.selectbox("Choix de la colonne Y :", list(selected_dataset.columns))

st.write("Bingo ! Tu sais ce que tu veux ! Plus qu'une question et on va pouvoir entrer dans le vif du sujet ;)")
graph = st.selectbox("Choix du Graphique : ", ["scatter_chart","bar_chart","line_chart"])

type_graph = {"scatter_chart" : "", "bar_chart" : "" , "line_chart" : ""}

Titre = "Graphique "+ type_graph[graph] + " sur l'analyse de données concernant " +Analyse[selection]
Axe_X = x
Axe_Y = y


# Création de la figure du graphique
fig, ax = plt.subplots()

if graph == 'scatter_chart':
    sns.scatterplot(data = selected_dataset, x = x, y = y)
elif graph == 'bar_chart':
    sns.barplot(data = selected_dataset, x = x, y = y)
else:
    sns.lineplot(data = selected_dataset, x = x, y = y)

plt.xlabel(Axe_X, size = 10, c = '#5D615B', fontweight = 'bold')
plt.ylabel(Axe_Y, size = 10, c = '#5D615B', fontweight = 'bold')
plt.title(Titre, color = "darkblue", fontweight = 'bold', size = 20)
st.pyplot(fig)

