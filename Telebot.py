#IMPORTS
import telebot
#TOKEN
bot = telebot.TeleBot('TOKEN')
#KEYBOARDS
keyboard1=telebot.types.ReplyKeyboardMarkup(True,True,True)
keyboard1.row('Подробнее','Купить ФК','Контакты')
keyboard2=telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Узнать стоимость')
keyboard3=telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row('Продолжить')
keyboard4=telebot.types.ReplyKeyboardMarkup(True)
keyboard4.row('Готово')
#FUNCTIONS
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет!\nЕсли ты занимаешься физкультурой в ГЛАВНОМ КОРПУСЕ, или КОРПУСЕ РГФ (кольцовский сквер), то я к твоим услугам.\n'
    "Если ты допустишь какую-то ошибку при вводе информации о себе, то это будет полностью на твоей совести, и очень маловероятно, что я смогу как-то тебе помочь.",reply_markup=keyboard2)
#DIFFERENT MESSAGES
@bot.message_handler(content_types=['text'])
def kbrd_txt(message):
    if message.text.lower() == 'подробнее':
        bot.send_message(message.chat.id, 'Если ты занимешься на Хользунова, то обратись лично по ссылке в контактах\n',reply_markup=keyboard1)
    elif message.text.lower() == 'купить фк':
        send = bot.send_message(message.chat.id,'Введите Ваши фамилию, имя и отчество:')
        bot.register_next_step_handler(send,step1)
    elif message.text.lower() == 'контакты':
        bot.send_message(message.chat.id,'TG: @kenzoroo',reply_markup=keyboard1)
    elif message.text.lower() == 'узнать стоимость':
        bot.send_message(message.chat.id,'В этом семестре стоимость составляет 2200 рублей как для юношей, так и для девушек.\nЕсли по какой-то причине '
                                         'Вы увидите, что зачёт так и не стоит на мудле, то обратитесь по контактам лично ко мне, и я в обязательном порядке помогу Вам индивидуально!',reply_markup=keyboard3)
    elif message.text.lower() == 'продолжить':
        bot.send_message(message.chat.id,'Выберите дальнейшее действие',reply_markup=keyboard1)
    elif message.text.lower() == 'готово':
        f=open("list.txt",'r')
        data=f.readline()
        bot.send_message(839442823,'Новый клиент!Проверь Сбер!\n'+data)
        f=open("list.txt",'w')
        f.close()
        bot.send_message(message.chat.id,'Спасибо за сотрудничество!<3',reply_markup=keyboard1)
#ПОШАГОВАЯ ЗАЯВКА НА ПОКУПКУ ФК
cntr=1
def step1(message):
    f = open("list.txt",'a')
    txt = message.text
    f.write(txt+' ')
    f.close()
    send = bot.send_message(message.chat.id,'Теперь введите Ваш факультет:')
    bot.register_next_step_handler(send,step2)
def step2(message):
    f = open("list.txt", 'a')
    txt = message.text
    f.write(txt + ' ')
    f.close()
    send = bot.send_message(message.chat.id,'Направление:')
    bot.register_next_step_handler(send, step3)
def step3(message):
    f = open("list.txt", 'a')
    txt = message.text
    f.write(txt + ' ')
    f.close()
    send=bot.send_message(message.chat.id,'Курс:')
    bot.register_next_step_handler(send, step4)
def step4(message):
    f = open("list.txt", 'a')
    txt = message.text
    f.write(txt + ' ')
    f.close()
    send=bot.send_message(message.chat.id, 'Группа:')
    bot.register_next_step_handler(send, step5)
def step5(message):
    f = open("list.txt", 'a')
    txt = message.text
    f.write(txt + ' ')
    f.close()
    send=bot.send_message(message.chat.id, 'Корпус, в которым Вы занимаетесь ФК:')
    bot.register_next_step_handler(send, step6)
def step6(message):
    f = open("list.txt", 'a')
    txt = message.text
    f.write(txt + ' ')
    f.close()
    bot.send_message(message.chat.id, 'Класс!\n Теперь отправь мне 2200 рублей на карту Сбербанк по номеру 89507775433 (Ролан) и подпиши в сообщении свои ФИО.\nЗАТЕМ нажми кнопку готово, и я проверю свой счёт.\nСпасибо за сотрудничество!<3',reply_markup=keyboard4)


#POLLING
bot.polling()
