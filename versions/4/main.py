# streamlit prep
import streamlit as st

if "username" not in st.session_state:
    st.session_state.username = ""

def logout():
    if st.button("Log out"):
        st.session_state.username = ""
        st.session_state.memory.clear()
        st.rerun()


login_page = st.Page("login.py", title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
home_page = st.Page("home.py", title="Home", icon=":material/home:")

if st.session_state.username:
    pg = st.navigation(
        {
            "Home": [home_page, logout_page],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
