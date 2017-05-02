from wiktionaryparser import WiktionaryParser
from pprint import pprint

base_url = "https://es.wiktionary.org/wiki/"

with open("./es_50k.txt") as f:
    counter = 0
    content = f.readlines()
    for word in content:
        counter += 1
        new_word = word.split(" ")[0]
        if counter < 100:
            print str(counter) + ". " + new_word + ": " + base_url + new_word
    f.close()

# parser = WiktionaryParser()
# word = parser.fetch('test')

# pprint(word)
