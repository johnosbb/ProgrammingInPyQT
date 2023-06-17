import spacy


# An adverbial clause modifier is used to represent the relationship between a verb and an adverbial clause
# that modifies or provides additional information about the action expressed by the verb.

def show_sentence_structure(doc):

    for token in doc:
        print(
            f"Token: {token.text} POS: {token.pos_} - [{spacy.explain(token.pos_)}]  Dependencies: {token.dep_} - [{spacy.explain(token.dep_)}] Fine Grained Tag: {token.tag_} - [{spacy.explain(token.tag_)}]")


def is_imperative_form(doc):

    num_subjects = 0
    is_imperative = False
    for token in doc:
        if token.dep_ == 'nsubj':
            num_subjects += 1
        if token.pos_ == "VERB" and token.dep_ == "ROOT" and token.tag_ in ["VB", "VBP"]:
            is_imperative = True
    return is_imperative and (num_subjects == 0)


def is_single_word_utterance(doc):

    if(len(doc) == 2 and doc[1].pos_ == "PUNCT"):
        return True
    else:
        return False


def is_simple_sentence(doc):
    result = False
    # Count the number of subjects and predicates
    num_subjects = 0
    num_predicates = 0
    if(len(doc) == 2 and doc[1].pos_ == "PUNCT"):
        print(
            f"{sentence}\n")
        show_sentence_structure(sentence)
        print("This is a single word utterance\n")

    else:
        for token in doc:
            # In spaCy, the dependency label "nsubj" stands for "nominal subject." It is used to represent the grammatical relationship between a verb and its subject. The "nsubj" dependency label is assigned to the noun phrase or pronoun that acts as the subject of a verb.
            if token.dep_ == 'nsubj':
                num_subjects += 1
            elif token.dep_ == 'ROOT' and token.pos_ == 'VERB':
                # The predicate is the part of the sentence that contains the verb and any objects or modifiers associated with the verb. It provides information about the subject and what it is doing or what is happening to it.
                num_predicates += 1
        result = num_subjects == 1 and num_predicates == 1

        # Return True if there is exactly one subject and one predicate
    return result


sentences = [
    "Let us wash our clothes",
    "Let's wash our clothes",
]
# sentences = ["The cat is sleeping.", "John and Sarah went to the park.",
#              "Excellent!",
#              "Fuck you!",
#              "Screw you!",
#              "Write something!",
#              "Well screw you!",
#              "Let us wash our clothes",
#              "You wash your clothes",
#              "Wash the dinner plates.",
#              "Jack and Jill walked up the hill but jack tumbled back down.",
#              "Jack and Jill walked up the hill but tumbled back down.",
#              "Jack likes walking and fishing but hates running and hunting",
#              "Wolves and European brown bears developed a fear of humans too late and became extinct in the British wilds and the forests and mountains of Europe in medieval times.",
#              "When she finished her work, mary went home.",
#              "When you write a comic strip, the person on the left always speaks first.", "Jack likes fishing but hates hunting."]
# The "conj" dependency label applied to mary indicates that two or more words are part of a coordinated structure and are connected by a coordinating conjunction.


for sentence in sentences:
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(sentence)
    print(
        f"Target Sentence: {sentence}\n")
    show_sentence_structure(doc)
    if(is_simple_sentence(doc)):
        print("This is a simple sentence\n")
    elif(is_imperative_form(doc)):
        print("This is the imperative\n")
    elif(is_single_word_utterance(doc)):
        print("This is a single word utterance\n")
    else:
        print(
            f"This is an unclassified sentence\n")
    print("-----------------\n")
