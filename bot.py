import telebot
import config
import scanner
import os

# объект бота
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello!")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'nope')


@bot.message_handler(content_types=['photo'])
def get_image(message):
    fileID = message.photo[-1].file_id
    file = bot.get_file(fileID)
    # получаем отправленный файл
    downloaded_file = bot.download_file(file.file_path)
    # временно сохраняем в директорию
    with open("tmp/" + file.file_path, "wb") as new_file:
        new_file.write(downloaded_file)
    barcode = scanner.detect(file.file_path, message.chat.id)
    bot.send_message(message.chat.id, barcode)
    # удаляем файл из директории
    os.remove("tmp/" + file.file_path)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
