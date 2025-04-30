import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title = "Welcome!",
                       layout = "wide",
                       page_icon = "🚗")

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

        login_button = st.button("Log In", disabled=login_disabled)

        if login_button and st.session_state.id_input:
            try:
                user_id = int(st.session_state.id_input)

                if role == "Customer":
                    if user_id == 1:
                        st.session_state["user"] = {
                            "id": user_id,
                            "first_name": "John",
                            "last_name": "Doe",
                            "type": "Customer"
                        }

                        st.success("Signed in")
                    else:
                        st.error(f"No customer with id {user_id}.")
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
            temp_data = [("1 University Drive", "Orange", "92868", "CA")]
            cols = ["Address", "City", "Zip Code", "State"]
            results_df = pd.DataFrame(temp_data, columns=cols)

            result = results_df[results_df[search_by] == st.session_state.search_input]
            if not result.empty:
                st.dataframe(result)
            else:
                st.warning("No matching dealership found.")


if __name__ == "__main__":
    main()
