#!/usr/bin/python*
# -*- coding: utf-8 -*-

import json

class UserManagement:
	def __init__(self):
		self.users= {}
		self.loadusers()

	def loadusers(self):
		try:
			file = open("user.json", "r")
			data = json.load(file)
			file.close()
			self.users = data
		except IOError:
			file = open("user.json", "w")
			json.dump({}, file, sort_keys=True, indent=4)
			file.close()
			self.users = {}
	def saveusers(self):
		with open("user.json", "w") as file:
			json.dump(self.users, file, sort_keys=True, indent=4)
			file.close()


	def registerUser(self, bot, update):
		user = update.message.from_user
		if not user["id"] in self.users.keys():
			user_dict = {}
			user_dict["first_name"] = user["first_name"]
			user_dict["last_name"] = user["last_name"]
			user_dict["username"] = user["username"]
			user_dict["id"] = user["id"]

			self.users[user["id"]] = user_dict

		self.saveusers()
