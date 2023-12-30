import streamlit as st

import streamlit_authenticator as sta
from hashutils import make_pwd_hash
import os

from dotenv import load_dotenv

load_dotenv('.env')

# print(os.getenv('DETA_API'))

from db import db

users = db.users

# print("USERS: ",list(users.find({})))
global name, last_name, email, password, confirm_password


@st.cache_resource(experimental_allow_widgets=True)
def run():
    st.session_state['reset'] = False
    global name, last_name, email, password, confirm_password


    st.title("Register :flag-za:")

    with st.form(key='register_form', clear_on_submit=True):
        if st.session_state['reset']:
            name = ""
        else:
            name = st.text_input("Name", type="default", help="Please enter your name")
        last_name = st.text_input("Last Name", type="default", help="Please enter your last name")
        email = st.text_input("Email", type="default", help="Please enter your email")
        password = st.text_input("Password", type="password", help="Please enter your password")
        confirm_password = st.text_input("Confirm Password", type="password", help="Please confirm your password")
        col1, col2 = st.columns(2)
        with col1:
            submit_button = st.form_submit_button(label='Register')
        with col2:
            reset_button = st.form_submit_button(label='Reset')
            if reset_button:
                st.session_state['reset'] = True
        if submit_button:
            if not name or not last_name or not email or not password or not confirm_password:
                st.error("Please fill out all the fields")

            if password == confirm_password:

                st.success("You have successfully registered")
                password_hashed = make_pwd_hash(password)
                insert = {
                    'name': name,
                    'last_name': last_name,
                    'email': email,
                    'password': password_hashed
                }
                db.users.insert_one(insert)
                st.session_state['reset'] = True
                return


            else:
                password = ""
                confirm_password = ""
                st.error("Passwords do not match")
                return

