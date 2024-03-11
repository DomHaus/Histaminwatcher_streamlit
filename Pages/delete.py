import streamlit as st
import pandas as pd

data_path = "Ressources/data1.csv"


def load_data():
    df = pd.read_csv(data_path, delimiter=";", encoding="utf-8")
    return df


def save_data(df):
    df.to_csv(data_path, sep=";", index=False, encoding="utf-8")


def delete_entry(data, index):
    data = data.drop(index, axis=0).reset_index(drop=True)
    return data


data = load_data()

st.title("Lebensmittel / Zutat löschen")

txt_search = st.text_input("Suche nach Zutat / Lebensmittel")

if txt_search:
    filtered_data = data[data["Zutat"].str.contains(txt_search, case=False)]

    if not filtered_data.empty:
        for index, entry in filtered_data.iterrows():
            with st.expander(f"{entry['Zutat']}"):
                st.write(entry)
                delete_button = st.button("Eintrag löschen")
                if delete_button:
                    data = delete_entry(data, index)
                    save_data(data)
                    st.success("Eintrag erfolgreich gelöscht!")
    else:
        st.write("No results found.")
