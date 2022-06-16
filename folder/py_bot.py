import telebot

bot = telebot.TeleBot("№№№") # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    bot.send_message(message, "Its my test bot")
    
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
    
@bot.message_handler(commands=['button'])   
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)



bot.infinity_polling()