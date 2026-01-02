from google import genai
from flask import Flask, request,jsonify, render_template
client= genai.Client(api_key="Gemini API Key")
app=Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/chat", methods=["POST"])
def chat():
    prompt=request.json["message"]
    response =client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
    )
    return jsonify({"reply": response.text})
app.run(port="2000")
