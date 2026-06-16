import streamlit as st
from database import *

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


# Challenges

if option == "Challenges":

    st.subheader("🌳 Eco Challenges")

    if st.button("Plant a Tree 🌳 +50"):

        update_points(
            st.session_state.user,
            50
        )

        st.success("Tree Challenge Completed")


# Quiz

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

    if st.button("Submit Quiz"):

        if answer == "Solar Energy":

            update_points(
                st.session_state.user,
                20
            )

            st.success("Correct Answer +20 Points")

        else:
            st.error("Wrong Answer")


# Profile

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
        st.write("Badge:", user[5])

    else:
        st.error("User not found")


# Admin

elif option == "Admin":

    st.subheader("⚙ Admin Panel")

    st.info("Admin Panel Active")

    st.write("Add Quiz and Challenges here")
