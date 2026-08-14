# Welcome to MacroMind

AI Meal Tracker is a full-stack Flask web application that helps users log meals in natural language and track daily nutrition goals. Users can enter meals like "eggs, toast, and coffee," and the app uses the Gemini API to estimate calories, protein, carbohydrates, and fat.

## Features

- Log meals using natural-language descriptions
- Estimate calories, protein, carbs, and fat using the Gemini API
- Categorize meals by breakfast, lunch, snack, and dinner
- Set daily nutrition goals for calories and macronutrients
- View daily calorie totals, remaining calories, and macro progress
- Store meals and goals persistently using SQLite
- Delete logged meals
- Responsive dashboard built with HTML, CSS, and Jinja templates

## Tech Stack

- Python
- Flask
- SQLite
- Jinja
- HTML/CSS
- Gemini API
- python-dotenv

## Project Overview

The app follows a server-rendered Flask architecture. Users submit meals through an HTML form, Flask sends the meal description to the Gemini API, parses the returned JSON nutrition estimate, stores the result in SQLite, and renders the updated dashboard using Jinja templates.

Basic flow:

```text
User enters meal
→ Flask receives form data
→ Gemini API estimates nutrition
→ Flask parses JSON response
→ Meal is saved in SQLite
→ Dashboard updates with totals and progress
```

## Database

The application uses SQLite with two main tables:

```text
meals
- id
- meal_type
- meal_name
- meal_description
- calories
- protein
- carbs
- fat
- date
- created_at

daily_goals
- goal_date
- calories
- protein
- carbs
- fat
```

## Setup

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
python3 app.py
```

Open the app in your browser:

```text
http://127.0.0.1:5000
```

## Environment Variables

This project requires a Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Do not commit your `.env` file to GitHub.

## What I Learned

- Building Flask routes for GET and POST requests
- Handling HTML form data with Flask
- Using Jinja templates to render dynamic data
- Integrating an external AI API into a Python web app
- Parsing JSON responses from an API
- Designing and querying SQLite tables
- Calculating daily calorie and macronutrient totals
- Structuring a full-stack Python project
- Styling a responsive dashboard with HTML and CSS
- Debugging API responses, database writes, and template rendering

## Future Improvements

- Add user authentication
- Add meal editing
- Add nutrition history by date
- Improve Gemini API error handling
- Add automated tests with pytest
- Deploy the application online
- Add PostgreSQL support for production use