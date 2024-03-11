import streamlit_authenticator as stauth

hashedpw = stauth.Hasher("HIER PASSWORT").generate()
print(hashedpw)

#After printing, add the password and user to the creds yaml