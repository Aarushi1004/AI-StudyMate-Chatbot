from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
import os


# Load API key
load_dotenv()


# Gemini connection
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    user_message = data["message"]

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message
        )

        bot_reply = response.text


    except Exception as e:

        print("GEMINI ERROR:", e)

        bot_reply = (
            "AI connection problem 🤖"
        )


    return jsonify(
        {
            "reply": bot_reply
        }
    )


if __name__ == "__main__":
    app.run(debug=True)