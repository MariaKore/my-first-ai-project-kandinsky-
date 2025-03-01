import telebot
from config import TOKEN
from logic import Text2ImageAPI
from config import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def command_text_hi(message):
    prompt = message.text

    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API_KEY, SECRET_KEY)
    model_id = api.get_model()
    uuid = api.generate(prompt, model_id)
    images = api.check_generation(uuid)[0]

    file_path = 'decoded_image.jpg'
    api.save_image(images, 'decoded_image.jpg')


    with open(file_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

# Запускаем бота
bot.polling()
