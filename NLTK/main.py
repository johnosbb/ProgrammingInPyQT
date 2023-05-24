import spacy
from spacy import displacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define a sentence to parse
sentence = "She sells seashells by the seashore."

# Parse the sentence using spaCy
doc = nlp(sentence)

# Extract the syntactic structure of the sentence
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)


# Save the parse tree to an SVG file
svg = displacy.render(doc, style="dep", jupyter=False)
with open("parse_tree.svg", "w", encoding="utf-8") as f:
    f.write(svg)
