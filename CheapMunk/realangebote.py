#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests
from lxml import html, cssselect


# Gib eine Liste mit Produkten aus, wie angeboten werden. (Diese Woche)
def getRealAngebote():
	url = "http://prospekt.real.de/wochenangebote-nach-kategorien/alle-angebote.html"
	page = requests.get(url)
	tree = html.fromstring(page.content)
	angebote = tree.cssselect("a.product_name")
	preise = tree.cssselect("div.preismarke_small.clearfix")
	datum = tree.cssselect("span.tc_bright_grey.fs_15")[0].text

	angebote_output = []
	produkte=[]
	for angebot, preis in zip(angebote, preise):
		produkt={}
		produkt["name"] = angebot.text
		produkt["preis"] = preis.attrib["title"]
		produkt["link"] = "http://prospekt.real.de/"+ angebot.attrib["href"]
		produkt["datum"] = datum
		produkte.append(produkt)
	return produkte




