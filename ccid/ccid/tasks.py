#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup as BS
from crawler.models import Crop, Quarter, Deductible, Meridian


def get_dropdown_options(soup, menu_name):
    """ Function for fetching all options from dropdown menu.
    """
    results = []
    select = soup.find('select', attrs={'name': menu_name}).decode()
    regex = re.compile('value=["\']([\d\w\s½]+)["\']\s*>(\w+)')

    # There is a bug on website (no closing <option> tags),
    # so we need to split options by tag itself.
    opts = select.split('<option ')

    # Get all value-option pairs (tuples)
    for opt_string in opts:
        m = re.search(regex, opt_string)
        if m:
            results.append((m.group(1), m.group(2)))

    return results


def get_dropdowns():

    r = requests.get('http://www.ehail.ca/quotes/')
    soup = BS(r.content, 'html.parser')

    # Get dropdown options
    dropdowns = {
        'crop': get_dropdown_options(soup, 'crop'),
        'quarter': get_dropdown_options(soup, 'quarter'),
        'deductible': get_dropdown_options(soup, 'deductible'),
        'meridian': get_dropdown_options(soup, 'meridian'),
    }