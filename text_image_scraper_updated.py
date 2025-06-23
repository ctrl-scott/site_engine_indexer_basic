# text_image_scraper.py
import sys
import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_text_and_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for tag in soup(['script', 'style']):
        tag.decompose()

    text = soup.get_text(separator='\n', strip=True).split('\n')
    img_urls = [urljoin(url, img.get('src')) for img in soup.find_all('img') if img.get('src')]
    return {"text": text, "images": img_urls}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Missing URL"}))
        sys.exit(1)

    result = scrape_text_and_images(sys.argv[1])
    print(json.dumps(result))
