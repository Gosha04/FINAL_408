import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Technician Dashboard", page_icon = "⚙️", layout = "wide")

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
        st.switch_page("pages/technicianDash.py")

    if st.button("Manage Work Orders"):
        st.switch_page("pages/tchncn_manageWorkOrders.py")


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

work_orders = st.container(border = True)

with work_orders:
    st.subheader("Your Work Orders", divider = "gray")

    # get work orders only assigned to this employee at the dealership they are assigned to
    # will require a join across multiple workOrder and employeeWorkOrder
    temp_work_order_data = [(1, "2025-01-06", True, 1, 6),
                            (2, "2025-02-05", False, 2, 5 ),
                            (3, "2025-03-04", True, 3, 4 ),
                            (4, "2025-04-03", False, 4, 3 ),
                            (5, "2025-05-02", False, 5, 2 ),
                            (6, "2025-06-01", True, 6, 1 ),
                            (7, "2025-01-06", False, 1, 6),
                            (8, "2025-02-05", True, 2, 5),
                            (9, "2025-03-04", False, 3, 4),
                            (10, "2025-04-03", True, 4, 3),
                            (11, "2025-05-02", True, 5, 2),
                            (12, "2025-06-01", False, 6, 1)
                            ]

    temp_work_order_cols = ["Work Order ID", "Date Opened", "Active", "Customer ID", "Vehicle ID"]

    temp_work_order_df = pd.DataFrame(temp_work_order_data, columns = temp_work_order_cols)

    filts_col, only_active_col = st.columns([3,7])
    with filts_col:
        filts = st.pills("Search by", options = ["All", "Customer ID", "Vehicle ID"], default = "All")
    with only_active_col:
        st.write("")
        st.write("")
        only_actice = st.checkbox("Show only active work orders")

    if only_actice:
        temp_work_order_df = temp_work_order_df[temp_work_order_df["Active"] == True]

    if filts == "All":
        st.dataframe(temp_work_order_df, hide_index = True)
        st.download_button("Download CSV", icon = ":material/download:", file_name = "work_orders.csv", data = temp_work_order_df.to_csv().encode("utf-8"))
    else:
        to_search_for = st.text_input(f"Enter {filts}")

        if to_search_for:
            try:
                to_search_by = int(to_search_for)

                temp_work_order_df = temp_work_order_df[temp_work_order_df[filts] == to_search_by]

                st.dataframe(temp_work_order_df, hide_index = True)
                st.download_button("Download CSV", data = temp_work_order_df.to_csv().encode("utf-8"), icon = ":material/download:", file_name = "work_orders.csv")
            except ValueError:
                st.error("Enter a number!")
