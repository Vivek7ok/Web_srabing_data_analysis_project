import requests
from bs4 import BeautifulSoup
import pandas as pd

base = "https://books.toscrape.com/"

response = requests.get(base)
soup = BeautifulSoup(response.text, "html.parser")

# Step 1: Get all category links
categories = soup.find("ul", class_="nav nav-list").find_all("a")

category_links = []

for cat in categories:
    link = cat.get("href")
    name = cat.text.strip()

    if link != "catalogue/category/books_1/index.html":
        full_link = base + link
        category_links.append((name, full_link))

data = []

# Step 2: Loop through each category
for category_name, base_url in category_links:

    print(f"\nScraping Category: {category_name}")

    url = base_url

    while url:
        print("  Page:", url)

        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all('article', class_='product_pod')

        for book in books:
            name = book.find('h3').find('a')['title']
            price = book.find('p', class_='price_color').text

            rating_tag = book.find('p', class_='star_rating')
            rating = rating_tag['class'][1] if rating_tag else "No rating"

            availability = book.find("p", class_="instock availability").text.strip()

            data.append([category_name, name, price, rating, availability])

        # pagination
        next_btn = soup.find('li', class_='next')

        if next_btn:
            next_page = next_btn.find('a')['href']
            url = base_url.replace("index.html", "") + next_page
        else:
            url = None

# Step 3: Save data
df = pd.DataFrame(data, columns=['Category', 'Name', 'Price', 'Rating', 'Availability'])

print(df)
df.to_csv(r"D:\Data_set\Data_set_21\books.csv", index=False)