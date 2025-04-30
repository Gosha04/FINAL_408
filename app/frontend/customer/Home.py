import streamlit as st
from . import Purchases, Rentals, WorkOrders

PAGES = {
    "Appointments": Purchases,
    "Service History": Rentals,
    "Support": WorkOrders
}

def app(user):
    if "customer_page" not in st.session_state:
        st.session_state.customer_page = "Home"

    # Sidebar navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio(
        "Go to",
        list(PAGES.keys()),
        index=list(PAGES.keys()).index(st.session_state.customer_page)
    )

    # Update selected page
    st.session_state.customer_page = selection

    # Render the selected page
    page = PAGES[selection]
    page.app(user)