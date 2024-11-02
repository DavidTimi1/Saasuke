import os

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from .gemini import ask_gemini
from .settings import *
from .models import Chats, Message


bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Open Mini App", mini_app))

    bot.reply_to(
        message, 
        "Howdy, how are you doing? I will now be giving Gemini responses", 
        reply_markup=markup
    )


@bot.message_handler(commands=['help'])
def help(message):
    person = message.from_user
    first_name = person.first_name
    chat_id = message.chat.id

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Open Website", landing_page))
    
    reply = f"Hi!! {first_name}, how may I help?"
    bot.send_message(chat_id, reply, reply_markup=markup)


@bot.message_handler(commands=['clear'])
def clear(message):
    person = message.from_user
    username = person.username

    delete_file(username)
    # delete messages too


@bot.message_handler(func=lambda msg: True)
def ai_reply(message):
    person = message.from_user
    username = person.username
    history = retrieve_chat_history(username)

    response = ask_gemini(message.text, history)

    save_chat_state(username, history[-2:])

    bot.reply_to(message, response)



def retrieve_chat_history(name):
    history = []
    chat, created = Chats.objects.get_or_create(username=name)

    if not created:
        for message in chat.messages.all():
            history.append(
                message.process()
            )

    return history


def save_chat_state(name, entries):
    chat = Chats.objects.get(username=name)
    file = text = None

    for entry in entries:
        for part in entry["parts"]:
            if isinstance(part, str):
                text = part
            else:
                file = part
            
        message = Message(chat=chat, role=entry["role"], textContent=text, file=file)
        message.save()
    


def delete_file(name):
    os.remove(f"chats/{name}.json")

def abs_path(x):
    return os.path.abspath(x)