from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)

def chatgpt_request(prompt):
   

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.3,
    )

    return response.choices[0].text.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    itinerary = None
    if request.method == "POST":
        destination = request.form["destination"]
        days = request.form["days"]
        interests = request.form["interests"]

        prompt = f"Create a detailed itinerary for a {days}-day vacation in {destination} for someone interested in {interests}. Include daily activities, restaurant recommendations, and sightseeing spots. If your recommendation involves a drive then specify how long it is and the best way of getting there:"
        itinerary = chatgpt_request(prompt)

    return render_template("index.html", itinerary=itinerary)

if __name__ == "__main__":
    app.run(debug=True)

