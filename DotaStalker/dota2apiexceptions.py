#!/usr/bin/python


class PlayerNotExistsInMatchError(Exception):
    def __init__(self, player_id, match_id):
        Exception.__init__(self, "Match " + match_id +
                           " does not contain a player " + player_id)
