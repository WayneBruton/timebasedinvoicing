import streamlit as st


@st.cache_resource(experimental_allow_widgets=True)
def run():
    st.title("Time Based Invoicing :credit_card:", anchor=None)
    st.image("invoicing.jpg")


