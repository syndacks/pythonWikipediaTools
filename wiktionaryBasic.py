from wiktionaryparser import WiktionaryParser
from pprint import pprint

f1 = open('./es_50k.txt')
f2 = open('Output.txt', 'a')

BASE_URL = "https://es.wiktionary.org/wiki/"

with f1 as f:
    counter = 0
    content = f.readlines()
    for word in content:
        counter += 1
        new_word = word.split(" ")[0]
        if counter < 1000:
            print str(counter) + ") " + new_word + ": " + BASE_URL + new_word
            f2.write(str(counter) + ") " + new_word + ": " + BASE_URL + new_word + '\n')
    f.close()
    f2.close()
