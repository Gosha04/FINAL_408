import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Trainee Dashboard", page_icon = "🧑‍🎓", layout = "wide")

st.markdown("""
    <style>
        [data-testid="stSidebarNav"], [data-testid="stSidebarHeader"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        section[data-testid="stSidebar"] button{
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

user = st.session_state["user"]

with st.sidebar:
    if st.button("Log out"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.switch_page("app.py")

    if st.button("Dashboard"):
        st.switch_page("pages/traineeDash.py")

st.markdown("""
            <style>
                .block-container {
                    padding-top: 11px;
                }

                .stColumn {
                    padding-top: 0;
                }
                </style>
        """, unsafe_allow_html=True)

st.title(f"Welcome, {user["first_name"]} {user["last_name"]}!")

usr_id_col, role_col, dealership_col, manager_col = st.columns([4, 4, 3, 15])

with usr_id_col:
    st.write(f"Your employee id: {st.session_state["user"]["id"]}")

with role_col:
    st.write(f"Role: {st.session_state["user"]["type"]}")

with dealership_col:
    st.write(f"Dealership: {st.session_state["user"]["dealershipID"]}")

with manager_col:
    st.write(f"Manager ID: {st.session_state["user"]["manager"]}")

st.subheader("You're a trainee. Report to your manager for further information.")


