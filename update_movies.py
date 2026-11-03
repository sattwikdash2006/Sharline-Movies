import os
import requests
import json

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
JSON_FILE = "movies.json"

def fetch_movies():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(url)
    movies = []
    
    if response.status_code == 200:
        data = response.json()
        for result in data.get("result", []):
            msg = result.get("channel_post")
            if msg:
                text = msg.get("text", "Movie Update")
                movies.append({
                    "title": text[:30],
                    "year": "2026",
                    "genre": "Telegram Stream",
                    "poster": "https://via.placeholder.com/300x450",
                    "link": f"https://t.me/c/{str(CHAT_ID)[4:]}/{msg['message_id']}"
                })
    return movies

def update_json():
    movies = fetch_movies()
    if movies:
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(movies, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    update_json()
