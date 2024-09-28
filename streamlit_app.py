import streamlit as st

st.title("🎲 Bunrawat Chat bot  🃏 ")
if user_input := st.text_input("You: ", placeholder="Type your message here..."):
    st.write(f"User Input: {user_input}")