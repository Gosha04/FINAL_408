import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Manage Work Orders", page_icon = "🧰", layout = "wide")

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

st.title(f"Welcome, {user["first_name"]} {user["last_name"]}! Manage Work Orders Here.")

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

    temp_work_order_cols = ["Work Order ID", "Date Opened", "Open", "Customer ID", "Vehicle ID"]

    temp_work_order_df = pd.DataFrame(temp_work_order_data, columns = temp_work_order_cols)

    filts_col, only_open_col = st.columns([3,7])
    with filts_col:
        filts = st.pills("Search by", options = ["All", "Customer ID", "Vehicle ID"], default = "All")
    with only_open_col:
        st.write("")
        st.write("")
        only_open = st.checkbox("Show only open work orders")

    if only_open:
        temp_work_order_df = temp_work_order_df[temp_work_order_df["Open"] == True]

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

work_order_vehs = st.container(border = True)

with work_order_vehs:
    st.subheader("Vehicles", divider="gray")

    # get all vehicle data into a df here
    temp_vehicle_data = [(1, "fake vin", 2022, "Subaru", "WRX", "Black", 20000, 49, True),
                         (2, "fake vin", 2016, "Toyota", "Tacoma", "Silver", 30000, 50, False),
                         (3, "fake vin", 2025, "Volkswagen", "Jetta", "White", 40000, 51, True),
                         (4, "fake vin", 2015, "Hyundai", "Sonata", "Black", 50000, 52, True),
                         (5, "fake vin", 2019, "Toyota", "Tundra", "Gray", 25000, 53, False),
                         (6, "fake vin", 2017, "Ford", "F150", "Blue", 35000, 54, True)]

    temp_vehicle_data_cols = ["Vehicle ID", "VIN", "Year", "Make", "Model", "Color", "Sale Price", "Rental Rate",
                              "Available"]

    temp_vehicles_df = pd.DataFrame(temp_vehicle_data, columns=temp_vehicle_data_cols)

    filters, only_available = st.columns(2)

    with filters:
        slsprsn_vehicles_filt = st.pills("See vehicles by", selection_mode="single",
                                         options=["All", "Year", "Color", "Sale Price", "Rental Rate", "Make"],
                                         default="All")

    if not slsprsn_vehicles_filt:
        st.error("Select a search term!")
    else:
        with only_available:
            st.write("")
            st.write("")
            only_available = st.checkbox("See only available vehicles")

        if only_available:
            temp_vehicles_df = temp_vehicles_df.loc[temp_vehicles_df["Available"] == True]

        if slsprsn_vehicles_filt != "All":
            if slsprsn_vehicles_filt == "Year" or slsprsn_vehicles_filt == "Sale Price" or slsprsn_vehicles_filt == "Rental Rate":
                filt_veh_results_by = st.text_input("Enter search term")

                if filt_veh_results_by:
                    try:
                        filt_veh_results_by = int(filt_veh_results_by)

                        asc_desc_eq_sales = st.segmented_control("Select criteria",
                                                                 ["Less than", "Equal to", 'Greater than'],
                                                                 default="Equal to")

                        if asc_desc_eq_sales == "Less than":
                            temp_vehicles_df = temp_vehicles_df.loc[
                                temp_vehicles_df[slsprsn_vehicles_filt] < filt_veh_results_by]

                            if temp_vehicles_df.empty:
                                st.warning("No results.")
                            else:
                                st.dataframe(temp_vehicles_df, hide_index=True)
                                st.download_button("Download CSV", data=temp_vehicles_df.to_csv().encode("utf-8"),
                                                   icon=":material/download:", file_name="vehicles.csv")

                        elif asc_desc_eq_sales == "Equal to":
                            temp_vehicles_df = temp_vehicles_df.loc[
                                temp_vehicles_df[slsprsn_vehicles_filt] == filt_veh_results_by]

                            if temp_vehicles_df.empty:
                                st.warning("No results.")
                            else:
                                st.dataframe(temp_vehicles_df, hide_index=True)
                                st.download_button("Download CSV", data=temp_vehicles_df.to_csv().encode("utf-8"),
                                                   icon=":material/download:", file_name="vehicles.csv")

                        elif asc_desc_eq_sales == "Greater than":
                            temp_vehicles_df = temp_vehicles_df.loc[
                                temp_vehicles_df[slsprsn_vehicles_filt] > filt_veh_results_by]

                            if temp_vehicles_df.empty:
                                st.warning("No results.")
                            else:
                                st.dataframe(temp_vehicles_df, hide_index=True)
                                st.download_button("Download CSV", data=temp_vehicles_df.to_csv().encode("utf-8"),
                                                   icon=":material/download:", file_name="vehicles.csv")
                    except ValueError:
                        st.error("Must be a number.")
                else:
                    st.warning("Enter search term.")

            else:
                filt_veh_results_by_str = st.text_input("Enter search term.")

                if filt_veh_results_by_str:
                    temp_vehicles_df = temp_vehicles_df.loc[
                        temp_vehicles_df[slsprsn_vehicles_filt] == filt_veh_results_by_str]

                    if temp_vehicles_df.empty:
                        st.warning("No results.")
                    else:
                        st.dataframe(temp_vehicles_df, hide_index=True)
                        st.download_button("Download CSV", data=temp_vehicles_df.to_csv().encode("utf-8"),
                                           icon=":material/download:", file_name="vehicles.csv")
                else:
                    st.warning("Enter search term.")

        else:
            st.dataframe(temp_vehicles_df, hide_index=True)
            st.download_button("Download CSV", data=temp_vehicles_df.to_csv().encode("utf-8"),
                               icon=":material/download:",
                               file_name="vehicles.csv")

