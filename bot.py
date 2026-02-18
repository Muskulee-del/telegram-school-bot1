import requests
from bs4 import BeautifulSoup
import time
from telegram import Bot
import os

TOKEN = os.environ.get(8560340743:AAGcb28cZOKcEj6n-ExGr5qnnC0Ks0YGC-c)
CHAT_ID = "5685919139"
URL = "https://mustjoe.edupage.org/substitution/"

bot = Bot(token=TOKEN)

last_text = ""

while True:
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text()

        if text != last_text:
            bot.send_message(
                chat_id=CHAT_ID,
                text="📚 Возможно появились новые замены! Проверь сайт."
            )
            last_text = text

    except Exception as e:
        print("Ошибка:", e)

    time.sleep(600)
