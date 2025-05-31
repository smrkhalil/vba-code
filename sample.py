import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "http://quotes.toscrape.com"

# Send GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all quote blocks
quotes = soup.find_all('div', class_='quote')

# Prepare CSV file
with open('quotes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])  # Header

    # Extract and write each quote to CSV
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        writer.writerow([text, author])

print("Scraping complete. Data saved to quotes.csv")
