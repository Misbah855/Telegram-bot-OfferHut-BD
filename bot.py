import telebot
from telebot import types

# 🔐 Token boshabe
TOKEN = '8135634634:AAHRBpCKdBv4KQiQblADmSjY0KJaQzQMUnE'
bot = telebot.TeleBot(TOKEN)

# 🔹 Offer links (Replace with your real affiliate links)
offers = {
    "Daraz": "https://c.lazada.com.bd/t/c.DARAZ_AFFILIATE_LINK",
    "Ajkerdeal": "https://ajkerdeal.com/affiliate/YOUR_AFFILIATE_LINK",
    "Pickaboo": "https://pickaboo.com/affiliate/YOUR_AFFILIATE_LINK",
    "Othoba": "https://othoba.com/affiliate/YOUR_AFFILIATE_LINK"
}

# 🔸 /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 স্বাগতম OfferHut BD তে!\n\n🔗 সর্বশেষ অফার দেখতে `/offer` লিখুন।")

# 🔸 /offer command
@bot.message_handler(commands=['offer'])
def send_offer_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for site in offers.keys():
        markup.add(types.KeyboardButton(site))
    bot.send_message(message.chat.id, "🛍️ কোন সাইটের অফার দেখতে চান?", reply_markup=markup)

# 🔸 Text handler (Button press)
@bot.message_handler(func=lambda message: True)
def send_offer_links(message):
    site = message.text.strip()
    if site in offers:
        bot.send_message(message.chat.id, f"🔥 {site} এর আজকের অফার:\n{offers[site]}")
    else:
        bot.send_message(message.chat.id, "❗দুঃখিত, এই সাইটটি আমাদের লিস্টে নেই। `/offer` দিয়ে আবার চেষ্টা করুন।")

# ▶️ Start the bot
bot.polling()