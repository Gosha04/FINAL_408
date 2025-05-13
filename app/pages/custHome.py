import streamlit as st

st.set_page_config(page_title = "Customer Home", page_icon = "🏠", layout = "wide")

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

    if st.button("Home"):
        st.switch_page("pages/custHome.py")

    if st.button("Find a Dealer"):
        st.switch_page("pages/dealerFinder.py")

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

st.write("")

st.write(f"Your customer id: {st.session_state["user"]["id"]}")

sales_col, rentals_col, work_orders_col = st.columns(3, border = True)

with sales_col:
    st.subheader("Purchases", divider = "gray")

    # purchase logic

with rentals_col:
    st.subheader("Rentals", divider = "gray")

    # rental logic

with work_orders_col:
    st.subheader("Work Orders", divider = "gray")

    # work order logic