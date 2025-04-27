
import streamlit as st
import random

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎯 Guess the Number (Advanced)</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>I'm thinking of a number between <b>1</b> and <b>100</b>. Can you guess it?</h4>", unsafe_allow_html=True)

# Input Section
guess = st.number_input("Enter your guess below 👇", min_value=1, max_value=100, step=1, key="guess_input")

# Action Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Submit Guess 🎯"):
        if not st.session_state.game_over:
            st.session_state.attempts += 1
            if guess < st.session_state.number:
                st.warning("🔻 Too Low! Try a higher number.")
            elif guess > st.session_state.number:
                st.warning("🔺 Too High! Try a lower number.")
            else:
                st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} tries.")
                st.balloons()
                st.session_state.game_over = True
with col2:
    if st.button("Restart Game 🔄"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.success("Game Restarted! Think of a new number! 🚀")

# Progress Display
st.progress(min(st.session_state.attempts * 10 / 100, 1.0))
st.caption(f"Number of Attempts: {st.session_state.attempts}")

