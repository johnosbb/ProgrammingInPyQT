import nltk
from nltk.tokenize import word_tokenize
from nltk import RecursiveDescentParser

# Define a function to parse a sentence using the default grammar


def parse_sentence(sentence):
    # Tokenize the sentence
    tokens = word_tokenize(sentence)

    # Set up the recursive descent parser with the default grammar
    parser = RecursiveDescentParser(
        nltk.data.load('/home/johnos/nltk_data/grammars/large_grammars/atis.cfg'))

    # Parse the sentence with the recursive descent parser
    parse_tree = next(parser.parse(tokens))

    return parse_tree


# Example sentence
sentence = "What flights are available from Boston to New York on Thursday?"

# Parse the sentence
tree = parse_sentence(sentence)

# Print the parse tree
print(tree)
