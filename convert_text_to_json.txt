# convert_text_to_json.py
# Creative Commons CC BY 4.0 License
# Author: OpenAI Assistant
# This script converts text content and image URLs into a JSON format.

import json

def convert_to_json(text_content, image_links):
    data = {
        "text": text_content.strip().split('\n'),
        "images": image_links
    }
    return json.dumps(data, indent=4)

if __name__ == '__main__':
    # Example data for demonstration
    text_content = """Example paragraph one.
Example paragraph two."""

    image_links = [
        "https://example.com/image1.jpg",
        "https://example.com/image2.png"
    ]

    json_output = convert_to_json(text_content, image_links)

    with open("output.json", "w", encoding="utf-8") as f:
        f.write(json_output)

    print("JSON data written to output.json")