customers = st.container(border = True)

with customers:
    st.subheader("Customers", divider = "gray")
    # logic for getting all existing customers

    cust_data = [(1, "Pppp", "adsfasdf"),
                 (2, "adsfsadf", "dafasdhf uiboaf")]
    cust_cols = ["Customer ID", "First Name", "Last Name"]

    temp_cust_df = pd.DataFrame(cust_data, columns = cust_cols)

    st.dataframe(temp_cust_df, hide_index=True)
    st.download_button("Download CSV", data = temp_cust_df.to_csv().encode("utf-8"), file_name = "customers.csv", icon=":material/download:")

create_work_order, delete_work_order = st.columns(2, border = True)

with create_work_order:
    st.subheader("Create a Work Order", divider = "gray")

    new_cust = st.checkbox("Create a New Customer")

    invalid_in = True
    no_such_cust = False
    no_such_veh = False

    if new_cust:
        new_cust_first_name = st.text_input("Enter New Customer First Name")
        new_cust_last_name = st.text_input("Enter New Customer Last Name")

        if new_cust_first_name and new_cust_last_name:
            invalid_in = False
    else:
        cust_id = st.text_input("Enter Customer ID")

        if cust_id:
            try:
                cust_id = int(cust_id)
                invalid_in = False

                if cust_id not in temp_cust_df["Customer ID"].values:
                    no_such_cust = True
                    st.warning(f"No customer with ID {cust_id}")
            except ValueError:
                st.error("Enter a number!")
                invalid_in = True

    veh_to_work_on = st.text_input("Enter Vehicle ID")

    if veh_to_work_on:
        try:
            veh_to_work_on = int(veh_to_work_on)
            invalid_in = False

            if veh_to_work_on not in temp_vehicles_df["Vehicle ID"].values:
                no_such_veh = True
                st.warning(f"No vehicle with ID {veh_to_work_on}")
        except ValueError:
            st.error("Enter a number!")
            invalid_in = True
    else:
        invalid_in = True

    create_work_order_button_disabled = invalid_in or no_such_cust or no_such_veh

    if st.button("Create Work Order", disabled = create_work_order_button_disabled):
        if new_cust:
            st.success("Created new customer")
            # get id back out into some var
            # then create work order with that id
            st.success("Created new work order")
        else:
            st.success("Created new work order")
            # just create new work order with given data

with delete_work_order:
    st.subheader("Delete a Work Order", divider = "gray")

    work_order_to_delete = st.text_input("Enter Work Order IDto delete")

    delete_button_disabled = True

    if work_order_to_delete:
        try:
            work_order_to_delete = int(work_order_to_delete)

            delete_button_disabled = False

            if work_order_to_delete not in temp_work_order_df["Work Order ID"].values:
                delete_button_disabled = True
                st.warning(f"No work order with ID {work_order_to_delete}")
        except ValueError:
            st.error("Enter a number!")

            delete_button_disabled = True

    if st.button("Delete Work Order", disabled = delete_button_disabled):
        st.success("Deleted work order")
        # delete work order logic

close_work_order = st.container(border = True)

with close_work_order:
    st.subheader("Close a Work Order", divider = "gray")

    temp_work_order_df = temp_work_order_df[temp_work_order_df["Open"] == True]

    st.dataframe(temp_work_order_df, hide_index=True)

    to_close = st.text_input("Enter Work Order ID to close")

    close_button_disabled = True

    if to_close:
        try:
            to_close = int(to_close)
            close_button_disabled = False

            if to_close not in temp_work_order_df["Work Order ID"].values:
                close_button_disabled = True
                st.warning(f"No open work order with ID {to_close}")
        except ValueError:
            st.error("Enter a number!")
            close_button_disabled = True

    if st.button("Close Work Order", disabled = close_button_disabled):
        st.success("Work order closed")
        # logic for updating work orders open status