import telebot

bot = telebot.TeleBot(open('D:\key.txt', 'r')) # You can set parse_mode by default. HTML or MARKDOWN

a = ['it sunny', 'its foggy', 'its rainy'] 
n = 0


 
 

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, a [1])
    bot.send_message(message, "Its my test bot")
    
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
    
#@bot.message_handler(commands=['button'])   
#def button_message(message):
#    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#   item1=types.KeyboardButton("Кнопка")
#    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)



bot.infinity_polling()