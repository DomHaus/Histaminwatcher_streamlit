import streamlit as st
import pandas as pd

data_path = "Ressources/data1.csv"

def load_data():
    df = pd.read_csv(data_path, delimiter=";", encoding="utf-8")
    return df

def save_data(df):
    df.to_csv(data_path, sep=";", index=False, encoding="utf-8")

def add_row(data, new_row):
    new_index = len(data)
    data.loc[new_index] = new_row
    return data

data = load_data()

st.title("Lebensmittel hinzufügen:")

with st.form(key='add_row_form'):
    zutat_input = st.text_input('Zutat')
    vertraeglichkeit_input = st.text_input('Verträglichkeit von 0 bis 3 (0 = sehr gut)')
    anmerkungen_input = st.text_input('Anmerkungen (Text)')
    eigene_wertung_input = st.text_input('Eigene Wertung')
    histamin_input = st.text_input('Histamin ("H" oder "H!")')
    kaloriengehalt_input = st.text_input('Kaloriengehalt (Niedrig bis 100kcal, Mittel bis 300kcal, hoch über 300kcal auf 100g)')
    andere_amine_input = st.text_input('Andere Amine (A)')
    blocker_input = st.text_input('Blocker (B)')

    submit_button = st.form_submit_button('Hinzufügen')

if submit_button:
    new_row = {
        'Zutat': zutat_input,
        'Verträglichkeit': vertraeglichkeit_input,
        'Anmerkungen': anmerkungen_input,
        'Eigene Wertung': eigene_wertung_input,
        'Histamin': histamin_input,
        'Kaloriengehalt': kaloriengehalt_input,
        'Andere Amine': andere_amine_input,
        'Blocker': blocker_input
    }
    data = add_row(data, new_row)
    save_data(data)
    st.success("Eintrag hinzugefügt!")