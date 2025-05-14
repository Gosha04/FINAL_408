import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Owner Dashboard", page_icon = "👑", layout = "wide")

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
        st.switch_page("pages/ownerDash.py")

    if st.button("Manage Dealerships"):
        st.switch_page("pages/dealershipManager.py")

    if st.button("Manage Employees"):
        st.switch_page("pages/employeeManager.py")


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

st.write(f"Your employee id: {st.session_state["user"]["id"]}, Role: {st.session_state["user"]["type"]}")

dealerships = st.container(border = True)

with dealerships:
    st.subheader("Dealerships", divider = "gray")

    temp_data = [(1, "1 University Drive", "Orange", "92868", "CA")]
    cols = ["ID", "Address", "City", "Zip Code", "State"]
    results_df = pd.DataFrame(temp_data, columns=cols)

    st.dataframe(results_df)

sales_col, employees_col = st.columns(2, border = True)

with sales_col:
    st.subheader("Dealership Sales", divider = "gray")

    def update_owner_dealer_search_in():
        st.session_state.owner_dealer_search_in = st.session_state.owner_dealer_search_temp

    st.text_input("Enter a Dealership ID to See Sales", key = "owner_dealer_search_temp", on_change = update_owner_dealer_search_in)

    if "owner_dealer_search_in" not in st.session_state:
        st.session_state.owner_dealer_search_in = ""

    search_disabled = not st.session_state.owner_dealer_search_in

    search_button = st.button("Get Sales", disabled=search_disabled)

    if search_button and st.session_state.owner_dealer_search_in:
        owner_dealer_search_id = int(st.session_state.owner_dealer_search_in)

        # logic for getting dealership sales with entered id
        if owner_dealer_search_id in list(results_df["ID"]):
            st.subheader(f"Total sales for Dealership: {st.session_state.owner_dealer_search_in}")
            st.header("$35,000")
        else:
            st.warning("No matching dealership found")


with employees_col:
    st.subheader("Dealership Employees", divider = "gray")

    def update_owner_employees_search_in():
        st.session_state.owner_employees_search_in = st.session_state.owner_employees_search_temp

    st.text_input("Enter a Dealership ID to see employees", key = "owner_employees_search_temp", on_change = update_owner_employees_search_in)

    if "owner_employees_search_in" not in st.session_state:
        st.session_state.owner_employees_search_in = ""

    emp_search_disabled = not st.session_state.owner_employees_search_in

    emp_search_button = st.button("See Employees", disabled=emp_search_disabled)

    if emp_search_button and st.session_state.owner_employees_search_in:
        owner_employees_search_id = int(st.session_state.owner_employees_search_in)

        # logic for getting employees at dealership

        if owner_employees_search_id in list(results_df["ID"]):
            st.subheader(f"Employees at Dealership: {st.session_state.owner_employees_search_in}")

            temp_emp_data = [(2, "John", "Pork", "Manager"), (3, "Maks", "Popov", "Salesperson"), (4, "Josh", "Vaysman", "Technician")]
            temp_emp_cols = ["Id", "First Name", "Last Name", "Role"]

            results_df = pd.DataFrame(temp_emp_data, columns=temp_emp_cols)

            st.dataframe(results_df)
        else:
            st.warning("No matching dealership found")