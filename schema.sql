-- schema.sql
-- Creative Commons CC BY 4.0 License
-- Author: OpenAI Assistant
-- Schema for storing scraped website text and image URLs

CREATE TABLE webpages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL UNIQUE,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE page_texts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    webpage_id INTEGER,
    paragraph TEXT,
    position INTEGER,
    FOREIGN KEY (webpage_id) REFERENCES webpages(id)
);

CREATE TABLE page_images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    webpage_id INTEGER,
    image_url TEXT,
    position INTEGER,
    FOREIGN KEY (webpage_id) REFERENCES webpages(id)
);
