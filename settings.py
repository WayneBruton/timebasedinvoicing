import streamlit as st
from db import db
import pandas as pd



def run():
    result = db.settings.find_one({'user_id': st.session_state['uuid']})
    st.write(result)
    if result:
        result['_id'] = str(result['_id'])
        nameR = result['name']
        trading_nameR = result['trading_name']
        phone_numberR = result['phone_number']
        addressR = result['address']
        emailR = result['email']
        vat_numberR = result['vat_number']
        vatableR = result['vatable']
    else:
        nameR = ""
        trading_nameR = ""
        phone_numberR = ""
        addressR = ""
        emailR = ""
        vat_numberR = "N/A"
        vatableR = False
    st.title("Settings  :gear:")
    name = st.text_input("Name", help="Please enter your name", value=nameR)
    trading_name = st.text_input("Trading Name", help="Please enter your trading name", value=trading_nameR)
    phone_number = st.text_input("Phone Number", help="Please enter your phone number", value=phone_numberR)
    address = st.text_area("Address", help="Please enter your address", value=addressR)
    email = st.text_input("Email", help="Please enter your email", value=emailR)
    col1, col2 = st.columns(2)
    vatable = col1.checkbox("VAT Registered", value=vatableR, help="Are you VAT registered?",  )
    cb_value = vat_numberR

    if vatable :
        cb_value = ""

        vat_number = col2.text_input("VAT Number", help="Please enter your VAT number", value=cb_value)
    # else:
        # vat_number = col2.text_input("VAT Number", help="Please enter your VAT number", value=cb_value, disabled=True)
    submit_button = st.button(label='Submit')
    if submit_button:
        if not name or not email or not trading_name or not phone_number or not address:
            st.error("Please fill out all the fields")
            return
        if vatable:
            if not vat_number:
                st.error("Please fill out all the fields")
                return
        else:
            vat_number = "N/A"
        if '@' not in email:
            st.error("Please enter a valid email")
            return




        # if address is not None:
        #     textsplit = address.splitlines()
        #
        #     for x in textsplit:
        #         st.write(x)

        st.write(st.session_state['uuid'])


        insert = {
            'name': name,
            'trading_name': trading_name,
            'phone_number': phone_number,
            'address': address,
            'email': email,
            'vat_number': vat_number,
            'vatable': vatable,
            'user_id': st.session_state['uuid']
        }
        st.write(insert)
        if result:
            db.settings.update_one({'user_id': st.session_state['uuid']}, {"$set": insert})
        else:
            db.settings.insert_one(insert)
        st.success("Settings saved successfully")

    # df = pd.DataFrame.from_dict(result, orient='index')
    # st.write("Dataframe")
    # st.dataframe(df)
    st.write("Table")
    st.table(result)

        # name = ""
        # trading_name = ""
        # phone_number = ""
        # address = ""
        # email = ""
        # vat_number = "N/A"
        # vatable = False
