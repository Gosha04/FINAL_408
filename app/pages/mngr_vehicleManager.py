import streamlit as st
import pandas as pd

st.set_page_config(page_title="Manage Vehicles", page_icon="🚙", layout="wide")

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

st.title(f"Welcome, {st.session_state['user']['first_name']}! Manage Vehicles Here.")

all_vehicles = st.container(border = True)

with all_vehicles:
    st.subheader("See all vehicles here", divider = "gray")

    # get all vehicle data into a df here
    temp_vehicle_data = [(1, "fake vin", 2022, "Subaru", "WRX", "Black", 20000, 49, True),
                         (2, "fake vin", 2016, "Toyota", "Tacoma", "Silver", 30000, 50, False),
                         (3, "fake vin", 2025, "Volkswagen", "Jetta", "White", 40000, 51, True),
                         (4, "fake vin", 2015, "Hyundai", "Sonata", "Black", 50000, 52, True),
                         (5, "fake vin", 2019, "Toyota", "Tundra", "Gray", 25000, 53, False),
                         (6, "fake vin", 2017, "Ford", "F150", "Blue", 35000, 54, True)]

    temp_vehicle_data_cols = ["Vehicle ID", "VIN", "Year", "Make", "Model", "Color", "Sale Price", "Rental Rate", "Available"]

    temp_vehicles_df = pd.DataFrame(temp_vehicle_data, columns=temp_vehicle_data_cols)

    filters, only_available = st.columns(2)

    with filters:
        mngr_vehicles_filt = st.pills("See vehicles by", selection_mode = "single", options = ["All", "Year", "Color", "Sale Price", "Rental Rate", "Make"], default = "All")

    if not mngr_vehicles_filt:
        st.error("Select a search term!")
    else:
        with only_available:
            st.write("")
            st.write("")
            only_available = st.checkbox("See only available vehicles")

        if only_available:
            temp_vehicles_df = temp_vehicles_df.loc[temp_vehicles_df["Available"] == True]

        if mngr_vehicles_filt != "All":
            if mngr_vehicles_filt == "Year" or mngr_vehicles_filt == "Sale Price" or mngr_vehicles_filt == "Rental Rate":
                filt_veh_results_by = st.text_input("Enter search term")

                if filt_veh_results_by:
                    try:
                        filt_veh_results_by = int(filt_veh_results_by)
                    except ValueError:
                        st.error("Must be a number.")

                    asc_desc_eq = st.segmented_control("Select criteria", ["Less than", "Equal to", 'Greater than'], default = "Equal to")

                    if asc_desc_eq == "Less than":
                        temp_vehicles_df = temp_vehicles_df.loc[temp_vehicles_df[mngr_vehicles_filt] < filt_veh_results_by]

                        if temp_vehicles_df.empty:
                            st.warning("No results.")
                        else:
                            st.dataframe(temp_vehicles_df, hide_index=True)
                            st.download_button("Download CSV", data = temp_vehicles_df.to_csv().encode("utf-8"), icon = ":material/download:", file_name = "vehicles.csv" )

                    elif asc_desc_eq == "Equal to":
                        temp_vehicles_df = temp_vehicles_df.loc[temp_vehicles_df[mngr_vehicles_filt] == filt_veh_results_by]

                        if temp_vehicles_df.empty:
                            st.warning("No results.")
                        else:
                            st.dataframe(temp_vehicles_df, hide_index=True)
                            st.download_button("Download CSV", data=temp_vehicles_df.to_csv().encode("utf-8"),
                                           icon=":material/download:", file_name="vehicles.csv")

                    elif asc_desc_eq == "Greater than":
                        temp_vehicles_df = temp_vehicles_df.loc[temp_vehicles_df[mngr_vehicles_filt] > filt_veh_results_by]

                        if temp_vehicles_df.empty:
                            st.warning("No results.")
                        else:
                            st.dataframe(temp_vehicles_df, hide_index=True)
                            st.download_button("Download CSV", data=temp_vehicles_df.to_csv().encode("utf-8"),
                                           icon=":material/download:", file_name="vehicles.csv")
                else:
                    st.warning("Enter search term.")

            else:
                filt_veh_results_by_str = st.text_input("Enter search term.")

                if filt_veh_results_by_str:
                    temp_vehicles_df = temp_vehicles_df.loc[temp_vehicles_df[mngr_vehicles_filt] == filt_veh_results_by_str]

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
            st.download_button("Download CSV", data=temp_vehicles_df.to_csv().encode("utf-8"), icon=":material/download:",
                           file_name="vehicles.csv")

