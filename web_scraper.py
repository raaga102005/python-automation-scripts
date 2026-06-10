import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_website(url, output_file='scraped_data.csv'):
    """
    Scrapes product/listing data from any public website.
    Extracts titles, prices, and links from the page.
    Saves results to a CSV file.

    Works on any site that lists items with prices.
    Example: books.toscrape.com (safe practice site)
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    all_items = []
    page = 1

    print(f"Starting scrape of: {url}")

    while True:
        # Build page URL
        if '?' in url:
            page_url = f"{url}&page={page}"
        else:
            page_url = f"{url}/page-{page}.html" if page > 1 else url

        # Fetch the page
        response = requests.get(page_url, headers=headers)

        if response.status_code != 200:
            print(f"Stopped at page {page} — status code {response.status_code}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all items on the page
        # This targets books.toscrape.com structure
        items = soup.find_all('article', class_='product_pod')

        if not items:
            print(f"No more items found at page {page}. Done.")
            break

        for item in items:
            title = item.find('h3').find('a')['title'] if item.find('h3') else 'N/A'
            price = item.find('p', class_='price_color').text.strip() if item.find('p', class_='price_color') else 'N/A'
            rating = item.find('p', class_='star-rating')['class'][1] if item.find('p', class_='star-rating') else 'N/A'
            availability = item.find('p', class_='availability').text.strip() if item.find('p', class_='availability') else 'N/A'

            all_items.append({
                'Title': title,
                'Price': price,
                'Rating': rating,
                'Availability': availability
            })

        print(f"Page {page}: scraped {len(items)} items")
        page += 1

        # Be polite — wait 1 second between requests
        time.sleep(1)

        # Stop after 5 pages for safety
        if page > 5:
            print("Reached 5 page limit. Stopping.")
            break

    # Save to CSV
    df = pd.DataFrame(all_items)
    df.to_csv(output_file, index=False)
    print(f"\nTotal items scraped: {len(all_items)}")
    print(f"Saved to: {output_file}")
    print("\nPreview:")
    print(df.head())
    return df


if __name__ == "__main__":
    # Practice on this safe test site
    scrape_website("https://books.toscrape.com", "books_data.csv")
