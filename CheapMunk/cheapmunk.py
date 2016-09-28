#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.

import logging
from telegrambotservice import *
from sets import Set
from realangebote import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,  MessageHandler, Filters


def start(bot, update):
	setMessage("Ich suche nach Angeboten! :)")
	sendMessage(bot, update)

def search_products(bot, update, name_list):
	angebote_all = getRealAngebote()
	angebote_found = []

	clearMessages()
	for name in name_list:
		for angebot in angebote_all:
			
			if name in angebot["name"]:
				angebote_found.append(angebot)

	for angebot in angebote_found:
		message = "Angebot:"
		message += "\nName: %s" % angebot["name"]
		message += "\nPreis: %s" % angebot["preis"]
		message += "\n\n\t%s" % angebot["link"]
		appendMessage(message)

	# Sende Nachricht
	sendMessage(bot, update)

def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))

def message_interpreter(bot, update):
	msg_splitted = update.message.text.lower().split(" ")	
	cmd = msg_splitted[0]

	if cmd == "search":
		search_list = []
		for to_search in msg_splitted[1:]:
			search_list.append(to_search)
		search_products(bot, update, search_list)


def main():

	logging.basicConfig(level=logging.DEBUG, format='%(asctime)s' +
                    '- %(name)s - %(levelname)s - %(message)s')
	logger = logging.getLogger(__name__)

	# Create the Updater and pass it your bot's token.
	updater = Updater("291218007:AAEKDywDY5B2liyHQzsS480QlqYEbOpPRgE")

	updater.dispatcher.add_handler(CommandHandler('start', start))
	updater.dispatcher.add_handler(CallbackQueryHandler(button))
	updater.dispatcher.add_handler(MessageHandler([Filters.text], message_interpreter))
	updater.dispatcher.add_error_handler(error)

	# Start the Bot
	updater.start_polling()

	# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT
	updater.idle()

# start Main Methode.
if __name__ == '__main__':
    main()
