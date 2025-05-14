import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Manager Dashboard", page_icon = "👨‍💼", layout = "wide")

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

usr_id_col, role_col, dealership_col = st.columns([4, 4, 14])

with usr_id_col:
    st.write(f"Your employee id: {st.session_state["user"]["id"]}")

with role_col:
    st.write(f"Role: {st.session_state["user"]["type"]}")

with dealership_col:
    st.write(f"Dealership: {st.session_state["user"]["dealershipID"]}")

employees = st.container(border = True)

with employees:
    st.subheader("Employees", divider = "gray")

    # get all employees for the dealership that the manager works at
    temp_employees_data = [(12, "John", "Pork", "Manager", 2), (13, "Jane", "Bacon", "Salesperson", 2), (14, "Kevin", "Bacon", "Technician", 2), (15, "Sporgle", "McSploingus", "Trainee", 2)]
    temp_employees_data_cols = ["Employee ID", "First Name", "Last Name", "Role", "Manager ID"]

    temp_employees_df = pd.DataFrame(temp_employees_data, columns = temp_employees_data_cols)

    emp_filt = st.pills("See Employees by Role", options = ["All", "Manager", "Salesperson", "Technician", "Trainee"], selection_mode = "single", default = "All")

    if emp_filt == "All":
        st.dataframe(temp_employees_df, hide_index=True)

        st.download_button("Download CSV", data = temp_employees_df.to_csv().encode("utf-8"), file_name = "employees.csv", icon = ":material/download:")
    else:
        temp_employees_df = temp_employees_df.loc[temp_employees_df["Role"] == emp_filt]

        st.dataframe(temp_employees_df, hide_index = True)

        # CHANGE DF NAME IN DOWNLOAD BUTTON IF CHANGING DF NAME
        st.download_button("Download CSV", data=temp_employees_df.to_csv().encode("utf-8"), file_name="employees.csv",
                           icon=":material/download:")

sales, vehicles = st.columns(2, border = True)

with sales:
    st.subheader("Sales", divider = "gray")

    mngr_sales_filt = st.toggle("See by Salesperson")

    if not mngr_sales_filt:
        amt = 60000 # replace with logic for getting sales for a dealership (only sum purchases, dont sum rentals)
        st.subheader(f"${amt}")
    else:
        # replace with require logic to get sales for employees (dollar amount of sales for each employee)
        temp_employee_sales_data = [(1, "Jonathan", "Johnson", 2, 20000), (2, "Skermit", "Skandalous", 2, 5000), (3, "Prototype", "Robot", 2, 1000)]
        temp_employee_sales_data_cols = ["Employee ID", "First Name", "Last Name", "Manager ID", "Sales"]

        temp_employee_sales_data_df = pd.DataFrame(temp_employee_sales_data, columns = temp_employee_sales_data_cols)

        st.dataframe(temp_employee_sales_data_df, hide_index = True)

        # CHANGE DF NAME IN DOWNLOAD BUTTON IF CHANGING DF NAME
        st.download_button("Download CSV", data=temp_employee_sales_data_df.to_csv().encode("utf-8"), file_name="sales_by_employee.csv",
                           icon=":material/download:")

with vehicles:
    st.subheader("Vehicles", divider = "gray")

    st.write("For more detailed info see vehicle management")

    temp_vehicle_data = [("2022", "Toyota", "4Runner", "Yes"), ("2016", "Honda", "Accord", "No"), ("2017", "Lamborghini", "Urus", "No")]
    temp_vehicle_data_cols = ["Year", "Make", "Model", "Available"]

    temp_vehicle_data_df = pd.DataFrame(temp_vehicle_data, columns = temp_vehicle_data_cols)

    st.dataframe(temp_vehicle_data_df, hide_index = True)
