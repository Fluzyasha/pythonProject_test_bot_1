# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from handlers import register_handlers
from init_bot import bot

if __name__ == '__main__':
    register_handlers()
    print('Бот запущен')
    bot.infinity_polling()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
