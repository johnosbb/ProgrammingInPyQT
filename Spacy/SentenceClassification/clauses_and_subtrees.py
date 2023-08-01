import spacy
from spacy.matcher import Matcher
import libnlp as lnlp

nlp = spacy.load('en_core_web_sm')


tree = nlp('I never saw the board, because it had flown away.')
tree = nlp("The man walked to work while his wife cycled to the university at the eastern end of the town.")
sentences = [
    "Although it was raining, we decided to go for a walk.",
    "I will go to the party if I finish my work on time.",
    "She studied hard because she wanted to pass the exam.",
    "After he finished his meal, he paid the bill and left.",
    "While I was reading, the phone rang.",
    "The man walked to work while his wife cycled to the university at the eastern end of the town.",
    "Although it was raining, we decided to go for a walk because we had umbrellas.",
    "I will go to the party if I finish my work on time, and I will bring a gift for the host.",
    "She studied hard because she wanted to pass the exam, but she also wanted to impress her professor.",
    "After he finished his meal, he paid the bill and left, but he forgot his keys on the table.",
    "While I was reading, the phone rang, so I had to answer it quickly because it may have been an important call."
]
i = 1
for sentence in sentences:
    tree = nlp(sentence)
    for token in tree:
        if token.dep_ == 'advcl':
            print(f"Sentence {i}")
            print(token, token.i, list(token.subtree))
    lnlp.render(tree)
    lnlp.render_ent(tree)
    lnlp.show_sentence_parts(tree)
    i = i + 1
