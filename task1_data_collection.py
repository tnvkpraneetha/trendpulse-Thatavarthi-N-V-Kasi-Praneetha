
# 1 — Make the API Calls

import requests
import time

#Categories detailes based on which we need to segregate stories
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "book", "show", "award", "streaming"]
}

headers = {"User-Agent": "TrendPulse/1.0"}

# Fetching story IDs
ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()

# Store fetched stories temporarily
stories = []

for category, keywords in categories.items():

    count = 0

    for story_id in ids:

        if count >= 25:
            break

        url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

        res = requests.get(url, headers=headers)

        if res.status_code != 200:
            print(f"Failed to fetch story {story_id}")
            continue

        story = res.json()
        title = story.get("title", "").lower()

        for word in keywords:
            if word in title:
                story["category"] = category   # assign category
                stories.append(story)
                count += 1
                break

        
    # Sleep AFTER finishing one category
    time.sleep(2)


#2 — Extract the Fields
    
from datetime import datetime

final_data = []

category_count = {cat: 0 for cat in categories}

for story in stories:

    category = story.get("category")

    # Skip if already 25 collected
    if category_count[category] >= 25:
        continue

    # Extracting required fields
    record = {
        "post_id": story.get("id"),
        "title": story.get("title"),
        "category": category,
        "score": story.get("score", 0),
        "num_comments": story.get("descendants", 0),
        "author": story.get("by"),
        "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    final_data.append(record)
    category_count[category] += 1

#3 — Save to a JSON File
    
import os
import json

if not os.path.exists("data"):
    os.makedirs("data")

date_str = datetime.now().strftime("%Y%m%d")
filename = f"data/trends_{date_str}.json"

with open(filename, "w") as f:
    json.dump(final_data, f, indent=4)

print("File saved as:", filename)
print("Total stories collected:", len(final_data))
