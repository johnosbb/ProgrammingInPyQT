import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("The quick brown fox jumps over the lazy dog.")

for token in doc:
    if token.dep_ == "ROOT":
        subtree_span = doc[token.i:].root.subtree
        print(subtree_span.text)
