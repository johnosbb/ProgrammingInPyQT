import spacy
from spacy.matcher import Matcher


# An adverbial clause modifier is used to represent the relationship between a verb and an adverbial clause
# that modifies or provides additional information about the action expressed by the verb.

def show_sentence_structure(doc):

    for token in doc:
        print(
            f"Token: {token.text} POS: {token.pos_} - [{spacy.explain(token.pos_)}]  Dependencies: {token.dep_} - [{spacy.explain(token.dep_)}] Fine Grained Tag: {token.tag_} - [{spacy.explain(token.tag_)}]")
    for chunk in doc.noun_chunks:
        print(f" Chunk: {chunk.text.lower()}")


sentences = [
    "Helping old ladies cross the street prevents accidents.",
    "It prevents accidents."
]

for sentence in sentences:
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(sentence)
    print(
        f"Target Sentence: {sentence}\n")
    show_sentence_structure(doc)
