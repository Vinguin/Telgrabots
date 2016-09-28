#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chatbot import Chatbot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s' +
                    '- %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

# Bot Token
TOKEN = '232840352:AAGbQS0S5-yod8HMUAuigwOiJpo9Mp4wjnE'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

chatbothandler = {}


def start(bot, update):
    bot.sendMessage(update.message.chat_id, "Pingu online.")


def chat(bot, update):
    if(str(update.message.chat_id) in chatbothandler.keys() and
            chatbothandler[str(update.message.chat_id)].isOn()):
        reply = chatbothandler[
            str(update.message.chat_id)].talk(update.message.text)
        bot.sendMessage(update.message.chat_id, reply)


def userhelp(bot, update):
    bot.sendMessage(update.message.chat_id, "Rufe mich mit 'Hey Wilson'. " +
                    "Dann antworte ich auch auf deine Nachrichten. " +
                    "Mit 'Bye Wilson' bin ich wieder afk :D")


def msgParser(bot, update):
    dictionary_switch = {
        update.message.text.lower(): chat,
        "wetter": getWeather
    }[update.message.text.lower()](bot, update)


def getWeather(bot, update):
    if(str(update.message.chat_id) in chatbothandler.keys() and
            chatbothandler[str(update.message.chat_id)].isOn()):
        reply = chatbothandler[
            str(update.message.chat_id)].talk(update.message.text)
        bot.sendMessage(update.message.chat_id, reply)




# Create Handlers.
help_handler = CommandHandler("help", userhelp)
start_handler = CommandHandler("start", start)
reset_handler = CommandHandler("resetWilson", resetWilson)
msg_handler = MessageHandler([Filters.text], msgParser)


# "Add Listeners"
dispatcher.add_handler(help_handler)
dispatcher.add_handler(reset_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(msg_handler)


# Start polling
updater.start_polling()
