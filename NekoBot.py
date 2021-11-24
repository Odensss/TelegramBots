from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters, Updater, CommandHandler
from telegram.utils.request import Request

TOKEN = "1955671353:AAHP8z8EkMNmGrWtfPNhju_x0VwwBUc3Ovs"
PROXY_URL = 'https://telegg.ru/orig/bot'
#Айди админов
ADMIN_IDS = [
    253704753,
]
# Мой айди
MAIN_ADMIN_ID = 253704753

#Доступ админа
def admin_access(f):
    def inner(*args, **kwargs):
        print(args, kwargs)
        update = args[0]
        if update and hasattr(update, 'message'):
            chat_id = update.message.chat_id
            if chat_id in ADMIN_IDS:
                print('Доступ разрешен!')
                return f(*args, **kwargs)
            else:
                print('Доступ запрещен!',chat_id)
        else:
            print('Нет аргумента update!')

    return inner


@admin_access
def secret_command(update: Update, context: CallbackContext):
    update.message.reply_text(text='It is a secret!')

#Логгер ошибок
def log_errors(f):
    def inner(*args,**kwargs):
        try:
            return f(*args,**kwargs)
        except Exception as e:
            error_message = f'[ADMIN] Произошла ошибка: {e}'
            print(error_message)
            update = args[0]
            if update and hasattr(update, 'message'):
                #Сообщение админу
                update.bot.send_message(
                    chat_id=MAIN_ADMIN_ID,
                    text=error_message,
                )

            raise e
    return inner
@log_errors


def start(update: Update, context: CallbackContext):
    update.message.reply_text(text = 'Виталя, пошел ты нахуй!')

def search_music(update: Update, context: CallbackContext):
    update.message.reply_text(text='What song are you looking for?')
    song_name = update.message.text
    update.message.reply_text(song_name)


def main():
    # 1--правилльное подключение
    request = Request(connect_timeout=0.5,  # ошибки при подключении айпи
                      read_timeout=1.0)
    bot = Bot(request=request,
              token=TOKEN,
              )
    print(bot.get_me())

    # 2--обработчики
    updater = Updater(bot=bot, use_context=True)

    start_cmd = CommandHandler('start',start)
    updater.dispatcher.add_handler(start_cmd)


    command1 = CommandHandler('secret', secret_command)
    updater.dispatcher.add_handler(command1)


    cmd_search = CommandHandler('music', search_music)
    updater.dispatcher.add_handler(cmd_search)


    # 3--Запустить бесконечную обработку входящих сообщений
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
