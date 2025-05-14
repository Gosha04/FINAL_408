import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Dealership Manager", page_icon = "⚙️", layout = "wide")

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
        st.switch_page("pages/dealershipManager.py")

    if st.button("Manage Employees"):
        st.switch_page("pages/employeeManager.py")

    if st.button("Sales Dashboard"):
        st.switch_page("pages/salesDashboard.py")


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

st.title(f"Welcome, {user['first_name']}. Manage your Dealerships here!")

dealerships = st.container(border = True)

with dealerships:
    st.subheader("See Dealerhips", divider = "gray")

    def update_dealers_man_search_in():
        st.session_state.dealers_man_search_in = st.session_state.dealers_man_search_temp

    filt = st.pills("See Dealerships by", options = ["All", "City", "County", "State"], selection_mode = "single", default = "All")

    # have to load all dealerships into a dataframe here
    temp_dealers_data = [(1, "1 University Drive", "Orange", "92868", "Orange", "CA"), (2, "1 test test", "Skibidi", "99999", "Texarkana", "CA"), (3, "2 testing testing", "Green Bay", "66666", "Point", "WI")]
    temp_dealer_data_cols = ["ID", "Address", "City", "Zip Code", "County", "State"]

    temp_dealer_df = pd.DataFrame(temp_dealers_data, columns=temp_dealer_data_cols)

    if filt == "All":
        st.dataframe(temp_dealer_df)
    else:
        st.text_input(f"Enter a {filt}", key = "dealers_man_search_temp", on_change=update_dealers_man_search_in)

        if "dealers_man_search_in" not in st.session_state:
            st.session_state.dealers_man_search_in = ""

        search_disabled = not st.session_state.dealers_man_search_in

        search_button = st.button(f"See Dealerships", disabled=search_disabled)

        result = temp_dealer_df.loc[temp_dealer_df[filt] == st.session_state.dealers_man_search_in]

        if search_button and st.session_state.dealers_man_search_in:
            if not result.empty:
                st.dataframe(result)
            else:
                st.warning("No matching dealerships found.")

create_dealership = st.container(border = True)

with create_dealership:
    st.subheader("Add a Dealership", divider = "gray")

    street_address = st.text_input("Enter street address")

    # get all states
    states_temp = ["CA", "WI", "TX", "OR", "NY", "Enter a new state"] # ... ... ... etc
    state = st.selectbox("Select State", states_temp)

    new_state, new_county, new_city = False, False, False

    if state == "Enter a new state":
        state = st.text_input("Enter a new state (abbreviation only)", max_chars = 2)
        county = st.text_input("Enter a new county")
        city = st.text_input("Enter a new city")

        new_state, new_county, new_city = True, True, True
    else:
        # get all counties in that state
        counties_temp = ["One", "Two", "Three", "Four", "Five", "Enter a new county"]
        county = st.selectbox("Select County", counties_temp)

        if county == "Enter a new county":
            county = st.text_input("Enter a new county")
            city = st.text_input("Enter a new city")

            new_county, new_city = True, True
        else:
            # get all cities in that county
            cities_temp = ["Six", "Seven", "Eight", "Nine", "Enter a new city"]
            city = st.selectbox("Select City", cities_temp)

            if city == "Enter a new city":
                city = st.text_input("Enter a new city")

                new_city = True

    create_button_disabled = not (state and city and county and street_address)

    create_dealership = st.button("Create Dealership", disabled=create_button_disabled)

    if create_dealership:
        if new_state:
            # state creation logic
            pass

        if new_county:
            # county creation logic
            pass

        if new_city:
            # city creation logic
            pass

        # address creation logic

        # dealership creation logic

        # IMPORTANT THAT IN THIS ORDER FOR DB LOGIC (OR USE A TRANSACTION IDK)