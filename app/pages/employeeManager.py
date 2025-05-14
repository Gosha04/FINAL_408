import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Employee Manager", page_icon = "️👷‍♂️", layout = "wide")

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

st.title(f"Welcome, {user['first_name']}. Manage your Employees here!")

dealerships = st.container(border = True)

with dealerships:
    st.subheader("See Dealerhips", divider = "gray")

    def update_dealers_man_search_in():
        st.session_state.dealers_man_search_in = st.session_state.dealers_man_search_temp

    filt = st.pills("See Dealerships by", options = ["All", "City", "County", "State"], selection_mode = "single", default = "All")

    # have to load all dealerships into a dataframe here
    temp_dealers_data = [(1, "1 University Drive", "Orange", "92868", "Orange", "CA"), (2, "1 test test", "Skibidi", "99999", "Texarkana", "CA"), (3, "2 testing testing", "Green Bay", "66666", "Point", "WI")]
    temp_dealer_data_cols = ["ID", "Address", "City", "Zip Code", "County", "State"]

    temp_dealer_df = pd.DataFrame(temp_dealers_data, columns=temp_dealer_data_cols)

    if filt == "All":
        st.dataframe(temp_dealer_df)
    else:
        st.text_input(f"Enter a {filt}", key = "dealers_man_search_temp", on_change=update_dealers_man_search_in)

        if "dealers_man_search_in" not in st.session_state:
            st.session_state.dealers_man_search_in = ""

        search_disabled = not st.session_state.dealers_man_search_in

        search_button = st.button(f"See Dealerships", disabled=search_disabled)

        result = temp_dealer_df.loc[temp_dealer_df[filt] == st.session_state.dealers_man_search_in]

        if search_button and st.session_state.dealers_man_search_in:
            if not result.empty:
                st.dataframe(result)
            else:
                st.warning("No matching dealerships found.")

see_employees, manage_managers = st.columns(2, border = True)

with see_employees:
    st.subheader("See Employees", divider = "gray")

    def update_employees_man_search_in():
        st.session_state.employees_man_search_in = st.session_state.employees_man_search_temp

    st.text_input("Enter a Dealership ID", key = "employees_man_search_temp", on_change=update_employees_man_search_in)

    if "employees_man_search_in" not in st.session_state:
        st.session_state.employees_man_search_in = ""

    emp_search_disabled = not st.session_state.employees_man_search_in

    button, toggle = st.columns([1,2.5], border = False)

    with button:
        emp_search_button = st.button(f"See Employees", disabled=emp_search_disabled)

    with toggle:
        managers_only = st.toggle("Managers only")

    if emp_search_button and st.session_state.employees_man_search_in:
        temp_emps = [(1, 1, "Jane", "Skort", "Manager", 10), (2,1,"Kor", "Man", "Tech", 10), (2, 2, "Poer", "Klop", "Salesperson", 10)]
        temp_emp_cols = ["ID", "Dealership ID", "First Name", "Last Name", "Role", "Supervisor ID"]

        emp_df = pd.DataFrame(temp_emps, columns=temp_emp_cols)

        emp_results = emp_df.loc[emp_df["Dealership ID"] == int(st.session_state.employees_man_search_in)]

        emp_results = emp_results.drop("Dealership ID", axis = 1)

        if managers_only:
            emp_results = emp_results.loc[emp_df["Role"] == "Manager"]

            if not emp_results.empty:
                st.dataframe(emp_results)
            else:
                st.warning("No employees found.")
        else:
            if not emp_results.empty:
                st.dataframe(emp_results)
            else:
                st.warning("No matching employees found.")

with manage_managers:
    st.subheader("Manage Managers", divider = "gray")

    choice = st.pills("Would you like to", options = ["Hire", "Fire", "Transfer"], default = "Hire")

    if choice == "Hire":
        new_mngr_id = st.text_input("Enter Dealership for New Manager")
        new_mngr_first = st.text_input("Enter First Name for New Manager")
        new_mngr_last = st.text_input("Enter Last Name for New Manager")

        # supervisor id will be 1 (owner id)
        # role will be hard coded as manager

        hire_button_disabled = not (new_mngr_id and new_mngr_first and new_mngr_last)

        hire_button = st.button("Hire", disabled=hire_button_disabled)

        if hire_button:
            st.success("Hired")
            # new manager (employee) creation logic
    elif choice == "Fire":
        to_fire_id = st.text_input("Enter Manager ID to be Fired")

        fire_button_disabled = not to_fire_id

        fire_button = st.button("Fire", disabled=fire_button_disabled)

        if fire_button:
            st.success("Fired")
            # manager deletion logic
            # need logic to ensure manager exists
    elif choice == "Transfer":
        to_transfer_mngr_id = st.text_input("Enter ID of Manager to be Transferred")
        new_dealership_id = st.text_input("Enter New Dealership ID for Manager")

        transfer_button_disabled = not (to_transfer_mngr_id and new_dealership_id)

        transfer_button = st.button("Transfer", disabled=transfer_button_disabled)

        if transfer_button:
            st.success("Transferred")
            # logic for moving a manager to a new dealership
            # includes changing all the people they manage to a different manager at that dealership if applicable
            # need logic to ensure manager and target dealership exist