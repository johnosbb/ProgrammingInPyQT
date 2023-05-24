import nltk
nltk.download('treebank')

# Load the Penn Treebank corpus
corpus = nltk.corpus.treebank

# Extract the productions from the corpus
productions = []
for sent in corpus.parsed_sents():
    print("generating ... {}".format(sent))
    productions += sent.productions()

# Convert the productions to Chomsky normal form
start = nltk.Nonterminal('S')
grammar = nltk.CFG(start, productions)
grammar_chomsky = grammar.chomsky_normal_form()

# Save the grammar to a file
with open('grammar_cnf.cfg', 'w') as f:
    f.write(str(grammar_chomsky))
