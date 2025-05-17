import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Salesperson Dashboard", page_icon = "👨‍💻", layout = "wide")

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
        st.switch_page("pages/salespersonDash.py")

    if st.button("Manage Sales"):
        st.switch_page("pages/slsprsn_salesManager.py")

    if st.button("Manage Rentals"):
        st.switch_page("pages/slsprsn_rentalsManager.py")

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

slsprsn_sales, slsprsn_rentals = st.columns(2, border = True)

with slsprsn_sales:
    st.subheader("Your Filed Sales", divider = "gray")

    # salesperson id will be theirs, dealership id will also be theirs, can use user var from above
    # logic for getting employee sales
    temp_sales_data = [(1, 40000, "2025-01-01", 1, 1),
                       (2, 50000, "2025-01-02", 2, 2),
                       (3, 60000, "2025-01-03", 3, 3),
                       (4, 70000, "2025-01-04", 4, 5),
                       (5, 80000, "2025-01-05", 5, 5)]

    temp_sales_cols = ["Sale ID", "Amount", "Date", "Customer ID", "Vehicle ID"]

    temp_sales_df = pd.DataFrame(temp_sales_data, columns = temp_sales_cols)

    st.dataframe(temp_sales_df, hide_index=True)

    st.download_button("Download CSV", file_name = f"emp{user["id"]}_sales.csv", icon = ":material/download:", data = temp_sales_df.to_csv().encode("utf-8"))

    total_sales_amt, avg_sale_amt, num_sales = st.columns(3)

    with total_sales_amt:
        st.write(f"Total sales:")
        st.subheader(f"${temp_sales_df["Amount"].sum()}")
    with avg_sale_amt:
        st.write(f"Average sale amount:")
        st.subheader(f"${temp_sales_df["Amount"].mean()}")
    with num_sales:
        st.write(f"Number of sales:")
        st.subheader(f"{temp_sales_df.shape[0]}")

with slsprsn_rentals:
    st.subheader("Your Filed Rentals", divider = "gray")

    # salesperson id will hbe theirs, dealership id will also be theirs, can use user var from above
    # logic for getting employee rentals

    temp_rentals_data = [(1, "2025-01-01", "", 1, 1),
                         (2, "2025-01-02", "2025-02-02", 2, 2),
                         (3, "2025-01-03", "", 3, 3),
                         (4, "2025-01-04", "2025-04-04", 4, 4),
                         (5, "2025-01-05", "2025-03-02", 5, 5)]

    temp_rentals_cols = ["Rental ID", "Start Date", "End Date", "Customer ID", "Vehicle ID"]

    temp_rentals_df = pd.DataFrame(temp_rentals_data, columns = temp_rentals_cols)

    st.dataframe(temp_rentals_df, hide_index=True)

    st.download_button("Download CSV", file_name=f"emp{user["id"]}_rentals.csv", icon=":material/download:",
                       data=temp_rentals_df.to_csv().encode("utf-8"))

    num_rentals, blank_col, blank_col2 = st.columns(3) # for formatting

    with num_rentals:
        st.write(f"Number of rentals:")
        st.subheader(f"{temp_rentals_df.shape[0]}")