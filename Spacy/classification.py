import spacy
from spacy.symbols import nsubj, VERB


nlp = spacy.load('en_core_web_sm')


def count_clauses(sentence):
    doc = nlp(sentence)
    clauses = 0

    # Find the root of the sentence
    root = next(token for token in doc if token.head == token)

    # Traverse the dependency tree to count subordinate clauses
    for token in doc:
        if token != root and token.dep_ in {"advcl", "ccomp", "xcomp"}:
            clauses += 1

    return clauses + 1  # Add 1 for the main clause


def has_dependent_clause(sentence):

    doc = nlp(sentence)
    has_subordinating_conjunction = False
    has_multiple_clauses = False
    has_main_clause = False
    number_of_clauses = count_clauses(sentence)
    for token in doc:
        # print(
        #     f"Processing token: {token.text}: Dependency: {token.dep_}: Part of Speech {token.pos_}")
        if token.dep_ in ['mark']:
            has_subordinating_conjunction = True
        if token.dep_ in ['ROOT']:
            has_main_clause = True
    if(has_subordinating_conjunction and (number_of_clauses > 0) and has_main_clause):
        return True
    else:
        return False


sentences = [
    "When the sun sets, the stars begin to shine.",
    "I went to the store, bought some groceries, and returned home.",
    "She opened the door, stepped outside, and took a deep breath.",
    "He read the book, enjoyed the story, and recommended it to his friends.",
    "They played soccer, laughed and shouted, and had a great time.",
    "The dog wagged its tail, barked happily, and ran towards its owner."
    "When will you arrive?",
    "If it rains tomorrow, we will stay indoors.",
    "After I finish my homework, I will go for a run.",
    "Although it was late, she decided to go for a walk.",
    "Because he studied hard, he passed the exam.",
    "Whenever I see her, I feel happy.",
    "Since I started exercising regularly, I feel more energetic.",
    "As soon as she arrived, the party began.",
    "Unless you hurry, you'll miss the bus.",
    "While I was reading a book, my phone rang."
]


for sentence in sentences:
    print(f"{sentence}:  {has_dependent_clause(sentence)}")  # True


doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
for chunk in doc.noun_chunks:
    print(
        f"text: {chunk.text}, root: {chunk.root.text}, Dep: {chunk.root.dep_}, Head: {chunk.root.head.text}")


doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
          [child for child in token.children])

# Finding a verb with a subject from below — good
print("Finding a verb with a subject from below")
verbs = set()
for possible_subject in doc:
    if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
        verbs.add(possible_subject.head)
print(verbs)


doc = nlp("Credit and mortgage account holders must submit their requests")

root = [token for token in doc if token.head == token][0]
subject = list(root.lefts)[0]
for descendant in subject.subtree:
    assert subject is descendant or subject.is_ancestor(descendant)
    print(descendant.text, descendant.dep_, descendant.n_lefts,
          descendant.n_rights,
          [ancestor.text for ancestor in descendant.ancestors])
