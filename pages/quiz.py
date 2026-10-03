#quiz!
import streamlit as st

st.title("Which Member of the Ball Family Are You?")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("Images/lamelo1.jpg", caption="LaMelo")

with col2:
    st.image("Images/lonzo.jpg", caption="Lonzo")

with col3:
    st.image("Images/gelo.jpg", caption="LiAngelo")

with col4:
    st.image("Images/lavar.jpg", caption="LaVar")


tab1, tab2 = st.tabs(["Quiz", "About Your Results"]) # EXTRA CREDIT

with tab1:
    st.write("Answer the questions below to find our which Ball Family member you are!")

    st.header("Question 1")

    question1 = st.radio("What is your favorite thanksgiving food?", ["Peach Cobbler", "Big Baller Breakfast", "PB & J", "Caramel Cookies"]) #NEW

    st.header("Question 2")

    question2 = st.number_input("What is your favorite number?", min_value = 0, max_value = 99, step = 1) #NEW

    st.header("Question 3")

    question3 = st.slider("How likely are you to sleep through practice?", min_value = 1, max_value = 10, value = 5) #NEW

    st.header("Question 4")

    question4 = st.radio ("Who is your favorite musical artist?", ["Lil Durk", "Lil Wayne", "NBA YoungBoy", "G3 Gelo"])

    if question4 == "NBA YoungBoy":
         st.toast("WHAT ARE YOU DOING???????") # EXTRA CREDIT
            
    st.header("Question 5")

    question5 = st.multiselect("Choose your 2 favorite basketball players:", ["LeGoat", "Kevin Durant", "Ant","Wemby", "Jokic", "Caitlin Clark", "Sue Bird", "Yao Ming", "Shaq", "Larry Bird","Jimmy Butler"], max_selections = 2) #NEW
    nba_team = "Not selected yet"
    if len(question5) == 2:
        if "LeGoat" in question5:
            nba_team = "Los Angeles Lakers"
        elif "Kevin Durant" in question5:
            nba_team = "Houston Rockets"
        elif "Ant" in question5:
            nba_team = "Minnesota Timberwolves"
        elif "Wemby" in question5:
            nba_team = "San Antonio Spurs"
        elif "Jokic" in question5:
            nba_team = "Denver Nuggets"
        elif "Caitlin Clark" in question5:
            nba_team = "Indiana Fever"
        elif "Sue Bird" in question5:
            nba_team = "Seattle Storm"
        elif "Yao Ming" in question5:
            nba_team = "Houston Rockets"
        elif "Shaq" in question5:
            nba_team = "Los Angeles Lakers"
        elif "Larry Bird" in question5:
            nba_team = "Boston Celtics"
        elif "Jimmy Butler" in question5:
            nba_team = "Golden State Warriors"
    
        st.header("Your NBA Team")
        st.subheader(nba_team)
    else:
        st.write("Choose two players to find your NBA team!")

    
    melo_score = 0
    gelo_score = 0
    lonzo_score = 0
    lavar_score = 0

    if question1 == "Peach Cobbler":
        melo_score += 1
    elif question1 == "Big Baller Breakfast":
        lavar_score += 1
    elif question1 == "PB & J":
        lonzo_score += 1
    elif question1 == "Caramel Cookies":
        gelo_score += 1

    if question2 % 4 == 0:
        melo_score += 1
    elif question2 % 4 == 1:
        gelo_score += 1
    elif question2 % 4 == 2:
        lonzo_score += 1
    else:
        lavar_score += 1

    if question3 <= 3:
        lavar_score += 1
    elif question3 <= 5:
        lonzo_score += 1
    elif question3 <= 7:
        gelo_score += 1
    else:
        melo_score += 1

    if question4 == "Lil Durk":
        melo_score += 1
    elif question4 == "Lil Wayne":
        lonzo_score += 1
    elif question4 == "NBA YoungBoy":
        gelo_score += 1
    elif question4 == "G3 Gelo":\
         lavar_score += 1

    if melo_score >= gelo_score and melo_score >= lonzo_score and melo_score >= lavar_score:
        ball_fam = "Melo"
    elif gelo_score >= melo_score and gelo_score >= lonzo_score and gelo_score >= lavar_score:
        ball_fam = "Gelo"
    elif lonzo_score >= melo_score and lonzo_score >= gelo_score and lonzo_score >= lavar_score:
        ball_fam = "Lonzo"
    else:
        ball_fam = "Lavar"

    st.header("Your Results")

    st.write("You are:")

    if ball_fam == "Melo":
        st.subheader("MELO")
    elif ball_fam == "Gelo":
        st.subheader("GELO")
    elif ball_fam == "Lonzo":
        st.subheader("LONZO")
    else:
        st.subheader("LAVAR")

    st.write("Your NBA team is:")
    st.subheader(nba_team)

    st.header("Want to learn more about your Ball family member?") # EXTRA CREDIT

    with st.expander("Lamelo:"):
        st.write("Lamelo Ball was drafted to the Hornets in 2020 as the 3rd overall pick, and was recently traded to the Timberwolves. He enjoys video games, NFTs, and has only just been media trained.")
    with st.expander("LiAngelo:"):
        st.write("Liangelo Ball played professional basketball as well, but his most famed achievement is his song TWEAKER, which hit the charts in several countries in 2025.")
    with st.expander("Lonzo:"):
        st.write("Lonzo Ball is a current free agent with the NBA, but has played for the Bulls, the Lakers, the Caveliers, and the Pelicans. He regrets his father's influence :(")
    with st.expander("Lavar:"):
        st.write("Where can you even start with Lavar- he's incredibly charismatic and humorous, but also has one of the steepest egos in all of Basketball history. He relentlessly trained his three sons to make it to the NBA, succeeded, and built a million-dollar brand along the way. He recently lost his foot to diabetes, but is convinced he can grow it back.")
            
with tab2:
    st.write("Take this short quiz to find out whether you're more of a Gelo, Melo, Lonzo, or Lavar!")

    st.write("You will also figure out which NBA team you're most likely to play for.")

    st.write("This quiz was developed based on hours of Ball in the family film review.")

    st.write("Your results will indicate which psychological profile you best correspond to in the Ball family. Your data will be shared with Big Baller Brand, as Lavar is looking to start a network of GT students to help him grow back his leg.")
    




