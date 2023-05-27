import spacy
import json
from ml_datasets import imdb

train_data, valid_data = imdb()

text = train_data[2000]

nlp = spacy.load("output/model-best")

doc = nlp(text[0])

print(doc.cats)

print(text)


nlp = spacy.load("output/model-best")

doc = nlp(text[0])

print(doc.cats)

print(text)


text = "I love this move, it was hard to watch, but always provoking"

nlp = spacy.load("output/model-best")

doc = nlp(text[0])

print(doc.cats)

print(text)
