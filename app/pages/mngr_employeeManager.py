import streamlit as st
import pandas as pd

st.set_page_config(page_title="Manage Employees", page_icon="👥", layout="wide")

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
        st.switch_page("pages/managerDash.py")

    if st.button("Manage Employees"):
        st.switch_page("pages/mngr_employeeManager.py")

    if st.button("Manage Vehicles"):
        st.switch_page("pages/mngr_vehicleManager.py")

    if st.button("See Work Orders"):
        st.switch_page("pages/mngr_workOrders.py")

    if st.button("Manage Customers"):
        st.switch_page("pages/mngr_customerManager.py")

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

st.title(f"Welcome, {st.session_state['user']['first_name']}! Manage Employees Here.")

employees_view = st.container(border = True)

with employees_view:
    st.subheader("Employees", divider="gray")

    # get all employees for the dealership that the manager works at
    temp_employees_data = [(12, "John", "Pork", "Manager", 2), (13, "Jane", "Bacon", "Salesperson", 2),
                           (14, "Kevin", "Bacon", "Technician", 2), (15, "Sporgle", "McSploingus", "Trainee", 2)]
    temp_employees_data_cols = ["Employee ID", "First Name", "Last Name", "Role", "Manager ID"]

    temp_employees_df = pd.DataFrame(temp_employees_data, columns=temp_employees_data_cols)

    emp_filt = st.pills("See Employees by Role", options=["All", "Manager", "Salesperson", "Technician", "Trainee"],
                        selection_mode="single", default="All")

    if not emp_filt:
        st.error("Select a search term!")
    else:
        if emp_filt == "All":
            st.dataframe(temp_employees_df, hide_index=True)

            st.download_button("Download CSV", data=temp_employees_df.to_csv().encode("utf-8"), file_name="employees.csv",
                           icon=":material/download:")
        else:
            temp_employees_df = temp_employees_df.loc[temp_employees_df["Role"] == emp_filt]

            st.dataframe(temp_employees_df, hide_index=True)

            # CHANGE DF NAME IN DOWNLOAD BUTTON IF CHANGING DF NAME
            st.download_button("Download CSV", data=temp_employees_df.to_csv().encode("utf-8"), file_name="employees.csv",
                           icon=":material/download:")

manage_employees = st.container(border = True)

with manage_employees:
    st.subheader("Manage Employees", divider="gray")

    hire_col, manage_col = st.columns(2, border = True)

    with hire_col:
        st.subheader("Hire Employees", divider="gray")

        new_emp_first_name = st.text_input("New Employee First Name")

        new_emp_last_name = st.text_input("New Employee Last Name")

        new_emp_role = st.selectbox("New Employee Role", options = ["Salesperson", "Technician", "Trainee"])

        new_emp_manager_id = st.text_input("New Employee Manager ID")

        if(new_emp_manager_id):
            try:
                new_emp_manager_id = int(new_emp_manager_id)
            except ValueError:
                st.error("Enter a Number!")

        # new employee dealership ID will be whatever dealership manager is at

        hire_emp_button_disabled = not (new_emp_first_name and new_emp_last_name and new_emp_role and new_emp_manager_id)

        if st.button("Hire Employee", disabled = hire_emp_button_disabled):
            # new employee creation logic
            st.success(f"{new_emp_first_name} {new_emp_last_name} hired as {new_emp_role}, reports to Manager ID: {new_emp_manager_id}")

            # add logic if fails for some reason
    with manage_col:
        st.write("")

        fire = st.container(border = True)

        with fire:
            st.subheader("Fire Employees", divider="gray")

            to_fire_emp_id = st.text_input("Employee ID to Fire")

            employee_not_exists = True

            if to_fire_emp_id:
                try:
                    to_fire_emp_id = int(to_fire_emp_id)

                    if to_fire_emp_id not in temp_employees_df["Employee ID"].values:
                        st.warning("No employee found")
                        employee_not_exists = False
                    else:
                        employee_not_exists = True
                except ValueError:
                    st.error("Enter a Number!")
                    employee_not_exists = False

            to_fire_emp_button_disabled = not (to_fire_emp_id and employee_not_exists)

            if st.button("Fire Employee", disabled = to_fire_emp_button_disabled):
                st.success(f"Fired employee ID: {to_fire_emp_id}")

        new_manager = st.container(border = True)

        with new_manager:
            st.subheader("Assign New Employee Manager", divider = "gray")

            # to get employee data
            to_reassign = st.text_input("Employee ID to Reassign")

            if to_reassign:
                try:
                    to_reassign = int(to_reassign)
                except ValueError:
                    st.error("Enter a Number!")

            # to get manager data
            new_mngr_id = st.text_input("New Manager ID")

            if new_mngr_id:
                try:
                    new_mngr_id = int(new_mngr_id)
                except ValueError:
                    st.error("Enter a Number!")

            reassign_button_disabled = not(to_reassign and new_mngr_id)

            # get employee to reassign data, this is all test data, all employees will have dealership id of manager as they can only manage their own dealership
            # this is different from above because we are grabbing right after the user has entered
            # i am essentially just trying to simulate validity checks here, this is not the best way to do it but idk how else
            # this could also be connected to the earlier loading in of the data above where all

            # get roles
            emp_to_reassign = temp_employees_df.loc[temp_employees_df["Employee ID"] == to_reassign]
            new_mngr = temp_employees_df.loc[temp_employees_df["Employee ID"] == new_mngr_id]

            if not emp_to_reassign.empty and not new_mngr.empty:
                if emp_to_reassign.iloc[0]["Role"] == "Manager":
                    st.error("Cannot reassign a Manager.")
                    reassign_button_disabled = True

                elif emp_to_reassign.iloc[0]["Role"] != "Trainee" and new_mngr.iloc[0]["Role"] != "Manager":
                    st.error("Non-Trainees must report to Managers.")
                    reassign_button_disabled = True

                elif emp_to_reassign.iloc[0]["Role"] == "Trainee" and new_mngr.iloc[0]["Role"] == "Trainee":
                    st.error("Trainees cannot manage Trainees.")
                    reassign_button_disabled = True
            else:
                if to_reassign and new_mngr_id:
                    st.error("Invalid employee or manager ID.")
                    reassign_button_disabled = True

            if st.button("Reassign Employee", disabled = reassign_button_disabled):
                st.success(f"Reassign Employee ID: {to_reassign} to Manager ID: {new_mngr_id}")

                # logic for updating an employees manager
