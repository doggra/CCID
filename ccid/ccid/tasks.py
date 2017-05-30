#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup as BS


def get_dropdown_options(soup, menu_name):
    """ Function for fetching all options from dropdown menu.
    """
    results = []
    select = soup.find('select', attrs={'name': menu_name}).decode()
    regex = re.compile('value=["\']([\d\w\s½]+)["\']\s*>([\w\s½]+)')

    # There is a bug on website (no closing <option> tags),
    # so we need to split options by tag itself.
    opts = select.split('<option ')

    # Get all value-option pairs (tuples)
    for opt_string in opts:
        m = re.search(regex, opt_string)
        if m:
            results.append((m.group(1), m.group(2).strip()))

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

    for model_name, options in dropdowns.items():
        for opt in options:
            # For every option check if already exists in DB,
            # if not, create object
            eval(("{}.objects.update_or_create"
                  "(name='{}', defaults={{'value': '{}'}})")\
                 .format(model_name.title(), opt[1].encode('utf-8'), opt[0].encode('utf-8')))


def make_request_to_ehailca(crawler_request):

    # Create session
    s = requests.Session()

    # Fetch security token and set referer
    s.get('http://www.ehail.ca/quotes')
    s.headers.update({'Referer': 'http://www.ehail.ca/quotes/'})
    crawler_request.token = s.cookies.get('MRSessToken')


    url = ('http://www.ehail.ca/quotes/process.php'
           '?ajax=rates'
           '&township={}'
           '&range={}'
           '&meridian={}'
           '&crop={}'
           '&deductible={}').format(crawler_request.township,
                                    crawler_request._range,
                                    crawler_request.meridian,
                                    crawler_request.crop,
                                    crawler_request.deductible)

    r = s.get(url)
