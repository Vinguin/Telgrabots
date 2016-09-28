#!/usr/bin/python

import requests

url_base = 'https://api.steampowered.com/IDOTA2Match_570/'
url_history = 'GetMatchHistory/V001/'
url_details = 'GetMatchDetails/V001/'
api_key = '538725FDE5979CB25FED104A6FFAEE21'

ganker_account_id = '76561198026178119'
vinh_account_id = '76561198027082546'

response = requests.get(url_base + url_history + "?account_id="
                        + ganker_account_id + "&key=" + api_key)

print(response.content)
