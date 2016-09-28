#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize

br = mechanize.Browser()
br.addheaders = [('User-agent', 'Firefox')]
br.set_handle_robots(False)   # ignore robots
response = br.open("https://weather.com/de-DE")

for form in br.forms():
    print "Form name:", form.name
    print form

