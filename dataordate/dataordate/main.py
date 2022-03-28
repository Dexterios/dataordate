from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import telebot
from telebot import types

import config
from utils import ID

bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('E:\projects\dataordate\dataordate\dataordate\samoyed_dog.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(" ID")
    item2 = types.KeyboardButton(" add date")
    item3 = types.KeyboardButton(" show date")
    
    first_question = "You can look up ID, add info about some person and show persons list!"
    
    bot.send_message(message.chat.id,first_question,
        parse_mode='html', reply_markup=markup)
    markup.add(item1, item2, item3)
    if item1:
        markup_id = types.ReplyKeyboardMarkup(resize_keyboard=True)
        id_item_add_name = types.KeyboardButton("<b>Name</b>")
        name = id_item_add_name
        descritption = [""]
        foto = Path.cwd()
        BIRTHDAY = datetime.date.today #исправить датутаймы
        chooses = ID(name, descritption, foto, BIRTHDAY)
        bot.reply_to(message, "Fill contact information:", reply_markup = markup_id) #API from contacts
        markup_id.add(id_item_add_name)
bot.polling(none_stop = True)
