import json


class BeautifulWord():
    def __init__(self, word, meaning, tags):
        self.word = word
        self.meaning = meaning
        self.tags = tags

    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__,
    #                       sort_keys=True, indent=4)
