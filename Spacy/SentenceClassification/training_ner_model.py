import pandas as pd
import json
import os
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin
import utilities

# https://spacy.io/usage/training#config

DATA_PATH = "./data/Syslog/annotations.json"
TEXT_PATH = "./data/Syslog/test.txt"


def load_data(data_path):
    with open(data_path, 'r') as f:
        data = json.load(f)

    train_data = data['annotations']
    train_data = [tuple(i) for i in train_data]
    return train_data


def convert_ner_data_to_spacy_format(data_path, target_directory, use_blank_model=True):
    if(use_blank_model):
        nlp = spacy.blank("en")  # load a new blank spacy model
    else:
        nlp = spacy.load("en_core_web_sm")  # load default web model
    db = DocBin()  # create a DocBin object
    with open(data_path, 'r') as f:
        data = json.load(f)
    train_data = data['annotations']
    train_data = [tuple(i) for i in train_data]
    for text, annot in tqdm(training_data):  # data in previous format
        doc = nlp.make_doc(text)  # create doc object from text
        ents = []
        for start, end, label in annot["entities"]:  # add character indexes
            span = doc.char_span(start, end, label=label,
                                 alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents  # label the text with the ents
        db.add(doc)
    db.to_disk(target_directory)  # save the docbin object


# print(train_data)

def evaluate():
    nlp1 = spacy.load("./data/Syslog/output/model-best")  # load the best model
    with open(TEXT_PATH, 'r') as file:
        text = file.read()
    doc = nlp1(text)  # input sample text
    for ent in doc.ents:
        print(f"Text: {ent.text}, Label: {ent.label_}")

# we can train the model with
# python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./train.spacy
# this should be run from the data/Syslog directory


def main():
    # training_data = load_data(DATA_PATH)
    # utilities.convert_ner_data_to_spacy_format(
    #     DATA_PATH, "./data/Syslog/train.spacy")
    evaluate()


if (__name__ == "__main__"):
    main()
