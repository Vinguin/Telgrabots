#!/usr/bin/python*
# -*- coding: utf-8 -*-


import logging
import json

from steamsale import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


botname= 'Piggybank'
username=   'Piggybanksteambot'
http_api= '288723325:AAErhiC_wUOvzue9DpS6jPEE6V4RJVBqJKY'


# Debug
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s' +'- %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def start(bot, update):
	bot.sendMessage(update.message.chat_id, "Hey, ich bin Piggybank :)")
	reload_db(bot, update)

def msgandler(bot, update):
	if update.message.text.lower() == "erstes spiel":
		dic = getSteamSales()
		for key in dic.keys():
			bot.sendMessage(update.message.chat_id, key)
			break

def main():
	updater = Updater(token=http_api)
	dispatcher = updater.dispatcher


	# Create Handlers.
	dispatcher.add_handler(CommandHandler("start", start))
	dispatcher.add_handler(MessageHandler([Filters.text], msgandler))

	# Lade die gespeicherten Dateien.

	# Start polling
	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()
