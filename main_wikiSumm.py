#!/usr/bin/env python
# -*- coding: utf-8 -*-

from articleData_summ import my_articles
from wikiapi import WikiApi
wiki = WikiApi({'locale': 'en'})


def getURL(searchQuery):
    results = wiki.find(searchQuery)

    try:
        article = wiki.get_article(results[0])
    except:
        article = "no article exists for: " + searchQuery

    try:
        summary = article.summary
    except:
        summary = "no summary exists for: " + searchQuery

    if summary:
        summary_split = []
        summary_split = summary.split(". ")

    print summary_split[-1]


for article in my_articles:
    getURL(article)
