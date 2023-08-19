# Register a custom attribute 'is_positive' for tokens
import spacy
from spacy.tokens import Token
from spacy.language import Language


Token.set_extension("is_positive", default=False)

# Define your data transformation logic


@Language.component("sentiment_analyzer")
def sentiment_analyzer(doc):
    for token in doc:
        # Perform sentiment analysis here and set a custom attribute 'is_positive'
        # For this example, we'll assume positive sentiment for tokens containing 'good'
        if 'good' in token.text.lower():
            token._.is_positive = True
        else:

            token._.is_positive = False
    return doc
