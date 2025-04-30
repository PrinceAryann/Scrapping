import requests
from bs4 import BeautifulSoup
import csv
import re
import os

# URL of Hacker News front page
URL = "https://news.ycombinator.com/news"

# Send an HTTP GET request to the page
response = requests.get(URL)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all the score elements (e.g., "42 points")
scores = soup.find_all("span", class_="score")

# Extract IDs and score numbers, clean and sort them by score descending
score_data = [
    [re.sub("score_", "", score.get("id")), score.text.split()[0]]
    for score in scores
]
score_data.sort(key=lambda x: int(x[-1]), reverse=True)

# Save path (replace with your own path if necessary)
SAVE_PATH = os.path.join("your", "path", "Data.csv")  # 🔁 Update this as needed

# Write data to CSV
with open(SAVE_PATH, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link", "Points"])  # Column headers

    # Loop through the sorted score data
    for score_entry in score_data:
        post_id = score_entry[0]
        points = score_entry[1]

        # Find the row corresponding to the post ID
        title_row = soup.find("tr", id=post_id)
        if title_row:
            title_element = title_row.select_one("span.titleline")
            if title_element:
                title_text = title_element.get_text(strip=True)
                link = title_element.a["href"] if title_element.a else "No Link"
                writer.writerow([title_text, link, points])  # Write to CSV

print("✅ Data Scraped & Saved Successfully!")
