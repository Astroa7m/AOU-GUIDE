import json

import streamlit as st
from helpers import convert_dict_to_formatted_string
from fake_auth import authenticate_user

st.title("AOU Guide")
st.write("Your all-in-one AI companion in AOU Oman")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
# login inputs
# if button clicked
st.session_state.user = None
if st.button("Login"):
    user = authenticate_user(username, password)
    print("Checking credentials")
    print(user)
    if user != None:
        st.session_state.username = user['title'] + user['name'].split()[-1]
        st.session_state.user = convert_dict_to_formatted_string(user)
        print(type(st.session_state.user))
        print(st.session_state.username)
        st.rerun()
    else:
        st.title("wrong")
