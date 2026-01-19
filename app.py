import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.title("Interaktywna analiza danych – Titanic")

df = sns.load_dataset("titanic")

st.subheader("Podgląd danych")
st.dataframe(df.head())

st.sidebar.header("Filtry")

sex = st.sidebar.multiselect(
    "Płeć",
    options=df["sex"].dropna().unique(),
    default=df["sex"].dropna().unique()
)

pclass = st.sidebar.multiselect(
    "Klasa",
    options=df["pclass"].unique(),
    default=df["pclass"].unique()
)

age_range = st.sidebar.slider(
    "Zakres wieku",
    int(df["age"].min()),
    int(df["age"].max()),
    (10, 60)
)

filtered_df = df[
    (df["sex"].isin(sex)) &
    (df["pclass"].isin(pclass)) &
    (df["age"].between(age_range[0], age_range[1]))
]

st.subheader("Dane po filtracji")
st.write(f"Liczba obserwacji: {len(filtered_df)}")
st.dataframe(filtered_df)

survival_stats = (
    filtered_df["survived"]
    .value_counts()
    .rename(index={0: "Nie przeżył", 1: "Przeżył"})
    .reset_index()
)

survival_stats.columns = ["Status", "Liczba"]

fig = px.bar(
    survival_stats,
    x="Status",
    y="Liczba",
    title="Przeżywalność pasażerów",
    text="Liczba"
)

st.plotly_chart(fig)

st.subheader("Podstawowe statystyki wieku")
st.write(filtered_df["age"].describe())
