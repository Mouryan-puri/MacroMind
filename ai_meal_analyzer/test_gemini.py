# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Automatically picks up GEMINI_API_KEY from environment
# api_key = os.getenv("GEMINI_API_KEY")

# client=genai.Client(api_key=api_key)

# response = client.models.generate_content(
#     model="gemini-3.5-flash",
#     contents="what is 2+2?",
# )

# print(response.text)


from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

# genai.client typically refers to the primary interface object provided by the official Google Gen AI SDK (and similar libraries). Its primary purpose is to act as the main "bridge" or controller connecting your application code to Generative AI models like Gemini.

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

meal = "chicken and rice along with broccoli"

prompt = f"""
You are a meal analyzer for Indian food.
The user ate: {meal}

Extract the individual food items from this meal.
Return ONLY a JSON array of ingredient names, nothing else.
Example: ["roti", "dal", "curd"]
"""

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
)
print(response.text)