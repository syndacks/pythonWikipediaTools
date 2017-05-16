#!/usr/bin/env python
# -*- coding: utf-8 -*-

from articleData_summ import my_articles
from wikiapi import WikiApi
wiki = WikiApi({'locale': 'en'})

# take lines from rawData and convert to list
file_list = []
f = open('./rawData.txt', 'r')
for line in f.xreadlines():
    file_list.append([line])
f.close()

# main function that takes an article and returns the summary
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
        # summary_split = []
        # summary_split = summary.split(". ")
        print summary

    # print summary_split[-1]


for article in file_list:
    getURL(article)
