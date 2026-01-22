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
    (0, int(df["age"].max()))
)

filtered_df = df[
    (df["sex"].isin(sex)) &
    (df["pclass"].isin(pclass)) &
    (df["age"].between(age_range[0], age_range[1]))
]
st.divider()
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
st.divider()
st.plotly_chart(fig)
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.subheader("Podstawowe statystyki dla grupy kobiet")
    st.write(filtered_df[filtered_df["sex"] == "female"]["age"].describe())

with col2:
    st.subheader("Podstawowe statystyki dla grupy mężczyzn")
    st.write(filtered_df[filtered_df["sex"] == "male"]["age"].describe())


st.divider()

sex_survival = (
    df
    .groupby(["sex", "survived"])
    .size()
    .reset_index(name="Liczba")
)

sex_survival["Płeć"] = sex_survival["sex"].map({"female": "Kobiety", "male": "Mężczyźni"})
sex_survival["Status"] = sex_survival["survived"].map({0: "Nie przeżył", 1: "Przeżył"})

fig_sex = px.bar(
    sex_survival,
    x="Płeć",
    y="Liczba",
    color="Status",
    barmode="stack",
    text="Liczba",
    title="Przeżywalność pasażerów wg płci"
)

st.plotly_chart(fig_sex)

