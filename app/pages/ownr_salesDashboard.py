import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Sales Dashboard", page_icon = "️💰️", layout = "wide")

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
        st.switch_page("pages/ownr_dealershipManager.py")

    if st.button("Manage Employees"):
        st.switch_page("pages/ownr_employeeManager.py")

    if st.button("Sales Dashboard"):
        st.switch_page("pages/ownr_salesDashboard.py")


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

st.title(f"Welcome, {user['first_name']}. See Sales Info Here!")

global_sales = st.container(border = True)

with global_sales:
    st.subheader("Global Sales", divider = "gray")

    sales_filt = st.pills("See sales by", options = ["Global", "City", "County", "State"], default = "Global")

    if not sales_filt:
        st.error("Select a search option!")
    else:
        if sales_filt == "Global":
            st.subheader("Total Sales for All Dealerships")

            amt = 100000000 # logic for getting total sales

            st.title(f"${amt}")
        elif sales_filt == "City":
            # sum with group by on city to load into data frame
            cities_sales_data_temp = [("Orange", 200000), ("Stevens Points", 10000), ("San Francisco", 5000000)]
            cities_sales_data_cols = ["City", "Sales Amount"]

            cities_sales_df_temp = pd.DataFrame(cities_sales_data_temp, columns = cities_sales_data_cols)

            st.dataframe(cities_sales_df_temp, hide_index=True)

            # CHANGE NAME IN DOWNLOAD IF CHANGING DF NAME
            st.download_button("Download CSV", data=cities_sales_df_temp.to_csv().encode("utf-8"),
                           file_name="sales_by_state.csv", icon=":material/download:")
        elif sales_filt == "County":
            # sum with group by on county to load into data frame
            counties_sales_data_temp = [("Orange", 10000000), ("Contra Costa", 200000), ("Texarkana", 666066060)]
            counties_sales_data_cols = ["County", "Sales Amount"]

            counties_sales_df_temp = pd.DataFrame(counties_sales_data_temp, columns = counties_sales_data_cols)

            st.dataframe(counties_sales_df_temp, hide_index=True)

            # CHANGE NAME IN DOWNLOAD IF CHANGING DF NAME
            st.download_button("Download CSV", data=counties_sales_df_temp.to_csv().encode("utf-8"),
                           file_name="sales_by_county.csv", icon=":material/download:")
        elif sales_filt == "State":
            # sum with group by on state to load into data frame
            states_sales_data_temp = [("CA", 400000000), ("WI", 79863522345), ("TX", 48572398475)]
            states_sales_data_cols = ["State", "Sales Amount"]

            states_sales_df_temp = pd.DataFrame(states_sales_data_temp, columns = states_sales_data_cols)

            st.dataframe(states_sales_df_temp, hide_index=True)

            # CHANGE NAME IN DOWNLOAD IF CHANGING DF NAME
            st.download_button("Download CSV", data=states_sales_df_temp.to_csv().encode("utf-8"),
                           file_name="sales_by_state.csv", icon=":material/download:")

dealership_sales = st.container(border = True)

with dealership_sales:
    st.subheader("Sales by Dealership", divider = "gray")

    def update_dealers_man_search_in():
        st.session_state.dealers_man_search_in = st.session_state.dealers_man_search_temp

    filt = st.pills("See Dealerships by", options = ["All", "City", "County", "State"], selection_mode = "single", default = "All")

    # have to load all dealerships into a dataframe here
    temp_dealers_data = [(1, "1 University Drive", "Orange", "92868", "Orange", "CA", 238475023798), (2, "1 test test", "Skibidi", "99999", "Texarkana", "CA", 237958209867), (3, "2 testing testing", "Green Bay", "66666", "Point", "WI", 6754798389)]
    temp_dealer_data_cols = ["ID", "Address", "City", "Zip Code", "County", "State", "Sales Amount"]

    temp_dealer_df_sales = pd.DataFrame(temp_dealers_data, columns=temp_dealer_data_cols)

    if not filt:
        st.error("Enter a search term!")
    else:
        if filt == "All":
            st.dataframe(temp_dealer_df_sales, hide_index=True)

            # CHANGE NAME IN DOWNLOAD IF CHANGING DF NAME
            st.download_button("Download CSV", data=temp_dealer_df_sales.to_csv().encode("utf-8"),
                           file_name="all_dealership_sales.csv", icon=":material/download:")
        else:
            st.text_input(f"Enter a {filt}", key = "dealers_man_search_temp", on_change=update_dealers_man_search_in)

            if "dealers_man_search_in" not in st.session_state:
                st.session_state.dealers_man_search_in = ""

            search_disabled = not st.session_state.dealers_man_search_temp

            search_button = st.button(f"See Dealerships", disabled=search_disabled)

            result = temp_dealer_df_sales.loc[temp_dealer_df_sales[filt] == st.session_state.dealers_man_search_in] # can just index original dataframe

            if search_button and st.session_state.dealers_man_search_in:
                if not result.empty:
                    st.dataframe(result, hide_index=True)

                    # CHANGE NAME IN DOWNLOAD IF CHANGING DF NAME
                    st.download_button("Download CSV", data=result.to_csv().encode("utf-8"),
                                   file_name="dealership_sales.csv", icon=":material/download:")
                else:
                    st.warning("No matching dealerships found.")