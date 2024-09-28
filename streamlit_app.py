import streamlit as st
import google.generativeai as genai
import numpy as np

# Create by  Bunrawat Charoenyuennan DADS
st.title("☕ Barista Chatbot 666 ")
st.subheader("Presented By Bunrawat Charoenyuennan")

# Capture Gemini API Key
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")
# Initialize the Gemini Model
if gemini_api_key:
    try:
        # Configure Gemini with the provided API Key
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")
        st.success("Gemini API Key successfully configured.")
    except Exception as e:
        st.error(f"An error occurred while setting up the Gemini model: {e}")

# Initialize session state for storing chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Initialize with an empty list

# Display previous chat history
for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)

# Welcome message for the first interaction
if len(st.session_state.chat_history) == 0:
    welcome_message = (
        "Welcome to our Coffee Shop! ☕ 666 I'm your friendly barista. "
        "I can help you choose the perfect coffee. "
        "You can ask me for recommendations based on your mood, taste preferences, or any specific type of coffee you like!"
    )
    st.session_state.chat_history.append(("assistant", welcome_message))
    st.chat_message("assistant").markdown(welcome_message)

# Capture user input and generate bot response
if user_input := st.chat_input("Type your coffee preferences or any question about our menu here..."):
    # Store and display user message
    st.session_state.chat_history.append(("user", user_input))
    st.chat_message("user").markdown(user_input)
    
    # Use Gemini AI to generate a barista-style response
    if model:
        try:
            # Modify user input to be more specific for coffee recommendations
            query = f"Act as a barista and recommend a coffee drink based on this preference: {user_input}"
            response = model.generate_content(query)
            bot_response = response.text
            
            # Store and display the bot response
            st.session_state.chat_history.append(("assistant", bot_response))
            st.chat_message("assistant").markdown(bot_response)
        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")
