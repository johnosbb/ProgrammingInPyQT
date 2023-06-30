import spacy
from spacy.matcher import Matcher


def show_sentence_structure(doc):

    for token in doc:
        print(
            f"Token: {token.text} POS: {token.pos_} - [{spacy.explain(token.pos_)}]  Dependencies: {token.dep_} - [{spacy.explain(token.dep_)}] Fine Grained Tag: {token.tag_} - [{spacy.explain(token.tag_)}]")
    for chunk in doc.noun_chunks:
        print(f" Chunk: {chunk.text.lower()}")


    
    
def is_complex_form(doc):
    num_subjects = 0
    is_complex = False

    for token in doc:
        if token.dep_ == "mark": # a token with the dependency label "mark," typically represents subordinating conjunctions or other markers of dependent clauses. 
            is_complex = True
            break
    return is_complex 

sentences = [
    "The movie, which was directed by Steven Spielberg, won several awards.",
    "Let them wash our clothes",
    "Let's wash our clothes",
    "So, clean your room!",
    "John, clean your room",
    "Then clean your room",
    "Please let me know if you have any questions.",
    "Let’s not forget to book a hotel room.",
    "Be quiet",
    "Don't run",
    "Do not do that"
]



for sentence in sentences:
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(sentence)
    print(
        f"Target Sentence: {sentence}\n")
    show_sentence_structure(doc)
    if(is_complex_form(doc)):
        print("This is the complex\n")
    else:
        print("Could not identify the sentence type\n")
        
        