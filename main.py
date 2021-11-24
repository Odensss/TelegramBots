import telebot
import requests
from bs4 import BeautifulSoup
import parser
import os

#####SOME VARS
url = 'https://login.rz.ruhr-uni-bochum.de/cgi-bin/laklogin'

#####BOT
bot = telebot.TeleBot('1470524618:AAHmEIYVcWcJ5Xr-2gl85Cc4j4jdTLkVIQQ')
#####KEYBOARDS
keyboard1=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('Login','LED Strip')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Bot is ready!',reply_markup=keyboard1)
@bot.message_handler(context_types=['text'])


#####FUNCTIONS
def login(message):
    bot.send_message(message.chat.id, 'OK, logging you in...')
    user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
    session = requests.Session()
    r = session.get(url, headers={'User-Agent': user_agent_val})
    session.headers.update({'Referer': url})
    session.headers.update({'User-Agent': user_agent_val})
    post_request = session.post(url, {
        'code': 1,
        'loginid': os.environ["myLogin"],
        'password': os.environ["myPassword"],
        'ipaddr': '10.4.201.237',
        'action': 'Login'
        })
    bot.send_message(message.chat.id, 'Login successful!')

def led(message):
    {}




@bot.message_handler(content_types=['text'])
def kbd_txt(message):
    if message.text == 'Login':
        login(message)
    elif message.text == 'LED Strip':
        led(message)

#####POLLING
bot.polling()