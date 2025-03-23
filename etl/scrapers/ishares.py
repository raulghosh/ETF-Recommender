import requests
from bs4 import BeautifulSoup
import os

# URL of the BlackRock regulatory documents page
url = "https://www.blackrock.com/us/individual/resources/regulatory-documents"

# Send a GET request to fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Locate the ETF listings (adjust the selector based on the actual HTML structure)
etf_listings = soup.find_all("div", class_="etf-listing")  # Hypothetical class name

# Extract ETF names and document links
etfs = []
for listing in etf_listings[:10]:  # Limit to 10 ETFs
    name = listing.find("h3").text.strip()  # Hypothetical tag for ETF name
    link = listing.find("a", href=True)["href"]  # Hypothetical link to documents
    etfs.append({"name": name, "link": link})

# Print the extracted ETFs
for etf in etfs:
    print(f"ETF Name: {etf['name']}, Document Link: {etf['link']}")