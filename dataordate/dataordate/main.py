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
    sti = open('E:\projects\dataordate\dataordate\dataordate\sticers_for_messages\samoyed_dog.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Good day. This bot is created by Vlad.")
    bot.send_message(message.chat.id, "This bot can remember birthday dates. Please select ID to create new member.")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(" ID")
    item2 = types.KeyboardButton(" add date")
    item3 = types.KeyboardButton(" show all IDs")

    bot.send_message(message.chat.id,
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
        #добавить день рождения Данияра 15.09.1998
        markup_id.add(id_item_add_name)
        bot.send_message(message.chat.id, chooses,
            reply_markup=markup_id)
        
bot.polling(none_stop = True)
