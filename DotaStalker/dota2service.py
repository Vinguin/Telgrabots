#!/usr/bin/python


from StringIO import StringIO
from lxml import html, cssselect
import requests
import json

from dota2apiexceptions import PlayerNotExistsInMatchError


class Dota2Api():
    def __init__(self, steam_api_key_init):
        self.steam_api_key = steam_api_key_init
        # Url Kompotenten
        self.url_base = 'https://api.steampowered.com/IDOTA2Match_570/'
        self.url_history = 'GetMatchHistory/V001/'
        self.url_details = 'GetMatchDetails/V001/'

    # Gibt die letzten 100 Games als Dictionary-Objekt aus.
    def retrieveMatchHistory(self, player_id):
        dictionary = "{}"
        while str(dictionary) == "{}":
            page = requests.get(self.url_base + self.url_history +
                                "?account_id=" + str(player_id) +
                                "&key=" + self.steam_api_key)
            dictionary = json.load(StringIO(page.content))
        return dictionary

    # Gibt die Match-Details zu einem Match als Dictionary-Objekt aus.
    def retrieveMatchDetails(self, match_id):
        dictionary = "{}"
        while str(dictionary) == "{}":
            page = requests.get(self.url_base + self.url_details +
                                "?match_id=" + str(match_id) + "&key=" +
                                self.steam_api_key)
            dictionary = json.load(StringIO(page.content))
        return dictionary

    # Gibt die letzten 100 Matches in einer Liste mit Match-IDS aus.
    def get100LatestMatchIds(self, player_id):
        dictionary = self.retrieveMatchHistory(player_id)
        output = []
        for match in dictionary["result"]["matches"]:
            output.append(match["match_id"])
        return output

    # Gibt die Spielernamen zu einem Match als Liste aus.
    def getPlayersOfMatch(self, match_id):
        player_tags = []
        dictionary = self.retrieveMatchDetails(match_id)["result"]["players"]
        for player in dictionary:
            player_id = player["account_id"] + 76561197960265728
            page = requests.get("http://steamcommunity.com/profiles/" +
                                str(player_id))
            tree = html.fromstring(page.content)
            elem = tree.cssselect("span.actual_persona_name")
            if len(elem) > 0:
                player_tags.append(elem[0].text)
            else:
                print "Account \"" + str(player_id) + "\" couldn't be found."
        return player_tags

    # Gibt zurueck, ob der Spieler das Match gewonnen hat.
    def hasPlayerWonMatch(self, player_id, match_id):
        dictionary = self.retrieveMatchDetails(match_id)["result"]["players"]
        player_ids = []
        for player in dictionary:
            player_ids.append(player["account_id"] + 76561197960265728)
        if player_id not in player_ids:
            raise PlayerNotExistsInMatchError(player_id, match_id)
        else:
            print "Account-ID \"" + str(player_id) + "\" couldn't be found."

# print get100LatestMatchIds(ganker)
