import telebot

TOKEN = 'PASTE_YOUR_BOT_TOKEN'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 স্বাগতম OfferHut BD-তে!")

@bot.message_handler(commands=['offer'])
def send_offer(message):
    bot.send_message(message.chat.id, "🔥 আজকের অফার:\nhttps://your_affiliate_link.com")

bot.polling()