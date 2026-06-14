#import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find titles and prices
titles = soup.find_all("h3")
prices = soup.find_all("p", class_="price_color")

# Store data
data = []

for i in range(len(titles)):

    title = titles[i].text
    price = prices[i].text

    data.append([title, price])

# Create dataframe
df = pd.DataFrame(data, columns=["Book Title", "Price"])

# Save CSV
df.to_csv("books.csv", index=False)

print(df)
print("Data Saved Successfully")