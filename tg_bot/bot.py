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
    user_id = message.from_user.id

    delete_chats(user_id)
    # delete messages too


@bot.message_handler(func=lambda msg: True)
def ai_reply(message):
    person = message.from_user
    print(message.text)
    history = retrieve_chat_history(person)

    response = ask_gemini(message.text, history)
    print(response)

    save_chat_state(person.id, history[-2:])
    print("Saved history")

    bot.reply_to(message, response)



def retrieve_chat_history(user):
    history = []
    chat, created = Chats.objects.get_or_create(username=user.username, user_id=user.id)

    if not created:
        for message in chat.messages.all():
            history.append(
                message.process()
            )

    return history


def save_chat_state(user_id, entries):
    chat = Chats.objects.get(user_id=user_id)
    file = text = None

    for entry in entries:
        for part in entry["parts"]:
            if isinstance(part, str):
                text = part
            else:
                file = part
            
        message = Message(chat=chat, role=entry["role"], textContent=text, file=file)
        message.save()
    


def delete_chats(user_id):
    chat = Chats.objects.get(user_id=user_id)
    chat.clear()
