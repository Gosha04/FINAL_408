import streamlit as st
import pandas as pd

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

    temp_purchases_data = [("2022", "Subaru", "WRX", 20000, 2), ("2019", "Chevy", "Camaro", 19000, 2)]
    temp_purchases_data_cols = ["Year", "Make", "Model", "Price", "Salesperson ID"]

    temp_purchases_data_df = pd.DataFrame(temp_purchases_data, columns=temp_purchases_data_cols)

    st.dataframe(temp_purchases_data_df, hide_index=True)
    # purchase logic to be returned as dataframe

with rentals_col:
    st.subheader("Rentals", divider = "gray")

    temp_rentals_data = [("2022", "Subaru", "WRX", 20000, 2, "2025-01-01", "Active"), ("2019", "Chevy", "Camaro", 19000, 2, "2025-01-02", "Complete")]
    temp_rentals_data_cols = ["Year", "Make", "Model", "Price", "Salesperson ID", "Start Date", "Status"]

    temp_rentals_data_df = pd.DataFrame(temp_rentals_data, columns=temp_rentals_data_cols)

    st.dataframe(temp_rentals_data_df, hide_index=True)
    # rental logic to be returned as dataframe

with work_orders_col:
    st.subheader("Work Orders", divider = "gray")

    temp_purchases_data = [("2022", "Subaru", "WRX", 2, "2025-01-01", "Complete"), ("2019", "Chevy", "Camaro", 2, "2025-01-02", "In Progress")]
    temp_purchases_data_cols = ["Year", "Make", "Model", "Technician ID", "Start Date", "Status"]

    temp_purchases_data_df = pd.DataFrame(temp_purchases_data, columns=temp_purchases_data_cols)

    st.dataframe(temp_purchases_data_df, hide_index=True)

    # work order logic to be returned as dataframe