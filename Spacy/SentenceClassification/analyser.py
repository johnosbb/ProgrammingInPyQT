import spacy
import libnlp as lnlp


nlp = spacy.load('en_core_web_sm')


def main():
    sentence = input("Please enter a sentence:\n")
    doc = nlp(sentence)
    # show_sentence_structure(doc)
    lnlp.show_sentence_parts(doc)
    subject_phrase = lnlp.get_subject_phrase(doc)
    object_phrase = lnlp.get_object_phrase(doc)
    dative_phrase = lnlp.get_dative_phrase(doc)
    prepositional_phrase_objs = lnlp.get_prepositional_phrase_objs(doc)
    print(f"subject_phrase: {subject_phrase}")
    print(f"object_phrase: {object_phrase}")
    print(f"dative_phrase: {dative_phrase}")
    print(f"prepositional_phrase_objs: {prepositional_phrase_objs}")
    clauses = lnlp.get_clauses(doc)
    print("Clauses")
    for clause in clauses:
        print(f"clause: {clause}")
    lnlp.show_noun_chunks(doc)
    print("Verb phrases\n--------\n")
    # (left_np, vp, right_np) = lnlp.find_triplet(doc, nlp)
    phrases = lnlp.find_triplet(doc, nlp)
    for phrase in phrases:
        print(phrase[0], "\t", phrase[1], "\t", phrase[2])
    # print(left_np, "\t", vp, "\t", right_np)
    lnlp.render(doc)


if (__name__ == "__main__"):
    main()
