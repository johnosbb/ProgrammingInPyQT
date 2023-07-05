import spacy
from spacy.matcher import Matcher
import libnlp as lnlp

# Reference : https://github.com/PacktPublishing/Python-Natural-Language-Processing-Cookbook/tree/master


nlp = spacy.load('en_core_web_sm')
#sentence = "He eats cheese, but he won't try ice cream."
sentence = "The man walked to work while his wife cycled to the university at the eastern end of the town."
doc = nlp(sentence)
# show_sentence_structure(doc)
lnlp.show_sentence_parts(doc)
clauses = lnlp.get_clauses(doc)
print("Clauses")
for clause in clauses:
    print(f"clause: {clause}")


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
