import streamlit as st
from database import register_user


st.title("🌱 Create Account")


username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input(
    "Password",
    type="password"
)


if st.button("Register"):

    if register_user(username,email,password):

        st.success("Registration Successful. Now Login")

    else:
        st.error("Username already exists")
