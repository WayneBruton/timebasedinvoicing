import streamlit as st


@st.cache_resource(experimental_allow_widgets=True)
def run():
    st.title("Customers :man-woman-girl-boy:")
    with st.form(key='customer_form'):
        st.write(st.session_state['uuid'])
        name = st.text_input("Name", help="Please enter your name")
        email = st.text_input("Email", help="Please enter your email")
        address = st.text_area("Address", help="Please enter your address")
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            if not name or not email or not address:
                st.error("Please fill out all the fields")
                return
            # check if valid email
            if '@' not in email:
                st.error("Please enter a valid email")
                return

            st.success("Thank you for contacting us. We will get back to you as soon as possible.")
