"""
این ماژول یک ربات تلگرام است که می‌تواند مقدار لحظه‌ای Tether را به کاربران ارسال کند.
"""

import requests
from bs4 import BeautifulSoup
import telegram.ext

# توکن ربات خود را اینجا قرار دهید
TOKEN = "6888363293:AAEXMlNgG3AV4syHLIitv1nk3UFi4XYqX1o"

def get_price():
    """
    مقدار لحظه‌ای Tether را برمی‌گرداند.

    :return: مقدار Tether به صورت رشته
    """

    url = "https://nobitex.ir/usdt/"

    # یک تایم‌اوت 5 ثانیه‌ای برای درخواست اضافه کنید.
    response = requests.get(url, timeout=5)

    # پاسخ HTML را تجزیه کنید و قیمت Tether را استخراج کنید.
    soup = BeautifulSoup(response.content, "html.parser")
    price = soup.find("span", {"class": "fw-bold ml-8-multi text-white fs-15"}).text

    return price

def send_price(updater: telegram.ext.Updater, context: telegram.ext.Context):
    """
    مقدار لحظه‌ای Tether را به کاربر ارسال می‌کند.

    :param updater: شیء به‌روزرسانی تلگرام
    :param context: Context رابط بین ربات و Dispatcher
    """

    # قیمت Tether را دریافت کنید.
    price = get_price()

    # قیمت را به کاربر ارسال کنید.
    updater.bot.send_message(context.message.chat.id, f"قیمت لحظه‌ای Tether: {price}")

updater = telegram.ext.Updater(TOKEN, update_queue=None)

# Handler برای دستور start
updater.dispatcher.add_handler(telegram.ext.CommandHandler("start", send_price))

# Handler برای پیام‌های متنی
updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.Text, send_price))

# شروع ربات
updater.start_polling()

# منتظر توقف ربات باشید.
updater.idle()
