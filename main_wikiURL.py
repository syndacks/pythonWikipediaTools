#!/usr/bin/env python
# -*- coding: utf-8 -*-
from articleData import my_articles
import requests
from wikiapi import WikiApi

wiki = WikiApi({'locale': 'es'})

def getURL(searchQuery):
    results = wiki.find(searchQuery)

    try:
        article = wiki.get_article(results[0])
    except:
        article = "no article exists for: " + searchQuery

    try:
        url = article.url
    except:
        url = "no url exists for: " + searchQuery

    # try:
    #     summary = article.summary
    # except:
    #     summary

    print url
    # print summary


# for article in my_articles:
#     getURL(article)

request = requests.get('https://es.wiktionary.org/wiki/comercion')
if request.status_code >= 400:
    print('Web site does not exist')
