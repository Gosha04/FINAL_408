import streamlit as st
import pandas as pd
import time

def main():
    st.set_page_config(page_title = "Welcome!",
                       layout = "wide",
                       page_icon = "🚗")

    st.markdown("""
        <style>
            [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] {
                display: none;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
            <style>
                .block-container {
                    padding-top: 11px;
                }
                
                .stColumn {
                    padding-top: 0;
                }
                </style>
        """, unsafe_allow_html = True)

    st.title("Welcome to the Dealership App!")

    login_col, finder_col = st.columns(2, border = True)

    with login_col:
        st.subheader("Log in", divider = "gray")

        role = st.radio(
            "Log in as a",
            ("Customer", "Employee"),
            horizontal = True
        )

        if "id_input" not in st.session_state:
            st.session_state.id_input = ""

        def update_id_input():
            st.session_state.id_input = st.session_state.input_temp

        st.text_input(
            f"Enter your {role} ID",
            key = "input_temp",
            on_change = update_id_input
        )

        login_disabled = not st.session_state.id_input

        col_login, col_create = st.columns(2)

        login_button = col_login.button("Log In", disabled=login_disabled, use_container_width=True)

        if role == "Customer":
            create_button = col_create.button("Create New Account", use_container_width=True)

        if login_button and st.session_state.id_input:
            try:
                user_id = int(st.session_state.id_input)

                if role == "Customer":
                    if user_id == 1: # WILL BE REPLACED W DATA EXTRACTED FROM DB
                        st.session_state["user"] = {
                            "id": user_id,
                            "first_name": "John",
                            "last_name": "Doe",
                            "type": "Customer"
                        }

                        with st.spinner("Logging in..."):
                            time.sleep(2)
                        st.success("Signed in")

                        time.sleep(0.5)

                        st.switch_page("pages/custHome.py")
                    else:
                        st.error(f"No customer with ID {user_id}.")
                elif role == "Employee":
                    if user_id == 1: # all will be replaced with data extracted from DB
                        st.session_state["user"] = {
                            "id": user_id,
                            "first_name": "John",
                            "last_name": "Doe",
                            "type": "Manager",
                            "manager": 1,
                            "dealershipID": 1
                        }

                        with st.spinner("Logging in..."):
                            time.sleep(2)
                        st.success("Signed in")

                        time.sleep(0.5)

                        if st.session_state["user"]["type"] == "Owner":
                            st.switch_page("pages/ownerDash.py")

                        if st.session_state["user"]["type"] == "Manager":
                            st.switch_page("pages/managerDash.py")
            except ValueError:
                st.error("Please enter a valid ID.")

        if role == "Customer" and create_button and st.session_state.id_input:
            try:
                user_id = int(st.session_state.id_input)

                # creation logic

                st.success(f"Created account with id {user_id}")
            except ValueError:
                st.error("Please enter a valid ID.")

    with finder_col:
        st.subheader("Find a dealership", divider = "gray")

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
            temp_data = [("1", "1 University Drive", "Orange", "92868", "Orange", "CA")]
            cols = ["ID", "Address", "City", "Zip Code", "County", "State"]
            results_df = pd.DataFrame(temp_data, columns=cols)

            result = results_df[results_df[search_by] == st.session_state.search_input]
            if not result.empty:
                st.dataframe(result, hide_index=True)
            else:
                st.warning("No matching dealership found.")


if __name__ == "__main__":
    main()
