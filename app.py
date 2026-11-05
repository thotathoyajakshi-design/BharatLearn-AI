import streamlit as st

st.set_page_config(
    page_title="BharatLearn AI",
    page_icon="📚",
    layout="wide"
)

st.title("🇮🇳 BharatLearn AI")
st.subheader("A Multilingual Smart Learning Assistant")
st.write("Making learning simple and accessible for every student.")

st.divider()

# Sidebar
st.sidebar.title("📚 Navigation")
page = st.sidebar.radio(
    "Choose a section",
    ["Dashboard", "Learn", "Practice Quiz", "About"]
)

# Sample learning library
explanations = {
    "probability": {
        "English": "Probability measures how likely an event is to happen. Example: A coin has a 1/2 chance of landing heads.",
        "తెలుగు": "ఒక సంఘటన జరిగే అవకాశం ఎంత ఉందో తెలిపేది సంభావ్యత.",
        "हिन्दी": "प्रायिकता बताती है कि किसी घटना के होने की कितनी संभावना है।"
    },
    "python": {
        "English": "Python is a programming language used to build software, websites and applications.",
        "తెలుగు": "పైథాన్ అనేది సాఫ్ట్‌వేర్ మరియు అప్లికేషన్లు తయారు చేయడానికి ఉపయోగించే ప్రోగ్రామింగ్ భాష.",
        "हिन्दी": "पाइथन एक प्रोग्रामिंग भाषा है जिसका उपयोग सॉफ्टवेयर और ऐप बनाने में होता है।"
    },
    "computer": {
        "English": "A computer is an electronic device that processes data and produces information.",
        "తెలుగు": "కంప్యూటర్ అనేది డేటాను ప్రాసెస్ చేసి సమాచారాన్ని అందించే ఎలక్ట్రానిక్ పరికరం.",
        "हिन्दी": "कंप्यूटर एक इलेक्ट्रॉनिक उपकरण है जो डेटा को प्रोसेस करके जानकारी देता है।"
    }
}

# Dashboard
if page == "Dashboard":
    st.header("🏠 Welcome to BharatLearn AI")

    col1, col2, col3 = st.columns(3)

    col1.metric("Languages", "3")
    col2.metric("Sample Topics", "3")
    col3.metric("Quiz Questions", "3")

    st.info("Learn concepts in English, Telugu and Hindi.")
    st.write("Use the sidebar to explore learning and quiz sections.")

# Learn section
elif page == "Learn":
    st.header("📖 Learn a Topic")

    language = st.selectbox(
        "Choose your language",
        ["English", "తెలుగు", "हिन्दी"]
    )

    topic = st.text_input("Enter a topic")

    if st.button("✨ Explain Topic"):
        key = topic.strip().lower()

        if key in explanations:
            st.success("Simple Explanation")
            st.write(explanations[key][language])
        elif key:
            st.warning("This sample library does not contain that topic yet.")
            st.write("Try Probability, Python or Computer.")
        else:
            st.warning("Please enter a topic.")

# Quiz section
elif page == "Practice Quiz":
    st.header("📝 Practice Quiz")
    st.write("Test your understanding!")

    answers = {
        "What is the probability of getting heads in a fair coin toss?":
            ["1/2", "1/3", "1", "0"],
        "Which language is commonly used for AI development?":
            ["Python", "HTML", "CSS", "None"],
        "What does CPU stand for?":
            ["Central Processing Unit", "Computer Personal Unit",
             "Central Program Utility", "Control Processing User"]
    }

    correct_answers = ["1/2", "Python", "Central Processing Unit"]

    selected = []

    for question, options in answers.items():
        st.write("**" + question + "**")
        selected.append(st.radio(
            "Choose your answer:",
            options,
            key=question
        ))

    if st.button("Check My Score"):
        score = sum(
            1 for i in range(3)
            if selected[i] == correct_answers[i]
        )

        st.success(f"Your score: {score}/3")

        if score == 3:
            st.balloons()
            st.write("Excellent work!")
        else:
            st.info("Good attempt! Keep practising.")

# About section
elif page == "About":
    st.header("ℹ️ About BharatLearn AI")

    st.write("""
    BharatLearn AI is a multilingual learning assistant
    designed to make education easier for students.

    Main features:
    - Multilingual sample explanations
    - English, Telugu and Hindi
    - Practice quizzes
    - Instant quiz scores

    Project Theme: AI for Bharat
    """)

st.divider()
st.caption("BharatLearn AI | Hackathon Project | Team VISIONX")