# GenAI Chatbot 🤖

A Generative AI chatbot application developed using Python and Flask, powered by the Gemini API.  
This project demonstrates how to integrate Generative AI into a web application with a simple and interactive user interface.

---

## ✨ Project Overview

The GenAI Chatbot allows users to interact with an AI model through a web interface.  
The backend handles user requests and communicates with the Gemini API, while the frontend displays responses in real time.

This project was built as part of **Generative AI training** to understand:
- API integration
- Backend–frontend communication
- Virtual environments
- Dependency management
- GitHub project workflow

---
## 🚀 Features

- AI-powered chatbot using Gemini API
- Flask-based backend
- Simple and interactive UI
- Beginner-friendly project structure
- Proper environment and dependency management

---

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **Backend Framework:** Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **AI Model:** Gemini API  
- **Environment Management:** Miniconda, Python Virtual Environment (`.venv`)  
- **Version Control:** Git & GitHub  

---

## 🧪 Environment & Setup Details

### 🔹 Miniconda
- Miniconda is used to manage the base Python environment.
- The project was executed inside the Conda base environment.
### 🔹 Python Virtual Environment
- A Python virtual environment (`.venv`) is created inside the project folder.
- This isolates project dependencies and avoids conflicts with system Python packages.

---
## ⚙️ How to Run the Project Locally

Follow the steps below to run the chatbot on your system.

### 1️⃣ Clone the Repository


git clone https://github.com/shahanthi-velagala/genai-chatbot.git


cd genai-chatbot

###2️⃣ Create Virtual Environment


python -m venv .venv

###3️⃣ Activate Virtual Environment

Windows (PowerShell):

.venv\Scripts\Activate.ps1


After activation, you will see:

(.venv)

in the terminal.

4️⃣ Install required libraries


pip install flask google-genai


5️⃣ Run the Application


python main.py

6️⃣ Access the Application in Browser



Open your browser and go to:

text

http://localhost:2000

---

📝 Notes

For simplicity, the frontend (HTML, CSS, and JavaScript) is implemented in a single index.html file.

The project is intended for learning and demonstration purposes.

Future improvements may include modular frontend structure and enhanced UI.
