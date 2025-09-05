# Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application

import requests

API_KEY = os.getenv("NEWS_API_KEY")
if not API_KEY:
    raise RuntimeError("API key not found in environment. Please set NEWS_API_KEY.")

BASE_URL = "https://newsapi.org/v2/everything"

categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]

userInput = input(f"Enter the category from {categories} you want the News for :\n").lower()

if userInput in categories:
    url = f"{BASE_URL}?q={userInput}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    for article in data["articles"]:
        print("\nTitle:", article["title"])
        print("Description:", article.get("description", "No description"))
        print("URL:", article["url"])
        print("-" * 50)
else:
    print("Invalid category!")

