#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.

import logging
from telegrambotservice import *
from realangebote import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def start(bot, update):
	setMessage("Ich suche nach Angeboten! :)")
	sendMessage(bot, update)

def search(bot, update, produktname):
	angebote = getRealAngebote()
	for key in angebote.keys():




def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))



def main():

	logging.basicConfig(level=logging.DEBUG, format='%(asctime)s' +
                    '- %(name)s - %(levelname)s - %(message)s')
	logger = logging.getLogger(__name__)

	# Create the Updater and pass it your bot's token.
	updater = Updater("291218007:AAEKDywDY5B2liyHQzsS480QlqYEbOpPRgE")

	updater.dispatcher.add_handler(CommandHandler('start', start))
	updater.dispatcher.add_handler(CallbackQueryHandler(button))
	updater.dispatcher.add_handler(CommandHandler('help', help))
	updater.dispatcher.add_error_handler(error)

	# Start the Bot
	updater.start_polling()

	# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT
	updater.idle()

# start Main Methode.
if __name__ == '__main__':
    main()
