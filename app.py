import streamlit as st
from database import *

st.title("🌱 Gamified Environmental Awareness Platform")

create_database()
create_admin()
if "login" not in st.session_state:
    st.session_state.login=False


if "user" not in st.session_state:
    st.session_state.user=""


st.set_page_config(
    page_title="Eco Platform",
    page_icon="🌱"
)



def login():

    st.title("🌱 Eco Awareness Platform")

    st.subheader("🔐 Login")

    username=st.text_input("Username")
    password=st.text_input(
        "Password",
        type="password"
    )


    if st.button("Login"):

        user=login_user(username,password)

        if user:

            st.session_state.login=True
            st.session_state.user=username

            st.success("Login Successful")
            st.rerun()

        else:
            st.error("Invalid Login")



def dashboard():

    st.title("🌍 Eco Dashboard")

    st.success(
        f"Welcome {st.session_state.user}"
    )


    option = st.sidebar.selectbox(
        "Menu",
        [
            "Challenges",
            "Quiz",
            "Profile",
            "Admin"
        ]
    )


    if option == "Challenges":

    st.subheader("🌱 Eco Challenges")

    st.write("Complete these tasks and earn points 🏆")


    if st.button("🌳 Plant a Tree (+50 Points)"):

        update_points(
            st.session_state.user,
            50
        )

        st.success("🌳 Tree planted! You earned 50 points")


    if st.button("💡 Save Electricity (+20 Points)"):

        update_points(
            st.session_state.user,
            20
        )

        st.success("⚡ Electricity saved! You earned 20 points")


    if st.button("♻️ Recycle Plastic (+30 Points)"):

        update_points(
            st.session_state.user,
            30
        )

        st.success("♻️ Recycling completed! You earned 30 points")
    elif option == "Quiz":

        st.subheader("🌎 Environmental Quiz")

        answer = st.radio(
            "Which is renewable energy?",
            [
                "Coal",
                "Solar Energy",
                "Petrol"
            ]
        )

        if st.button("Submit"):

            if answer == "Solar Energy":
                st.success("Correct Answer")

            else:
                st.error("Wrong Answer")


    elif option == "Profile":

        st.subheader("👤 Profile")

        user = get_user(
            st.session_state.user
        )

        if user:
            st.write("Username:", user[0])
            st.write("Email:", user[1])
            st.write("Points:", user[3])
            st.write("Level:", user[4])


    elif option == "Admin":

        st.subheader("⚙ Admin Panel")

        st.info("Admin Panel Ready")

if st.session_state.login:
    dashboard()

else:
    login()
