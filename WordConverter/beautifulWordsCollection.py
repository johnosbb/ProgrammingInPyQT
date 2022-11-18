import json
import jsonpickle

from beautifulWord import BeautifulWord


class BeautifulWordsCollection():
    def __init__(self):
        self.wordList = []

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def add(self, word: BeautifulWord):
        self.wordList.append(word)

    def save(self):
        # saves the words to a file
        with open("beautiful_words.json", "w") as outfile:
            jsonObj = jsonpickle.encode(self.wordList, keys=True)
            outfile.write(jsonObj)

    def load(self):
        # loads the words from a file
        # Opening JSON file
        with open('beautiful_words.json', 'r') as openfile:
            words = openfile.read()
            self.wordList = jsonpickle.decode(words, keys=True)
