# GenAI Chatbot 🤖

A modern AI-powered chatbot web application built using **Python**, **Flask**, and the **Google Gemini API**.
The project features a professional ChatGPT-style interface with real-time AI responses, markdown rendering, and responsive UI design.

---

# ✨ Project Overview

This project demonstrates how to integrate Generative AI into a full-stack web application using Flask and Gemini AI.

Users can interact with the AI through a modern chatbot interface that supports:

* Structured responses
* Headings and bullet points
* Numbered lists
* Code block formatting
* Real-time AI conversations

The backend communicates with the Gemini API, while the frontend provides a smooth and professional user experience similar to ChatGPT.

---

# 🚀 Features

* 🤖 AI-powered chatbot using Gemini API
* 🎨 Modern glassmorphism UI design
* 🌙 Professional dark theme
* 📝 Markdown-rendered AI responses
* 📱 Fully responsive interface
* ⚡ Real-time messaging experience
* 🔒 Secure API key management using `.env`
* 🧠 Typing animation and smooth UI effects
* 🛠️ Flask backend integration

---

# 🛠️ Technologies Used

## Backend

* Python
* Flask
* Google Gemini API
* python-dotenv

## Frontend

* HTML5
* CSS3
* JavaScript
* Marked.js (Markdown Rendering)
* Lucide Icons

## Tools & Environment

* Git & GitHub
* VS Code
* Miniconda
* Python Virtual Environment (`.venv`)

---

# 📂 Project Structure

```bash
genai-chatbot/
│
├── main.py
├── .env
├── .gitignore
│
├── templates/
│   └── index.html
│
└── README.md
```

---

# 🔐 Environment Variables

This project uses a `.env` file to securely store the Gemini API key.

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

⚠️ Never upload `.env` to GitHub.

---

# ⚙️ How to Run the Project Locally

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/shahanthi-velagala/genai-chatbot.git
```

```bash
cd genai-chatbot
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

---

## 3️⃣ Activate Virtual Environment

### Windows (PowerShell)

```bash
.venv\Scripts\Activate.ps1
```

After activation, you will see:

```bash
(.venv)
```

in the terminal.

---

## 4️⃣ Install Required Libraries

```bash
pip install flask google-genai python-dotenv
```

---

## 5️⃣ Run the Application

```bash
python main.py
```

---

## 6️⃣ Open in Browser

Go to:

```text
http://localhost:2000
```

---

# 💡 Key Learning Outcomes

This project helped in understanding:

* Generative AI integration
* Flask backend development
* Frontend–backend communication
* API handling and security
* Environment variables
* Virtual environments
* Git & GitHub workflow
* Modern UI/UX implementation
* Markdown rendering in chat applications

---

# 🔮 Future Improvements

Possible future enhancements include:

* User authentication
* Chat history storage
* Voice input support
* Multiple AI model support
* Database integration
* File upload support
* Streaming AI responses
* Deployment on cloud platforms

---

# 📌 Notes

* The frontend is currently implemented inside a single `index.html` file for simplicity.
* The project is intended for learning, portfolio building, and AI integration practice.
* API keys are managed securely using `.env`.

---

# 👩‍💻 Author

**Shahanthi Velagala**
B.Tech Student — Vishnu Institute of Technology

GitHub:
https://github.com/shahanthi-velagala

---

