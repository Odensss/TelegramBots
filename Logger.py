import telebot
import requests
from bs4 import BeautifulSoup

# SOME VARS
url = 'https://login.rz.ruhr-uni-bochum.de/cgi-bin/start'
payload = {
    'lgn': 'login',
    'pwd': 'password'
}
# TOKEN
TOKEN = 'Token'
bot = telebot.TeleBot(TOKEN)


# KEYBOARDS

# COMMANDS
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Lorem')


@bot.message_handler(commands=['login'])
def login(message):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parcer')
    with requests.Session() as s:
        p = s.post(url, data=payload)


# POLLING
bot.polling()
