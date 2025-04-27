# file: project3_advanced.py

import streamlit as st

# Initialize session state
if "low" not in st.session_state:
    st.session_state.low = 1
if "high" not in st.session_state:
    st.session_state.high = 100
if "guess" not in st.session_state:
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.markdown("<h1 style='text-align: center; color: #FF5722;'>🤖 Computer Guesses Your Number (Advanced)</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Think of a number between <b>1</b> and <b>100</b> and guide me! 🎯</h4>", unsafe_allow_html=True)

if not st.session_state.game_over:
    st.subheader(f"My guess is: 🔥 **{st.session_state.guess}**")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Too Low ⬆️"):
            st.session_state.low = st.session_state.guess + 1
            st.session_state.attempts += 1
    with col2:
        if st.button("Correct 🎯"):
            st.success(f"🎉 Hurray! I guessed your number in {st.session_state.attempts + 1} tries.")
            st.balloons()
            st.session_state.game_over = True
    with col3:
        if st.button("Too High ⬇️"):
            st.session_state.high = st.session_state.guess - 1
            st.session_state.attempts += 1

    # Update the guess
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
else:
    if st.button("Play Again 🔄"):
        st.session_state.low = 1
        st.session_state.high = 100
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.success("New game started! Think of another number! 🚀")

# Show progress
st.progress(min(st.session_state.attempts * 10 / 100, 1.0))
st.caption(f"Number of Attempts: {st.session_state.attempts}")
