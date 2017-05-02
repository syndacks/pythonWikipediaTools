from wiktionaryparser import WiktionaryParser
from pprint import pprint

parser = WiktionaryParser()
word = parser.fetch('test')

pprint(word)
