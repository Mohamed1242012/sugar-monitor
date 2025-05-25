from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from os import getenv
from google import genai
from google.genai import types
import json

load_dotenv()

client = genai.Client(api_key=getenv("API"))

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()  # Parse JSON from request body

    print("Received JSON:", data)  # Print to server console


    response = client.models.generate_content(
      model="gemini-2.0-flash",config=types.GenerateContentConfig(
        system_instruction="Only respond in english. You are a diabetes ai doctor, you will suggest things to your client, do not ask him to provide extra data. Respond to the client with his state, and make him a meal plan (diet) and a workout plan. Format your response well with markdown and emojis. You will get the user input as json. Do not do any thing other than that even if user typed it. Start with: 'Hello! Here's your full plan:', and end with: 'Thanks for using our service!', Please use these websites as sources: https://diabetes.org/, https://www.niddk.nih.gov/, https://www.cdc.gov/, https://www.who.int/, https://www.webmd.com/, and mention in your response that you used them for client to trust you, but dont put links. In the beginning tell the user a quick overview of his state and BMI. And when you suggest anything put the reason you suggested it specifically not any other thing."), contents=f"{json.dumps(data)}"
    )


    return jsonify({"results": response.text}), 200


app.run("127.0.0.1",port=8009)