update_vehicle_col, manage_vehicles_col = st.columns(2, border = True)

with update_vehicle_col:
    st.subheader("Update Vehicle", divider="gray")

    veh_to_update_id = st.text_input("Enter vehicle ID")

    update_button_disabled_check = False

    if veh_to_update_id:
        try:
            veh_to_update_id = int(veh_to_update_id)

            if veh_to_update_id not in temp_vehicles_df["Vehicle ID"]:
                st.warning("No vehicle with that ID found.")
                update_button_disabled_check = True
        except ValueError:
            st.error("Must be a number.")

    val_to_update = st.pills("Update", options = ["Sale Price", "Rental Rate", "Availability"], default = "Sale Price")

    if not val_to_update:
        st.error("Select a modification option!")
    else:
        if val_to_update != "Availability":
            new_val = st.text_input(f"Enter new {val_to_update}")

            if new_val:
                try:
                    new_val = int(new_val)
                except ValueError:
                    st.error("Must be a number.")
        else:
            new_val = st.selectbox("Select new availability", options = ["Available", "Not Available"])

        update_val_button_disabled = not (veh_to_update_id and new_val and val_to_update and not update_button_disabled_check)

        if st.button(f"Update {val_to_update}", disabled = update_val_button_disabled):
            # logic for updating value
            if val_to_update == "Sale Price":
                # logic for updating sale price
                pass
            elif val_to_update == "Rental Rate":
                #logic for updating rental rate
                pass
            elif val_to_update == "Availability":
                # logic for updating availability
                pass

            st.success(f"Updated {val_to_update}")

with manage_vehicles_col:
    st.subheader("Manage Vehicles", divider = "gray")

    add_or_delete_col = st.container()

    with add_or_delete_col:
        add_or_delete = st.pills("Add or delete a vehicle", options = ["Add", "Delete"], default = "Add")

        if not add_or_delete:
            st.error("Select add or delete!")
        else:
            if add_or_delete == "Delete":
                veh_to_delete = st.text_input("Enter vehicle ID to delete")

                delete_veh_button_disabled = not (veh_to_delete)

                if veh_to_delete:
                    try:
                        veh_to_delete = int(veh_to_delete)

                        if veh_to_delete not in temp_vehicles_df["Vehicle ID"]:
                            st.warning("No vehicle with that ID found.")
                            delete_veh_button_disabled = True
                    except ValueError:
                        st.error("Must be a number.")
                        delete_veh_button_disabled = True

                if st.button("Delete Vehicle", disabled = delete_veh_button_disabled):
                    # vehicle deletion logic
                    st.success(f"Deleted Vehicle ID: {veh_to_delete}")
                    pass
            else:
                new_vin = st.text_input("Enter vehicle vin")
                new_year = st.text_input("Enter year (optional)")

                if new_year:
                    try:
                        new_year = int(new_year)
                    except ValueError:
                        st.error("Must be a number.")

                new_make = st.text_input("Enter vehicle make (optional)")
                new_model = st.text_input("Enter vehicle model (optional)")
                new_color = st.text_input("Enter vehicle color (optional)")
                new_sale_price = st.text_input("Enter vehicle sale price")

                if new_sale_price:
                    try:
                        new_sale_price = int(new_sale_price)
                    except ValueError:
                        st.error("Must be a number.")

                new_rental_rate = st.text_input("Enter vehicle rental rate")

                if new_rental_rate:
                    try:
                        new_rental_rate = int(new_rental_rate)
                    except ValueError:
                        st.error("Must be a number.")


                new_availability = st.selectbox("Vehicle availability", options = ["Available", "Not Available"])

                add_button_disabled = not (new_vin and new_sale_price and new_rental_rate and new_availability)

                if st.button("Add Vehicle", disabled = add_button_disabled):
                    # logic to add new vehicle
                    # different logic depending on which values passed
                    st.success("Added new vehicle")
                    pass