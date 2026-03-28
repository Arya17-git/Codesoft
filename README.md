# Codesoft
internship
.

🍓 Berry Bot: A Python-Powered Virtual Assistant
Berry is a lightweight, rule-based chatbot designed to provide quick information and friendly conversation through a modern web interface. Built during my Python development internship, this project focuses on Intent Mapping, Natural Language Processing (NLP) basics, and Web Deployment.

🚀 Features
Natural Conversational Flow: Handles greetings, identity, and common FAQs using synonym-based trigger tuples.

Real-time Utilities: Fetches current system time and date dynamically.

Dynamic Variability: Uses randomization to ensure the bot feels less scripted and more engaging.

Web Interface: Fully interactive UI built with Streamlit, moving beyond the traditional terminal.

Robust Matching: Implements tokenization logic to prevent "sub-string" confusion (e.g., distinguishing between "hi" and "hai").

🛠️ Tech Stack
Language: Python 3.12

Framework: Streamlit

Libraries: random, datetime, re (Regex)

📁 Project Structure
Plaintext
├── app.py              # Main application logic and UI
├── berry_brain.py      # Dictionary containing intents and responses
├── requirements.txt    # List of dependencies for cloud deployment
└── README.md           # Project documentation
⚙️ How to Run Locally
Clone the repository:

Bash
git clone https://github.com/YOUR_USERNAME/berry-bot.git
Install the requirements:

Bash
pip install -r requirements.txt
Run the application:

Bash
python -m streamlit run app.py
