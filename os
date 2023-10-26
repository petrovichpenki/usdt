import requests
from bs4 import BeautifulSoup

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text("سلام! ربات قیمت لحظه ای تتر در نوبیتکس را فعال کردم. هر یک دقیقه یکبار قیمت را برای شما ارسال می کنم.")

def price(update, context):
    url = "https://nobitex.ir/usdt/"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    price = soup.find("span", {"class": "fw-bold ml-8-multi text-white fs-15"}).text

    update.message.reply_text(f"قیمت لحظه ای تتر در نوبیتکس: {price}")

updater = Updater(token="6888363293:AAEXMlNgG3AV4syHLIitv1nk3UFi4XYqX1o")

updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, price))

updater.start_polling()
updater.idle()
