import streamlit as st
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

if authentication_status is True:
    st.switch_page("pages/search.py")