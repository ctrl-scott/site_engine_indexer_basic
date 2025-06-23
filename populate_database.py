# populate_database.py
# Creative Commons CC BY 4.0 License
# Author: OpenAI Assistant
# Populates the database with scraped webpage data

import sqlite3
from datetime import datetime

def initialize_db(db_path="scraped_data.db"):
    with open("schema.sql", "r") as f:
        schema = f.read()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()

def insert_scraped_data(url, text_blocks, image_urls, db_path="scraped_data.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Insert into webpages
    cursor.execute("INSERT OR IGNORE INTO webpages (url, scraped_at) VALUES (?, ?)", (url, datetime.now()))
    conn.commit()
    cursor.execute("SELECT id FROM webpages WHERE url = ?", (url,))
    webpage_id = cursor.fetchone()[0]

    # Insert text paragraphs
    for position, paragraph in enumerate(text_blocks):
        cursor.execute("INSERT INTO page_texts (webpage_id, paragraph, position) VALUES (?, ?, ?)",
                       (webpage_id, paragraph, position))

    # Insert image URLs
    for position, image_url in enumerate(image_urls):
        cursor.execute("INSERT INTO page_images (webpage_id, image_url, position) VALUES (?, ?, ?)",
                       (webpage_id, image_url, position))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()

    # Example usage
    example_url = "https://example.com"
    example_texts = ["Example paragraph one.", "Example paragraph two."]
    example_images = ["https://example.com/image1.jpg", "https://example.com/image2.png"]
    insert_scraped_data(example_url, example_texts, example_images)
    print("Database populated.")
