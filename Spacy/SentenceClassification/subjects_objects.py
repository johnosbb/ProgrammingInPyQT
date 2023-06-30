import spacy

sentences = ["The boy shot at the man", "The boy shot a gun at the man", "The big black cat stared at the small dog.",
             "Jane watched her brother in the evenings.", "Laura gave Sam a very interesting book.", "I gave a gift to my friend."]

nlp = spacy.load('en_core_web_sm')


def show_sentence_parts(doc):
    print(doc)
    print("{:<12} | {:<6} | {:<8} | {:<8} | {:<24} | {:<20} | {:<10}".format(
        'Text', 'Index', 'POS', 'Dep', 'Dep Detail', 'Ancestors', 'Children'))
    print("----------------------------------------------------------------------------------------------------------------------")
    for token in doc:
        ancestors = ' '.join([t.text for t in token.ancestors])
        children = ' '.join([t.text for t in token.children])
        print("{:<12} | {:<6} | {:<8} | {:<8} | {:<24} | {:<20} | {:<10}".format(
            token.text, token.i, token.pos_, token.dep_, spacy.explain(token.dep_), ancestors, children))
        print("----------------------------------------------------------------------------------------------------------------------")


def show_sentence_structure(doc):

    print("-------------------------")
    for token in doc:
        print(
            f"Token: {token.text} POS: {token.pos_} - [{spacy.explain(token.pos_)}]  Dependencies: {token.dep_} - [{spacy.explain(token.dep_)}] Fine Grained Tag: {token.tag_} - [{spacy.explain(token.tag_)}]")
    for chunk in doc.noun_chunks:
        print(f" Chunk: {chunk.text.lower()}")
    print("-------------------------")


def get_subject_phrase(doc):
    for token in doc:
        if ("subj" in token.dep_):
            subtree = list(token.subtree)
            start = subtree[0].i
            end = subtree[-1].i + 1
            return doc[start:end]


def get_object_phrase(doc):
    for token in doc:
        if ("dobj" in token.dep_):
            subtree = list(token.subtree)
            start = subtree[0].i
            end = subtree[-1].i + 1
            return doc[start:end]


def get_dative_phrase(doc):
    for token in doc:
        if ("dative" in token.dep_):
            # a token's subtree refers to the collection of tokens that are directly or indirectly dependent on that token.
            subtree = list(token.subtree)
            # Each token in spaCy has an i attribute that represents its index within the parent Doc object.
            start = subtree[0].i
            end = subtree[-1].i + 1
            return doc[start:end]


def get_prepositional_phrase_objs(doc):
    prep_spans = []
    for token in doc:
        if ("pobj" in token.dep_):
            # a token's subtree refers to the collection of tokens that are directly or indirectly dependent on that token.
            subtree = list(token.subtree)
            start = subtree[0].i
            end = subtree[-1].i + 1
            prep_spans.append(doc[start:end])
    return prep_spans


def main():
    for sentence in sentences:
        doc = nlp(sentence)
        # show_sentence_structure(doc)
        show_sentence_parts(doc)
        subject_phrase = get_subject_phrase(doc)
        object_phrase = get_object_phrase(doc)
        dative_phrase = get_dative_phrase(doc)
        prepositional_phrase_objs = get_prepositional_phrase_objs(doc)
        print(f"subject_phrase: {subject_phrase}")
        print(f"object_phrase: {object_phrase}")
        print(f"dative_phrase: {dative_phrase}")
        print(f"prepositional_phrase_objs: {prepositional_phrase_objs}")


if (__name__ == "__main__"):
    main()
