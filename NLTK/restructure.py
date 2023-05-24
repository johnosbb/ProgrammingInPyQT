import spacy

nlp = spacy.load("en_core_web_sm")

# Example sentence
doc = nlp(
    "I will go to the store after I finish my homework, but I might not have time.")

# List of subordinating conjunctions
subordinating_conjunctions = {"after", "although", "as", "because", "before", "even if", "even though", "if", "in order that", "once", "provided that",
                              "rather than", "since", "so that", "than", "that", "though", "unless", "until", "when", "whenever", "where", "whereas", "wherever", "whether", "while", "why"}

# Detect subordinating and coordinating conjunctions
for token in doc:
    if token.dep_ == "mark":
        if token.text.lower() in subordinating_conjunctions:
            print("Subordinating conjunction found:", token.text)
    elif token.dep_ == "cc":
        print("Coordinating conjunction found:", token.text)
