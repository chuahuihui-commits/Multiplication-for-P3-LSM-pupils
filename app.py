import streamlit as pd
import streamlit as st
import random

# Set up page configuration
st.set_page_config(
    page_title="Space Multiplier!",
    page_icon="🚀",
    layout="centered"
)

# Custom CSS for kid-friendly styling (larger fonts and bright colors)
st.markdown("""
    <style>
    .big-font {
        font-size: 40px !important;
        font-weight: bold;
        text-align: center;
        color: #2E86C1;
    }
    .score-font {
        font-size: 24px !important;
        font-weight: bold;
        color: #27AE60;
    }
    </style>
    """, unsafe_allowed_html=True)

# Initialize session state variables if they don't exist
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'num1' not in st.session_state:
    st.session_state.num1 = random.randint(100, 999) # 3-digit number
if 'num2' not in st.session_state:
    st.session_state.num2 = random.randint(2, 9)     # 1-digit number
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""
if 'feedback_type' not in st.session_state:
    st.session_state.feedback_type = ""

# Function to generate a new question
def next_question():
    st.session_state.num1 = random.randint(100, 999)
    st.session_state.num2 = random.randint(2, 9)
    st.session_state.answered = False
    st.session_state.feedback = ""
    st.session_state.feedback_type = ""

# --- App Layout ---

st.title("🚀 Space Multiplier Adventure!")
st.write("Welcome, Space Cadet! Help steer the rocket by solving the multiplication questions below.")

# Display current score
st.markdown(f"<p class='score-font'>⭐ Current Score: {st.session_state.score}</p>", unsafe_allowed_html=True)
st.markdown("---")

# Display the question prominently
st.markdown(f"<p class='big-font'>{st.session_state.num1}  ×  {st.session_state.num2}  =  ?</p>", unsafe_allowed_html=True)

# Form for user input to prevent accidental reloads on typing
with st.form(key='math_form', clear_on_submit=True):
    user_answer = st.number_input("Type your answer here:", min_value=0, step=1, value=None, placeholder="???")
    submit_button = st.form_submit_button(label='🚀 Check Answer')

# Logic handling when the user submits an answer
if submit_button:
    if user_answer is None:
        st.warning("Please type a number before checking!")
    else:
        correct_answer = st.session_state.num1 * st.session_state.num2
        st.session_state.answered = True
        
        if user_answer == correct_answer:
            st.session_state.score += 10
            # List of fun positive feedback phrases
            positive_reinforcement = random.choice([
                "🌟 Spectacular! You're a multiplication superstar!",
                "🚀 Correct! Rocket boosters engaged!",
                "🎉 Brilliant job! Your brain power is out of this world!",
                "🎯 Direct hit! Way to go!"
            ])
            st.session_state.feedback = positive_reinforcement
            st.session_state.feedback_type = "success"
        else:
            # Positive/Encouraging feedback for incorrect responses
            encouraging_feedback = random.choice([
                f"🛸 So close! Mistakes help our brains grow. The correct answer was {correct_answer}. Let's try another one together!",
                f"✨ Nice try, Cadet! You're learning fast. The right answer was {correct_answer}. Keep pushing!",
                f"💪 Good effort! Practice makes perfect. The secret code was {correct_answer}. Ready for the next challenge?"
            ])
            st.session_state.feedback = encouraging_feedback
            st.session_state.feedback_type = "info"

# Display feedback from the state
if st.session_state.feedback:
    if st.session_state.feedback_type == "success":
        st.success(st.session_state.feedback)
        st.balloons()
    elif st.session_state.feedback_type == "info":
        st.info(st.session_state.feedback)

# Next Question Button
if st.session_state.answered:
    st.button("👉 Next Question", on_click=next_question)
