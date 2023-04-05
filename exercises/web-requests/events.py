



import requests
from bs4 import BeautifulSoup # note that the import package command is `bs4`





events_url = "https://www.georgetown.edu/events/"

response = requests.get(events_url)

soup = BeautifulSoup(response.text)





clean_listings = []

listings = soup.find_all("div", "c--event-teaser-row")

for listing in listings:
    date = listing.find("div", "f--date").text.strip()
    title = listing.find("h3").text.strip()
    loc = listing.find("div", "f--event-location").text.strip()
    time = listing.find("time", "f--time-string").text.strip()
    link = listing.find("a")["href"]

    clean_listing = {
        "date": date,
        "time": time,
        "title": title,
        "location": loc,
        "url": link
    }
    clean_listings.append(clean_listing)



clean_listings


