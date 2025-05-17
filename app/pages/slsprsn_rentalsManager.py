import streamlit as st
import pandas as pd

st.set_page_config(page_title="Manage Rentals", page_icon="🏷️", layout="wide")

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

st.title(f"Welcome, {user["first_name"]} {user["last_name"]}! Manage Rentals Here.")

view_rentals = st.container(border=True)

with view_rentals:
    st.subheader("View Filed Rentals", divider="gray")

    # load in sales data for employee
    temp_rentals_data = [(1, "2025-01-01", "", 1, 1),
                         (2, "2025-01-02", "2025-02-02", 2, 2),
                         (3, "2025-01-03", "", 3, 3),
                         (4, "2025-01-04", "2025-04-04", 4, 4),
                         (5, "2025-01-05", "2025-03-02", 5, 5)]

    temp_rentals_cols = ["Rental ID", "Start Date", "End Date", "Customer ID", "Vehicle ID"]

    temp_rentals_df = pd.DataFrame(temp_rentals_data, columns=temp_rentals_cols)

    filters, only_active = st.columns([1,3])

    with filters:
        search_term = st.pills("Find by", options=["All", "Customer ID", "Vehicle ID"], default="All")

    with only_active:
        st.write("")
        st.write("")
        active_rentals_only = st.checkbox("Show only active rentals")

    if active_rentals_only:
        temp_rentals_df = temp_rentals_df.loc[temp_rentals_df["End Date"] != ""]

    if search_term:
        if search_term == "All":
            st.dataframe(temp_rentals_df, hide_index=True)

            st.download_button("Download CSV", file_name=f"emp{user["id"]}_all_sales.csv",
                               data=temp_rentals_df.to_csv().encode("utf-8"), icon=":material/download:")
        else:
            to_search_for = st.text_input(f"Enter {search_term}:")

            if to_search_for:
                try:
                    to_search_for = int(to_search_for)

                    temp_rentals_df = temp_rentals_df.loc[temp_rentals_df[search_term] == to_search_for]

                    if not temp_rentals_df.empty:
                        st.dataframe(temp_rentals_df, hide_index=True)
                        st.download_button("Download CSV", data=temp_rentals_df.to_csv().encode("utf-8"),
                                       icon=":material/download:", file_name="sales.csv")
                    else:
                        st.warning("No matching results.")
                except ValueError:
                    st.error("Must be a number.")

            else:
                st.warning("Enter search term.")

    else:
        st.error("Select a search term!")

vehicles = st.container(border=True)

with vehicles:
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

                        asc_desc_eq = st.segmented_control("Select criteria", ["Less than", "Equal to", 'Greater than'],
                                                           default="Equal to")

                        if asc_desc_eq == "Less than":
                            temp_vehicles_df = temp_vehicles_df.loc[
                                temp_vehicles_df[slsprsn_vehicles_filt] < filt_veh_results_by]

                            if temp_vehicles_df.empty:
                                st.warning("No results.")
                            else:
                                st.dataframe(temp_vehicles_df, hide_index=True)
                                st.download_button("Download CSV", data=temp_vehicles_df.to_csv().encode("utf-8"),
                                                   icon=":material/download:", file_name="vehicles.csv")

                        elif asc_desc_eq == "Equal to":
                            temp_vehicles_df = temp_vehicles_df.loc[
                                temp_vehicles_df[slsprsn_vehicles_filt] == filt_veh_results_by]

                            if temp_vehicles_df.empty:
                                st.warning("No results.")
                            else:
                                st.dataframe(temp_vehicles_df, hide_index=True)
                                st.download_button("Download CSV", data=temp_vehicles_df.to_csv().encode("utf-8"),
                                                   icon=":material/download:", file_name="vehicles.csv")

                        elif asc_desc_eq == "Greater than":
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

customers = st.container(border=True)

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

file_rental, delete_rental = st.columns(2, border = True)

