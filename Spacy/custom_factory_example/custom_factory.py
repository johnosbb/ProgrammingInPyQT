import spacy
from spacy.tokens import Token
from spacy.language import Language
import sentiment_analyser




# Load the base English model
nlp = spacy.load("en_core_web_sm")


# Add the custom component to the pipeline
nlp.add_pipe("sentiment_analyzer", last=True)

# Process the text
text = "She was feeling happy after the good news."
doc = nlp(text)

nlp.to_disk("./Models/model_with_custom_factory")
for token in doc:
    print(token.text, token._.is_positive)
