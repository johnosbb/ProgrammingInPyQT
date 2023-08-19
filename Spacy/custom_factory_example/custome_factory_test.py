# An example of trying to use a previous model that referenced a custom factory. The model fail because in that instance the factory was not packaged with the model
import spacy
from spacy.language import Language
#import sentiment_analyser

#nlp_new = spacy.load("./Models/model_with_custom_factory")
nlp_new = spacy.load("en_core_web_sm_ex")
text = "This is a string with good or positive sentiment"
doc = nlp_new(text)
for token in doc:
    print(token.text, token._.is_positive)
