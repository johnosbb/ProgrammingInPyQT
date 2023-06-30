import spacy
from spacy.matcher import Matcher


def show_sentence_structure(doc):

    for token in doc:
        print(
            f"Token: {token.text} POS: {token.pos_} - [{spacy.explain(token.pos_)}]  Dependencies: {token.dep_} - [{spacy.explain(token.dep_)}] Fine Grained Tag: {token.tag_} - [{spacy.explain(token.tag_)}]")
    for chunk in doc.noun_chunks:
        print(f" Chunk: {chunk.text.lower()}")

def is_imperative_mood(doc):
    matcher = Matcher(nlp.vocab)
    pattern = [
        {"LOWER": "let"}, {"POS": "PRON", "LOWER": {"IN": ["us", "'s"]}}
    ]
    matcher.add("IMPERATIVE_MOOD", [pattern], greedy='LONGEST')
    matches = matcher(doc)
    matches.sort(key=lambda x: x[1])
    # print(len(matches))
    # for match in matches[:10]:
    #     print(f"match found = {doc[match[1]:match[2]]}")
    if(len(matches) > 0):
        return True
    else:
        return False
    
    
def is_imperative_form(doc):
    num_subjects = 0
    is_imperative = False
    imperative_mood = is_imperative_mood(doc)
    for token in doc:
        if token.dep_ == 'nsubj' and not imperative_mood:
            num_subjects += 1
        if (token.pos_ == "VERB" or token.pos_ == "AUX") and token.dep_ == "ROOT" and token.tag_ in ["VB", "VBP"]:
            is_imperative = True
    return is_imperative and (num_subjects == 0)

sentences = [
    "Let us wash our clothes",
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
    if(is_imperative_form(doc)):
        print("This is the imperative\n")
    else:
        print("Could not identify the sentence type\n")
        
        