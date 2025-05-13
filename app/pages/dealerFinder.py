import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Dealership Finder", page_icon = "🔍", layout = "wide")

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

with st.sidebar:
    if st.button("Log out"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.switch_page("app.py")

    if st.button("Home"):
        st.switch_page("pages/custHome.py")

    if st.button("Find a Dealer"):
        st.switch_page("pages/dealerFinder.py")

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

st.title("Find a Dealer")

search_by = st.radio(
            "Search by",
            ("City", "County", "State"),
            horizontal = True
        )

if "search_input" not in st.session_state:
    st.session_state.search_input = ""

def update_search_input():
    st.session_state.search_input = st.session_state.search_temp

st.text_input(
            f"Enter a {search_by}",
            key = "search_temp",
            on_change = update_search_input
        )

search_disabled = not st.session_state.search_input

search_button = st.button("Search", disabled=search_disabled)

if search_button and st.session_state.search_input:
    temp_data = [("1", "1 University Drive", "Orange", "92868", "CA")]
    cols = ["Dealership ID", "Address", "City", "Zip Code", "State"]
    results_df = pd.DataFrame(temp_data, columns=cols)

    result = results_df[results_df[search_by] == st.session_state.search_input]
    if not result.empty:
        st.dataframe(result)
    else:
        st.warning("No matching dealership found.")

if "dealer_search_input" not in st.session_state:
    st.session_state.dealer_search_input = ""

def update_dealer_search_input():
    st.session_state.dealer_search_input = st.session_state.dealer_search_temp

st.text_input(
    f"Enter a Dealership ID to see available vehicles",
    key = "dealer_search_temp",
    on_change = update_dealer_search_input
)

dealer_search_disabled = not st.session_state.dealer_search_input
dealer_search_button = st.button("See vehicles", disabled=dealer_search_disabled)

if dealer_search_button and st.session_state.dealer_search_input:
    temp_vehicle_data = [("2022", "Subaru", "WRX", "2")]
    temp_vehicle_cols = ["Year", "Make", "Model", "Dealership ID"]
    veh_results_df = pd.DataFrame(temp_vehicle_data, columns=temp_vehicle_cols)

    veh_result = veh_results_df[veh_results_df["Dealership ID"] == st.session_state.dealer_search_input]

    if not veh_result.empty:
        st.dataframe(veh_result.drop(columns="Dealership ID"))
    else:
        st.warning("No vehicles available at this dealership.")