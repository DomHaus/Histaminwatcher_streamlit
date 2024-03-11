import streamlit as st
import pandas as pd
from st_pages import show_pages_from_config
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

#---- AUTH PROCESS ----

with open('.streamlit/creds.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

name, authentication_status, username = authenticator.login('main')

if not authentication_status:
    st.error("Username / Passwort ist falsch!")

if authentication_status is None:
    st.warning("Bitte Benutzername / Passwort eingeben!")

if authentication_status:

    data_path = "Ressources/data1.csv"

    show_pages_from_config()
    def load_data():
        df = pd.read_csv(data_path, delimiter=";", encoding="utf-8")
        return df


    def save_data(df):
        df.to_csv(data_path, sep=";", index=False, encoding="utf-8")


    data = load_data()

    st.header("Suchen & bearbeiten:")

    txt_search = st.text_input("Suche nach Zutat / Lebensmittel")

    if txt_search:
        filtered_data = data[data["Zutat"].str.contains(txt_search, case=False)]

        if not filtered_data.empty:
            for index, entry in filtered_data.iterrows():
                with st.expander(f"{entry['Zutat']}"):
                    with st.form(key=f'edit_form_{index}'):
                        vertraeglichkeit_input = st.text_input('Verträglichkeit (0 bis 3)', value=entry['Verträglichkeit'])
                        anmerkungen_input = st.text_input('Anmerkungen (Text)', value=entry['Anmerkungen'])
                        eigene_wertung_input = st.text_input('Eigene Wertung', value=entry['Eigene Wertung'])
                        histamin_input = st.text_input('Histamin ("H" oder "H!")', value=entry['Histamin'])
                        kaloriengehalt_input = st.text_input('Kaloriengehalt (Niedrig bis 100kcal, Mittel bis 300kcal, hoch über 300kcal auf 100g)', value=entry['Kaloriengehalt'])
                        andere_amine_input = st.text_input('Andere Amine (A)', value=entry['Andere Amine'])
                        blocker_input = st.text_input('Blocker (B)', value=entry['Blocker'])

                        submit_button = st.form_submit_button('Speichern')

                        if submit_button:
                            # Update the DataFrame with edited values
                            data.loc[index, 'Verträglichkeit'] = vertraeglichkeit_input
                            data.loc[index, 'Anmerkungen'] = anmerkungen_input
                            data.loc[index, 'Eigene Wertung'] = eigene_wertung_input
                            data.loc[index, 'Histamin'] = histamin_input
                            data.loc[index, 'Kaloriengehalt'] = kaloriengehalt_input
                            data.loc[index, 'Andere Amine'] = andere_amine_input
                            data.loc[index, 'Blocker'] = blocker_input

                            # Save the updated DataFrame
                            save_data(data)

                            st.success("Änderungen gespeichert!")
                            st.write("Values saved:")
                            st.write("Verträglichkeit:", vertraeglichkeit_input)
                            st.write("Anmerkungen:", anmerkungen_input)
                            st.write("Eigene Wertung:", eigene_wertung_input)
                            st.write("Histamin:", histamin_input)
                            st.write("Kaloriengehalt:", kaloriengehalt_input)
                            st.write("Andere Amine:", andere_amine_input)
                            st.write("Blocker:", blocker_input)
        else:
            st.write("Keine Ergebnisse gefunden.")

    st.header("Alle Daten ansehen:")
    st.dataframe(data)
