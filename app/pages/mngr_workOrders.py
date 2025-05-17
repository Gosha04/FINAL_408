import streamlit as st
import pandas as pd

st.set_page_config(page_title="See Work Orders", page_icon= "🔧", layout="wide")

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

st.title(f"Welcome, {st.session_state['user']['first_name']}! See Work Orders Here.")

work_orders = st.container(border = True)

with work_orders:
    st.subheader("Work Orders", divider = "gray")

    # can only see work orders at the dealership they manage
    # logic for getting work orders (workOrders table)
    temp_work_orders_data = [(1, "2025-01-02", True, 1, 1), (2, "2025-01-03", False, 2, 2), (3, "2025-01-04", False, 3, 3), (4, "2025-01-05", True, 4, 4)]
    temp_work_orders_cols = ["WorkOrder ID", "Date Opened", "Active", "Customer ID", "Vehicle ID"]

    temp_work_orders_df = pd.DataFrame(temp_work_orders_data, columns = temp_work_orders_cols)

    only_open = st.checkbox("See only active work orders")

    if only_open:
        temp_work_orders_df = temp_work_orders_df.loc[temp_work_orders_df["Active"] == True]

    st.dataframe(temp_work_orders_df, hide_index=True)

    st.download_button("Download CSV", data = temp_work_orders_df.to_csv().encode("utf-8"), icon = ":material/download:", file_name = "workOrders.csv")

see_employee_work_orders = st.container(border = True)

with see_employee_work_orders:
    st.subheader("See assigned employees", divider = "gray")

    work_order_to_see = st.text_input("Enter Work Order ID to See Assigned Employees")

    if work_order_to_see:
        try:
            work_order_to_see = int(work_order_to_see)
        except ValueError:
            st.error("Enter a number")

    see_employees_button_disabled = not (work_order_to_see)

    button_col, checkbox_col = st.columns([1, 6])

    with button_col:
        see_employees_button = st.button("See Employees", disabled = see_employees_button_disabled)

    if not see_employees_button_disabled:
        with checkbox_col:
            only_trainees = st.checkbox("See trainees only")

    if see_employees_button:
        # logic for getting employees assigned to entered work order (employeeWorkOrders table)
        temp_emps_work_orders_data = [(1, "First", "Last", "Technician"),
                                      (2, "Last", "First", "Trainee"),
                                      (3, "Middle", "SuperMiddle", "Technician")]

        temp_emps_work_order_cols = ["Employee ID", "First Name", "Last Name", "Role"]

        temp_emps_work_orders_df = pd.DataFrame(temp_emps_work_orders_data, columns = temp_emps_work_order_cols)


        if only_trainees:
            temp_emps_work_orders_df = temp_emps_work_orders_df.loc[temp_emps_work_orders_df["Role"] == "Trainee"]

        st.dataframe(temp_emps_work_orders_df, hide_index=True)

        st.download_button("Download CSV", data = temp_emps_work_orders_df.to_csv().encode("utf-8"), file_name = f"assigned_emps_work_order_{work_order_to_see}.csv", icon = ":material/download:")

