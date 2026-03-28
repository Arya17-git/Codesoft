import streamlit as st
import random
import datetime

# --- 1. YOUR BRAIN 
berry_brain={
    ("hi","hii","hiiee","hiii""hello","hola","hey","namste","hiii!","yo","sup"):["hii how are you","hello! How can I help you today?","Hey there!","Namaste! Kaise ho?"],
    ("how are you","how do you do","kaise ho","how do you do","haal-chaal","tbiyat"):["I am fine","Mei tho bdhiya hu","doing greaat!How about you?"],
    ("name","what should I call you?","Who are you"):["My name is Berry"],
    ("help","madat","support","need"):["How can I assist you?"],
    ("joke", "funny","make me smile"): ["What do you call a fake noodle? An Impasta!"],
    ("bye","see you later","goodbye","amigos","alvida","tata"):["Goodbye! Have a great day! 🍓"],
    ("weather", "temperature", "rain"): ["I don't have a window, but I hope it's sunny! ☀️","It feels like 25°C in my server room! 🌡️","I'm a bot, so I'm always dry and cozy. ☔"]
    }

# --- 2. THE WEB INTERFACE ---
st.set_page_config(page_title="Berry Bot", page_icon="🍓")
st.title("Berry 🍓")
st.subheader("Your Friendly Python Assistant")

# Initialize chat history (This is Berry's "Session Memory")
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 3. THE INPUT LOGIC ---
if prompt := st.chat_input("Say something to Berry..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    user_message = prompt.lower().strip()
    response = ""

    # --- 4. THE SEARCH ENGINE (Your Logic) ---
    if "time" in user_message:
        response = f"The current time is: {datetime.datetime.now().strftime('%H:%M:%S')} 🍓"
    elif "date" in user_message:
        response = f"Today's date is: {datetime.datetime.now().strftime('%Y-%m-%d')} 🍓"
    else:
        found_match = False
        for triggers, replies in berry_brain.items():
            if any(word in user_message.split() for word in triggers):
                response = random.choice(replies)
                found_match = True
                break
        
        if not found_match:
            response = "I'm sorry, I don't understand that yet. 🍓"

    # Display Berry's response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})