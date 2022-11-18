from nltk.corpus import wordnet as wn
res = wn.synset('locomotive.n.01').lemma_names()
print(res)
resdef = wn.synset('ocean.n.01').definition()
print(resdef)
res_exm = wn.synset('good.n.01').examples()
print(res_exm)
res_a = wn.lemma('horizontal.a.01.horizontal').antonyms()
print(res_a)
# res_s = wn.lemma('horizontal.a.01.horizontal').synoms()
# print(res_s)
# Then, we're going to use the term "program" to find synsets like so:
syns = wn.synsets("program")

# An example of a synset:
print(syns[0].name())

# Just the word:
print(syns[0].lemmas()[0].name())

# Definition of that first synset:
print(syns[0].definition())

# Examples of the word in use in sentences:
print(syns[0].examples())
synonyms = []
antonyms = []

for syn in wn.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))