with file_rental:
    st.subheader("File a Rental", divider="gray")

    new_cust = st.checkbox("Create New Customer")

    to_sell = st.text_input("Enter Vehicle ID")

    if to_sell:
        try:
            to_sell = int(to_sell)
        except ValueError:
            st.error("Must be a number.")

    txt_disabled = False

    if to_sell and (to_sell not in temp_vehicles_df["Vehicle ID"]):
        txt_disabled = True
        st.warning("Vehicle ID not found.")

    to_sell_availability = (temp_vehicles_df.loc[temp_vehicles_df["Vehicle ID"] == to_sell, "Available"])

    if not to_sell_availability.empty:
        if to_sell_availability.iloc[0] == False:
            st.warning("Vehicle not available")
            txt_disabled = True

    if new_cust:
        new_cust_first_name = st.text_input("Enter Customer First Name", disabled=txt_disabled)
        new_cust_last_name = st.text_input("Enter Customer Last Name", disabled=txt_disabled)

        st.write("Enter Rental Start Date")
        year, month, day = st.columns(3)
        with year:
            rental_file_year = st.text_input("Year", placeholder="Year", label_visibility="collapsed", max_chars=4,
                                      disabled=txt_disabled)
        with month:
            rental_file_month = st.text_input("Month", placeholder="Month", label_visibility="collapsed", max_chars=2,
                                       disabled=txt_disabled)
        with day:
            rental_file_day = st.text_input("Day", placeholder="Day", label_visibility="collapsed", max_chars=2,
                                     disabled=txt_disabled)

        if rental_file_year and rental_file_month and rental_file_day:
            try:
                int(rental_file_day)
                int(rental_file_month)
                int(rental_file_year)
                if len(rental_file_year) < 4:
                    st.warning("Year must be 4 digits")

                    txt_disabled = True

                if len(rental_file_month) < 2:
                    st.warning("Month must be 2 digits")

                    txt_disabled = True

                if len(rental_file_day) < 2:
                    st.warning("Day must be 2 digits")

                    txt_disabled = True

                if int(rental_file_month) > 12:
                    st.warning("Verify month")
                    txt_disabled = True

                if int(rental_file_day) > 31:
                    st.warning("Verify day")
                    txt_disabled = True
            except ValueError:
                st.error("Date must be numeric.")
                txt_disabled = True

        # some sort of formatting logic here, however it needs to be done to go into db

        file_button_disabled = not (to_sell and new_cust_first_name and new_cust_last_name and rental_file_year and rental_file_month and rental_file_day and not txt_disabled)

        if st.button("File Rental for New Customer", disabled=file_button_disabled):
            st.success("Customer created")
            # logic for creating new customer

            st.success("Rental filed")
            # logic for creating new purchase
    else:
        cust_id = st.text_input("Enter Customer ID", disabled=txt_disabled)

        file_button_disabled = True

        st.write("Enter Rental Start Date")
        year, month, day = st.columns(3)
        with year:
            rental_file_year = st.text_input("Year", placeholder="Year", label_visibility="collapsed", max_chars=4,
                                             disabled=txt_disabled)
        with month:
            rental_file_month = st.text_input("Month", placeholder="Month", label_visibility="collapsed", max_chars=2,
                                              disabled=txt_disabled)
        with day:
            rental_file_day = st.text_input("Day", placeholder="Day", label_visibility="collapsed", max_chars=2,
                                            disabled=txt_disabled)

        if rental_file_year and rental_file_month and rental_file_day:
            try:
                int(rental_file_day)
                int(rental_file_month)
                int(rental_file_year)
                if len(rental_file_year) < 4:
                    st.warning("Year must be 4 digits")

                    txt_disabled = True

                if len(rental_file_month) < 2:
                    st.warning("Month must be 2 digits")

                    txt_disabled = True

                if len(rental_file_day) < 2:
                    st.warning("Day must be 2 digits")

                    txt_disabled = True

                if int(rental_file_month) > 12:
                    st.warning("Verify month")
                    txt_disabled = True

                if int(rental_file_day) > 31:
                    st.warning("Verify day")
                    txt_disabled = True
            except ValueError:
                st.error("Date must be numeric.")
                txt_disabled = True

        if cust_id:
            try:
                cust_id = int(cust_id)

                file_button_disabled = not (to_sell and cust_id and rental_file_day and rental_file_month and rental_file_year and not txt_disabled)
            except ValueError:
                st.error("Must be a number.")
                file_button_disabled = True

        if st.button(f"File Rental for Customer ID: {cust_id}", disabled=file_button_disabled):
            st.success("Rental filed ")

with delete_rental:
    st.subheader("Delete a Rental", divider = "gray")

    rental_to_delete = st.text_input("Enter ID of Sale to Delete")

    delete_button_disabled = True

    if rental_to_delete:
        try:
            to_delete = int(rental_to_delete)

            if to_delete not in temp_rentals_df["Rental ID"]:
                st.warning("No Sale found with that ID")
                delete_button_disabled = True
            else:
                delete_button_disabled = False
        except ValueError:
            st.error("Must be a number.")

    if st.button(f"Delete Rental ID: {rental_to_delete}", disabled=delete_button_disabled):
        st.success("Deleted Rental")
        # rental deletion logic