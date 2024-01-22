import telebot

from init_bot import bot


@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Привет! Это бот для выбора фильма на вечер! В каком жанре фильм хотите посмотреть?\n\n'
                                      '/com - комедия\n\n/mult - мультфильм\n\n/tril - триллер\n\n/dram - драма')

@bot.message_handler(commands=['com'])
def com(message: telebot.types.Message):
    with open('com_file.txt', 'r', encoding='utf-8') as file:
        info = file.read()
    bot.send_message(message.chat.id, info)


@bot.message_handler(commands=['mult'])
def mult(message: telebot.types.Message):
    with open('mult_file.txt', 'r', encoding='utf-8') as file:
        info = file.read()
    bot.send_message(message.chat.id, info)


@bot.message_handler(commands=['tril'])
def mult(message: telebot.types.Message):
    with open('tril_file.txt', 'r', encoding='utf-8') as file:
        info = file.read()
    bot.send_message(message.chat.id, info)


@bot.message_handler(commands=['dram'])
def mult(message: telebot.types.Message):
    with open('dram_file.txt', 'r', encoding='utf-8') as file:
        info = file.read()
    bot.send_message(message.chat.id, info)


@bot.message_handler(func=lambda _: True)
def unknown_command(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Неизвестная команда')




