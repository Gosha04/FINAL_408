import streamlit as st
import pandas as pd

st.set_page_config(page_title="Manage Customers", page_icon= "💼", layout="wide")

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

st.title(f"Welcome, {st.session_state['user']['first_name']}! Manage Customers Here.")

customers = st.container(border = True)

with customers:
    st.subheader("Customers", divider="gray")
    # logic for getting all existing customers

    cust_data = [(1, "Pppp", "adsfasdf"),
                 (2, "adsfsadf", "dafasdhf uiboaf")]
    cust_cols = ["Customer ID", "First Name", "Last Name"]

    temp_cust_df = pd.DataFrame(cust_data, columns=cust_cols)

    st.dataframe(temp_cust_df, hide_index=True)
    st.download_button("Download CSV", data=temp_cust_df.to_csv().encode("utf-8"), file_name="customers.csv",
                       icon=":material/download:")

add_customer, delete_customer = st.columns(2, border = True)

with add_customer:
    st.subheader("Add Customer", divider="gray")

    new_first_name = st.text_input("New Customer First Name")
    new_last_name = st.text_input("New Customer Last Name")

    add_button_disabled = not (new_first_name and new_last_name)

    if st.button("Add Customer", disabled = add_button_disabled):
        st.success("Added new Customer")
        # logic for adding a customer

with delete_customer:
    st.subheader("Delete Customer", divider="gray")

    to_delete = st.text_input("Customer ID to delete")

    delete_button_disabled = not (to_delete)

    if to_delete:
        try:
            to_delete = int(to_delete)

            if to_delete not in temp_cust_df["Customer ID"]:
                st.warning("No customer with that ID found.")
                delete_button_disabled = True
        except ValueError:
            st.error("Must be a number.")
            delete_button_disabled = True

    if st.button("Delete customer", disabled = delete_button_disabled):
        st.success("Deleted customer")
        # delete customer logic