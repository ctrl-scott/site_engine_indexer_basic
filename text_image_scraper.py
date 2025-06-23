# text_image_scraper.py
# Creative Commons CC BY 4.0 License
# Author: OpenAI Assistant
# This script scrapes visible text and image URLs from a webpage.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_text_and_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Remove all script and style elements
    for script_or_style in soup(['script', 'style']):
        script_or_style.decompose()

    # Extract all visible text
    text = soup.get_text(separator='\n', strip=True)

    # Extract image URLs
    img_urls = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            full_url = urljoin(url, src)
            img_urls.append(full_url)

    return text, img_urls

if __name__ == '__main__':
    target_url = input("Enter website URL: ")
    text_content, image_links = scrape_text_and_images(target_url)

    print("\n--- TEXT CONTENT ---\n")
    print(text_content)

    print("\n--- IMAGE URLS ---\n")
    for link in image_links:
        print(link)
