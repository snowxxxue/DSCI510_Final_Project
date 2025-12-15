import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
HOME_URL = "https://books.toscrape.com/catalogue/"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
}

def get_soup(url):
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("Failed to load:", url)
        return None
    return BeautifulSoup(r.text, "html.parser")

def main():
    all_books = []

    # Scrape first 5 pages (100 books)
    for page in range(1, 6):
        url = BASE_URL.format(page)
        print(f"\nFetching page {page}: {url}")

        soup = get_soup(url)
        if soup is None:
            break

        books = soup.select(".product_pod")
        print("Books found:", len(books))

        for b in books:
            # Title
            title = b.h3.a["title"]

            # Price
            price = b.select_one(".price_color").text.replace("£", "")

            # Star rating
            rating = b.select_one(".star-rating")["class"][1]

            # Details link
            link = HOME_URL + b.h3.a["href"].replace("../", "")

            all_books.append([title, price, rating, link])

        time.sleep(0.5)

    # Save dataset into data/raw folder
    output_path = "data/raw/books_5pages.csv"
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "price", "rating", "url"])
        writer.writerows(all_books)

    print("\nScraping Completed!")
    print("Saved to:", output_path)
    print("Total books collected:", len(all_books))

if __name__ == "__main__":
    main()





