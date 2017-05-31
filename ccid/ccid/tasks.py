#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import requests
from business.models import Business
from crawler.models import CrawlerResult
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

    # Fetch security token and set crucial headers.
    s.get('http://www.ehail.ca/quotes')
    s.headers.update({'Referer': 'http://www.ehail.ca/quotes/'})
    s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'})
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

    # Get options with companies and rates.
    payload = {}
    soup = BS(r.content, 'html.parser')
    options = soup.find_all('option')
    results = {}
    c = 1
    for opt in options[1:]:
        optText = opt.getText()
        if 'NA' not in optText:
            option_payload = {
                'item{}'.format(c,): c,
                'acres{}'.format(c,): crawler_request.acres,
                'crop{}'.format(c,): crawler_request.crop,
                'quarter{}'.format(c,): crawler_request.quarter,
                'section{}'.format(c,): crawler_request.section,
                'township{}'.format(c,): crawler_request.township,
                'range{}'.format(c,): crawler_request._range,
                'meridian{}'.format(c,): crawler_request.meridian,
                'deductible{}'.format(c,): crawler_request.deductible,
                'company{}'.format(c,): opt.get('value'),
                'coverageperacre{}'.format(c,): crawler_request.coverage
            }
            payload.update(option_payload)
            results[c] = {'company': Business.objects.get(\
                                        name__icontains=optText.split(' ')[0])}
            c+=1

    # Fetch results.
    r = s.post('http://www.ehail.ca/quotes/legalinfo.php', data=payload)

    soup = BS(r.content, 'html.parser')
    summary_table = soup.find('table', {'id': 'purchase_summary'})
    trs = summary_table.find_all('tr')

    # Omit header row.
    for tr in trs[1:]:
        try:
            tds = tr.find_all('td')
            row_id = int(tds[0].getText().split("#")[1])
            liability = tds[11].getText().split('$')[1].split("<")[0]
            premium = tds[12].getText().split('$')[1].split(" ")[0]
            results[row_id]['liability'] = liability
            results[row_id]['premium'] = premium

        # !! Exception for "TOTAL" (footer) row.
        except IndexError:
            pass

    for k,v in results.items():
        CrawlerResult.objects.create(request=crawler_request,
                                     business=v['company'],
                                     liability=v['liability'],
                                     premium=v['premium'])
