from selenium import webdriver
import time
import json
import re
import pandas as pd

driver = webdriver.Edge()

driver.get("https://www.imdb.com/chart/top/")
time.sleep(10)

html = driver.page_source
driver.quit()

# JSON-LD script extract karo
match = re.search(
    r'<script type="application/ld\+json">(.*?)</script>',
    html,
    re.DOTALL
)

if match:
    data = json.loads(match.group(1))

    movies = []

    for item in data["itemListElement"]:
        movie = item["item"]["name"]
        rating = item["item"]["aggregateRating"]["ratingValue"]

        movies.append([movie, rating])

    df = pd.DataFrame(movies, columns=["Movie", "Rating"])

    print(df.head(20))

    df.to_csv("imdb_top250.csv", index=False)

    print(f"\nSaved {len(df)} movies to imdb_top250.csv")

else:
    print("JSON data not found")