import spacy
from spacy.matcher import Matcher

# Reference : https://github.com/PacktPublishing/Python-Natural-Language-Processing-Cookbook/tree/master


def get_clause_token_span_for_verb(verb, doc, all_verbs):
    first_token_index = len(doc)
    last_token_index = 0
    this_verb_children = list(verb.children)
    for child in this_verb_children:
        if (child not in all_verbs):
            if (child.i < first_token_index):
                first_token_index = child.i
            if (child.i > last_token_index):
                last_token_index = child.i
    return(first_token_index, last_token_index)


# The verb with a dependency of ROOT. The top of the syntactic tree
def find_root_of_sentence(doc):
    root_token = None
    for token in doc:
        if (token.dep_ == "ROOT"):
            root_token = token
    return root_token


def find_other_verbs(doc, root_token):
    other_verbs = []
    for token in doc:
        ancestors = list(token.ancestors)
        if (token.pos_ == "VERB" and len(ancestors) == 1  # if it is a verb and has one ancestor which is the root token
                and ancestors[0] == root_token):
            other_verbs.append(token)
    return other_verbs


nlp = spacy.load('en_core_web_sm')
sentence = "He eats cheese, but he won't try ice cream."
doc = nlp(sentence)

for token in doc:
    ancestors = [t.text for t in token.ancestors]
    children = [t.text for t in token.children]
    print(token.text, "\t", token.i, "\t",
          token.pos_, "\t", token.dep_, "\t",
          ancestors, "\t", children)


root_token = find_root_of_sentence(doc)
other_verbs = find_other_verbs(doc, root_token)


token_spans = []
all_verbs = [root_token] + other_verbs
for other_verb in all_verbs:
    (first_token_index, last_token_index) = \
        get_clause_token_span_for_verb(other_verb,
                                       doc, all_verbs)
    token_spans.append((first_token_index,
                        last_token_index))

sentence_clauses = []
for token_span in token_spans:
    start = token_span[0]
    end = token_span[1]
    if (start < end):
        clause = doc[start:end]
        sentence_clauses.append(clause)
sentence_clauses = sorted(sentence_clauses,
                          key=lambda tup: tup[0])

clauses_text = [clause.text for clause in sentence_clauses]
print(clauses_text)


# Ancestors and depenencies
# Consider the following example sentence:
# In this sentence, the word "eats" is the main verb, and "John" and "apple"
# are the noun phrases (or tokens) involved in the action.

# The dependency relation between "eats" and "John" can be labeled as "nsubj" (nominal subject),
# indicating that "John" is the subject of the verb "eats".
# "John eats an apple."

#       eats
#   ┌─────┴─────┐
#  John        apple
# In this tree, "eats" is the root (governing) token, and both "John" and "apple"
# are its dependents (children). "John" is the subject of the verb, and "apple" is the direct object.
# Now, let's consider ancestors.
# If we look at the token "apple", its ancestors are the tokens "eats" and "John"
# because they are higher in the syntactic tree structure. In other words, "apple" is directly governed
# by "eats" and "eats" is directly governed by "John".
