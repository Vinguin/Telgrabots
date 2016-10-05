 #!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.

import logging

from telegrambotservice import *
from jobs import *
from usermanagement import *
from realangebote import *
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,  MessageHandler, Filters, Job


def start(bot, update):
	setMessageString("Ich suche nach Angeboten! :)")
	sendMessage(bot, update)

	setMessageString(str(getUsers()))
	sendMessage(bot, update)
	

def search_products(name_list):
	angebote_all = getRealAngebote()
	angebote_found = []
	outputmsg = []
	clearMessages()
	for name in name_list:
		for angebot in angebote_all:			
			if name in angebot["name"] and not angebot in angebote_found:
				angebote_found.append(angebot)

	for produkt in angebote_found:
		message = "Angebot:\n\n"
		message += "Name:   %s\n" % produkt["name"]
		message += "Preis:     %s\n" % produkt["preis"]
		message += "Datum:  %s\n\n" % produkt["datum"]

		message += "%s" % produkt["link"]

		outputmsg.append(message)


	# Gebe Nachrichten zurück.
	return outputmsg


def subscribe_products(bot, update, name_list):
	for name in name_list:
		subscribe(update.message.chat_id, name)

	# Sende Nachricht
	setMessageString(str(getSubscribeList(update.message.chat_id)))
	sendMessage(bot, update)

def unsubscribe_products(bot, update, name_list):
	for name in name_list:
		unsubscribe(update.message.chat_id, name)

	# Sende Nachricht
	setMessageString(str(getSubscribeList(update.message.chat_id)))
	sendMessage(bot, update)


def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))

def message_interpreter(bot, update):
	msg_splitted = update.message.text.lower().split(" ")	
	cmd = msg_splitted[0]
	registerUser(update.message.from_user, bot, update)

	if cmd == "search":
		search_list = []
		for to_search in msg_splitted[1:]:
			search_list.append(to_search.encode("utf-8"))
		msglist = search_products(search_list)
		
		if msg_splitted:
			setMessageList(msglist)
			sendMessage(bot, update)
		else:
			setMessageString("Gegenwärtig keine Angebote.")
			sendMessage(bot, update)


	if cmd == "subscribe":
		subscribe_list = []
		for to_subscribe in msg_splitted[1:]:
			subscribe_list.append(to_subscribe.encode("utf-8"))
		subscribe_products(bot, update, subscribe_list)


	if cmd == "unsubscribe":
		unsubscribe_list = []
		for to_unsubscribe in msg_splitted[1:]:
			unsubscribe_list.append(to_unsubscribe.encode("utf-8"))
		unsubscribe_products(bot, update, unsubscribe_list)


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

	jobqueue = updater.job_queue

	# User datebase:	
	loadusers()

	# Job: stündlich
	job_hour = Job(callback_hour, 5)
	jobqueue.put(job_hour, next_t=0.0)

	# Start the Bot
	updater.start_polling()

	# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT
	updater.idle()

# start Main Methode.
if __name__ == '__main__':
    main()
