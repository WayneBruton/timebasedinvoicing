# import time

# import numpy as np
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# import os
# from streamlit_cookies_manager import EncryptedCookieManager

import extra_streamlit_components as stx

# from cryptography.fernet import Fernet

# from encodecookie import encode_cookie, decode_cookie

# import db

import login, about, contact, customers, invoices, register, settings, home

# print(db.conn)
# print(db.PORT_DB)




st.set_page_config(layout="centered",
                   initial_sidebar_state="expanded",
                   page_title="Item Based Invoicing",
                   page_icon=":moneybag:",
                   )
# create random number generator
# rng = np.random.default_rng()
# st.write("Random number generator: ", rng)

cookie_manager = stx.CookieManager(key=1)
# value = cookie_manager.get(cookie="email_in")


cookie = cookie_manager.get(cookie="user_in")
cookie_email = cookie_manager.get(cookie="email_in")
cookie_uuid = cookie_manager.get(cookie="uuid")
# st.write(cookie)
if cookie and cookie_email and cookie_uuid:
    st.session_state['user'] = cookie
    st.session_state['email'] = cookie_email
    st.session_state['uuid'] = cookie_uuid
    options = ["Home", "Invoices", "Customers",
               "Settings", "About", "Contact"]
    option_icons = ["house-fill", "file-earmark-text-fill",
                    "people-fill", "gear-fill", "info-circle-fill", "telephone-fill"]
else:

    st.session_state['user'] = None

    options = ["Home", "Login", "Register",  "About", "Contact"]
    option_icons = ["house-fill", "person-fill", "person-plus-fill",  "info-circle-fill", "telephone-fill"]

with st.sidebar:
    if cookie and cookie_email:
        # st.subheader("User")
        st.write(f"Welcome {cookie} :see_no_evil: :hear_no_evil: :speak_no_evil:")
        st.write(f"Email: {cookie_email}")
        st.write(f"UUID: {cookie_uuid}")
        logout = st.button("Logout")
        if logout:
            cookie_manager.delete(cookie="user_in", key=100)
            cookie_manager.delete(cookie="email_in" , key=101)

    selected = option_menu(menu_title="Menu", options=options,
                           menu_icon="menu-up",

                           icons=option_icons,
                           default_index=0,
                           styles={
                               "container": {
                                   "padding": "5!important", "background-color": "black"},
                               "icon": {"color": "white", "font-size": "23px"},
                               "nav-link": {"color": "white", "font-size": "20px", "text-align": "left"},
                               "nav-link-selected": {"background-color": "#02ab21"},
                           })

    # st.subheader('Home')

if selected == "Home":
    home.run()
elif selected == "Login":
    login.run()
elif selected == "Register":
    register.run()
elif selected == "Invoices":
    invoices.run()
elif selected == "Customers":
    customers.run()
elif selected == "Settings":
    settings.run()
elif selected == "About":
    about.run()
elif selected == "Contact":
    contact.run()

