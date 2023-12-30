import streamlit as st

import extra_streamlit_components as stx
from streamlit_js_eval import streamlit_js_eval as js

from db import db

from hashutils import check_pwd_hash

import home



def run():
    st.title("Login:flag-za:")

    with st.form(key='login'):
        email = st.text_input(label='Email')
        # st.write(email)
        password = st.text_input(label='Password', type='password')
        # st.write(password)
        submit_button = st.form_submit_button(label='Login')
        # st.write(submit_button)
        if submit_button:
            if email != '' and password != '':
                # st.write(email)
                user_db = db.users.find_one({'email': email})
                # st.write(user_db)
                if user_db:

                    # st.write(user_db['password'])
                    # st.write(password)

                    if check_pwd_hash(password, user_db['password']):


                        st.success('Logged in successfully!')
                        cookie_manager = stx.CookieManager(key=0)
                        cookie_manager.set('user_in', user_db['name'], key=100)
                        cookie_manager.set('email_in', email, key=101)
                        cookie_manager.set('uuid', str(user_db['_id']), key=102)

                        home.run()
                        js(js_expressions="parent.window.location.reload()")

                        # st.redirect_to(main)


                        # go to home pag
                        # st.stop()
                        # st.rerun()


                    else:
                        # st.session_state['user'] = None
                        # st.session_state['email'] = None
                        st.error('Incorrect username/password')

                else:
                    st.error('Incorrect username/password')
                    # st.session_state['page'] = 'Login'

                # st.success('Logged in successfully!')
                # st.session_state['page'] = 'Login'
            else:
                st.error('All fields must be filled')
                # st.session_state['page'] = 'Login'
    #
    # # st.write(f"You came from {st.session_state['page']} page.")
    # # st.session_state['page'] = 'Login'
    # value = cookie_manager.get(cookie="email_in")
    # st.write(value)