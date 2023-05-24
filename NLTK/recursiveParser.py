import nltk
from nltk.tokenize import word_tokenize
from nltk import RecursiveDescentParser

# Define a grammar for the parser
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'man' | 'woman'
    V -> 'chased' | 'saw' | 'bit' | 'loved'
    P -> 'in' | 'on' | 'by' | 'with'
""")

# Define a function to parse a sentence


def parse_sentence(sentence):
    # Tokenize the sentence
    tokens = word_tokenize(sentence)

    # Set up the recursive descent parser
    parser = RecursiveDescentParser(grammar)

    # Parse the sentence with the recursive descent parser
    parse_tree = next(parser.parse(tokens))

    return parse_tree


# Example sentence
sentence = "the cat chased the dog"

# Parse the sentence
tree = parse_sentence(sentence)

# Print the parse tree
print(tree)
