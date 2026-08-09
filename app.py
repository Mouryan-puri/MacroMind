# [app.py] is the main backend.
# It does these jobs:
    # imports Flask tools:
        # Flask to create the app
        # render_template to show HTML files
        # request to get form data

    # imports Gemini:
        # from google import genai

    # loads environment variables:
        # load_dotenv()
        # os.getenv("GEMINI_API_KEY") - function that fetch api key from env

    # creates the Flask app:
        # app = Flask(__name__)

    # defines the homepage route /
    # defines the /analyze route for form submission
    # sends the meal text to Gemini
    # renders result.html with the returned output
    # starts the server using app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from google import genai
from dotenv import load_dotenv
import os
import json
from database import init_db, save_meal, get_meals_for_date
from datetime import date

load_dotenv() 
api_key = os.getenv("GEMINI_API_KEY")

# creates your flask web application, similar to how tk.Tk() created your window
app = Flask(__name__)

# this is new syntax called a decorator. It means "when someone visits this URL path, run the function right below it." "/" means the homepage (like localhost:5000/)
@app.route("/")

#  the function that runs, and whatever it returns is what shows up in the browser
def home():
    # return "<h1> Meal analyzer </h1> <p> Type your value below </p>"

    # render_template("index.html") — Flask automatically looks inside a folder called templates for your HTML files. This is a strict rule — the folder MUST be named templates, Flask looks for it by default.
    today=date.today().isoformat()
    meals=get_meals_for_date(today)

    return render_template("index.html", meals=meals)

# there is also a route called /analyze
# but it is meant to receive submitted form data
@app.route("/meals", methods=["POST"])
def log_meal():
    # meal = request.form["meal"]  # grabs the value typed in the box, using the 'name' from HTML
    # return f"<h1>You typed: {meal}</h1><p>Score: 75 (fake for now)</p>"

    meal=request.form.get("meal")
    meal_type=request.form.get("meal_type")

    # Gemini client that uses the API key to perform any task
    client=genai.Client(api_key=api_key)

    prompt = f"""
    You are a meal-tracking assistant.

    The user logged this meal:
    {meal}

    Estimate the nutrition for this meal.

    Return only one valid JSON object.
    Do not include Markdown, code fences, explanations, or extra text.

    Use exactly this structure:

    {{
        "meal_name": "short, clear meal name",
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0
    }}

    Rules:
    - calories must be a whole number in kcal.
    - protein, carbs, and fat must be whole numbers in grams.
    - Make reasonable estimates when portion sizes are not provided.
    """

    # function that sends your prompt to AI model and gets answer back
    # basically, this take this input text, send it to gemini, let gemini think, and gets the response back
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    today=date.today().isoformat()# will store today's date

    data=response.text
    data=json.loads(data) # this loads the response and convert this into json formatting

    print(data)
    save_meal(meal, meal_type, data, today)

    # return render_template("result.html", meal=meal, data=data)

    #basically 
    # url_for("home")-> finds the correct url connected to the function home
    # redirect() simply redirects to that corresponding url 
    return redirect(url_for("home"))



# What it does: It checks if a Python file is being run directly as the main program or if it is being imported as a helper module by another file.How it works: Python automatically changes a hidden variable called __name__. If you run the file directly, Python sets it to "__main__". If you import the file, Python changes it to the file's actual name.Why it is needed: It acts as a safety guard. Without it, any loose code or print statements in a file will accidentally run the exact moment you try to import and reuse that file in a new project.
if __name__=="__main__":
    # make sure database table exists and if not exists, make one using initialization function in database.py
    init_db()

    # starts the server. debug=True auto-reloads when you change code, and shows helpful errors in the browser
    app.run(debug=True)