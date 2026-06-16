import streamlit as st


# ---------------- LOGIN SYSTEM ----------------

if "login" not in st.session_state:
    st.session_state.login = False

if "points" not in st.session_state:
    st.session_state.points = 0


def login_page():

    st.title("🌱 Eco Awareness Platform")

    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "1234":
            st.session_state.login = True
            st.success("Login Successful")
            st.rerun()

        else:
            st.error("Invalid Username or Password")



# ---------------- DASHBOARD ----------------


def dashboard():

    st.title("🌍 Eco Awareness Dashboard")

    st.write("Welcome to the Environmental Awareness Platform")

    st.sidebar.title("Menu")

    option = st.sidebar.selectbox(
        "Choose Option",
        [
            "Eco Challenges",
            "Environmental Quiz",
            "Rewards",
            "Leaderboard"
        ]
    )


    # Challenges

    if option == "Eco Challenges":

        st.subheader("🌱 Complete Eco Challenges")

        challenge = st.checkbox(
            "Plant a Tree 🌳 (+50 points)"
        )

        if challenge:
            st.session_state.points += 50


        challenge2 = st.checkbox(
            "Save Electricity ⚡ (+20 points)"
        )

        if challenge2:
            st.session_state.points += 20


        challenge3 = st.checkbox(
            "Avoid Plastic Bags 🛍️ (+30 points)"
        )

        if challenge3:
            st.session_state.points += 30


        st.success(
            f"Your Points: {st.session_state.points}"
        )



    # Quiz

    elif option == "Environmental Quiz":

        st.subheader("🌎 Environmental Quiz")


        q1 = st.radio(
            "Which energy source is renewable?",
            [
                "Coal",
                "Solar Energy",
                "Petrol"
            ]
        )


        if st.button("Submit Quiz"):

            if q1 == "Solar Energy":
                st.success("Correct Answer! +20 Points")
                st.session_state.points += 20

            else:
                st.error("Wrong Answer")



    # Rewards

    elif option == "Rewards":

        st.subheader("🏆 Your Rewards")

        points = st.session_state.points


        if points >= 100:
            st.success("🌳 Green Champion Badge")

        elif points >= 50:
            st.info("🌱 Eco Warrior Badge")

        else:
            st.warning("Complete challenges to earn badges")



    # Leaderboard

    elif option == "Leaderboard":

        st.subheader("🏆 Leaderboard")

        data = {
            "User": [
                "You",
                "Rahul",
                "Priya"
            ],

            "Points": [
                st.session_state.points,
                120,
                100
            ]
        }

        st.table(data)



# ---------------- MAIN ----------------


if st.session_state.login:

    dashboard()

else:

    login_page()
