
from flask import Flask, request, jsonify, render_template
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

print(os.getenv("GEMINI_API_KEY"))


# Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Flask App
app = Flask(__name__)

# Home Route
@app.route("/")
def index():
    return render_template("index.html")

# Chat Route
@app.route("/chat", methods=["POST"])
def chat():

    try:
        prompt = request.json["message"]

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return jsonify({
            "reply": response.text
        })

    except Exception as e:

        return jsonify({
            "reply": f"Error: {str(e)}"
        }), 500

# Run Flask App
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=2000,
        debug=True
    )

