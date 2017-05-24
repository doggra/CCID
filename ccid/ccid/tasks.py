#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as BS
from .models import Crop


def get_dropdowns():

    r = requests.get('http://www.ehail.ca/quotes/')
    soup = BS(r.content, 'html.parser')

    # Get all dropdown menus
    dropdowns = soup.find_all('select')

    for menu in dropdowns:
        if menu.get('name') == 'crop':
            pass