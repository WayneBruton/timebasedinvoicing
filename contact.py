import streamlit as st
from db import db


def run():
    st.title("Contact Page :loudspeaker:")

    with st.form(key='contact_form'):
        st.write("Please fill out the form below and we will get back to you as soon as possible.")
        name = st.text_input("Name", help="Please enter your name")
        email = st.text_input("Email", help="Please enter your email")
        message = st.text_area("Message", help="Please enter your message")
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            if not name or not email or not message:
                st.error("Please fill out all the fields")
                return
            # check if valid email
            if '@' not in email:
                st.error("Please enter a valid email")
                return

            st.success("Thank you for contacting us. We will get back to you as soon as possible.")
