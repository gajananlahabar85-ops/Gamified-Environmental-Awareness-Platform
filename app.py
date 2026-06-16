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


    if option == "Challenges":

        st.subheader("🌳 Eco Challenges")

        if st.button("Plant a Tree 🌳 +50"):

            update_points(
                st.session_state.user,
                50
            )

            st.success("Tree Challenge Completed +50 Points")


        if st.button("Save Electricity ⚡ +20"):

            update_points(
                st.session_state.user,
                20
            )

            st.success("Electricity Challenge Completed +20 Points")

    elif menu=="Quiz":

        st.subheader("🌎 Quiz")

        q=st.radio(
            "Renewable Energy?",
            [
                "Coal",
                "Solar",
                "Petrol"
            ]
        )


        if st.button("Submit"):

            if q=="Solar":
                st.success("Correct +20 Points")

            else:
                st.error("Wrong")



    elif menu=="Profile":

        data=get_user(
            st.session_state.user
        )

        st.subheader("👤 Profile")

        st.write("Username:",data[0])
        st.write("Email:",data[1])
        st.write("Points:",data[3])
        st.write("Level:",data[4])
        st.write("Badge:",data[5])



    elif menu=="Admin":

        st.subheader("⚙ Admin Panel")

        st.info(
            "Admin features coming soon"
        )



if st.session_state.login:
    dashboard()

else:
    login()
