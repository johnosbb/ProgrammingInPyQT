import spacy
from spacy.matcher import Matcher


# An adverbial clause modifier is used to represent the relationship between a verb and an adverbial clause
# that modifies or provides additional information about the action expressed by the verb.

def show_sentence_structure(doc):

    for token in doc:
        print(
            f"Token: {token.text} POS: {token.pos_} - [{spacy.explain(token.pos_)}]  Dependencies: {token.dep_} - [{spacy.explain(token.dep_)}] Fine Grained Tag: {token.tag_} - [{spacy.explain(token.tag_)}]")


def is_imperative_mood(doc):
    matcher = Matcher(nlp.vocab)
    pattern = [
        {"LOWER": "let"}, {"POS": "PRON",
                           "LOWER": {"IN": ["us", "'s", "them"]}}
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


def is_optative_mood(doc):
    matcher = Matcher(nlp.vocab)

    pattern = [
        {"LOWER": {"IN": ["let", "wish"]}},
        {"LOWER": {"IN": ["there", "you"]}},
        {"LOWER": "be"},
        {"POS": {"IN": ["NOUN", "ADJ"]}, "OP": "*"},
        {"LOWER": "on", "OP": "?"},
        {"LOWER": "earth", "POS": "NOUN", "OP": "?"}
    ]
    matcher.add("OPTATIVE_MOOD", [pattern], greedy='LONGEST')
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
        # Is the verb in its base form or the verb is (Verb, Present Tense, Non-3rd Person Singular)
        if (token.pos_ == "VERB" or token.pos_ == "AUX") and token.dep_ == "ROOT" and token.tag_ in ["VB", "VBP"]:
            has_correct_verb_form = True
    return ((has_correct_verb_form and (num_subjects == 0)), {"number of subjects": num_subjects, "has_correct_verb_form": has_correct_verb_form})


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
    # if the sentence consists of two tokens and the second token is a punctuation.
    if(len(doc) == 2 and doc[1].pos_ == "PUNCT"):
        print(
            f"{sentence}\n")
        show_sentence_structure(sentence)
        print("This is a single word utterance\n")

    else:
        for token in doc:
            # In spaCy, the dependency label "nsubj" stands for "nominal subject." It is used to represent the grammatical relationship between a verb and its subject.
            # The "nsubj" dependency label is assigned to the noun phrase or pronoun that acts as the subject of a verb.
            if token.dep_ == 'nsubj':
                num_subjects += 1
            elif token.dep_ == 'ROOT' and token.pos_ == 'VERB':
                # The predicate is the part of the sentence that contains the verb and any objects or modifiers associated with the verb.
                # It provides information about the subject and what it is doing or what is happening to it.
                num_predicates += 1
        result = num_subjects == 1 and num_predicates == 1

        # Return True if there is exactly one subject and one predicate
    return result


sentences = [
    "Let there be peace on Earth."
]


# sentences = [
#     "Let them wash our clothes",
#     "Give them the keys.",
#     "Let me know if you need help.",
#     "Let there be peace on Earth."
# ]


# sentences = [
#     "Let us wash our clothes",
#     "Let them wash our clothes",
#     "Let's wash our clothes",
#     "So, clean your room!",
#     "John, clean your room",
#     "Then clean your room",
#     "Please let me know if you have any questions.",
#     "Let’s not forget to book a hotel room.",
#     "Be quiet",
#     "Don't run",
#     "Do not do that"
# ]
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
    (is_imperative, reasons) = is_imperative_form(doc)
    if(is_imperative):
        print("This is the imperative\n")
        for key, value in reasons.items():
            print(f"Reason {key} : {value}")
    if (is_simple_sentence(doc)):
        print("This is a simple sentence\n")
    if(is_single_word_utterance(doc)):
        print("This is a single word utterance\n")
    if(is_optative_mood(doc)):
        print("This is the optative\n")
    # else:
    #     print("Could not identify the sentence type\n")
    print("-----------------\n")
