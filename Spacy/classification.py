import spacy

# Load the pre-trained model
nlp = spacy.load('en_core_web_sm')

# Example sentences
sentences = [
    "I loved the movie! The acting was superb.",
    "The food at the restaurant was terrible. I wouldn't recommend it.",
]

print(nlp.pipe_names)  # Prints the pipeline components
print(nlp.meta['cats'])  # Prints the available categories and labels


# Process each sentence and classify
for sentence in sentences:
    doc = nlp(sentence)

    # Access the sentence classification using the .cats attribute
    positive_sentiment = doc.cats['POSITIVE']
    negative_sentiment = doc.cats['NEGATIVE']

    # Print the results
    print(f"Sentence: {sentence}")
    print(f"Positive sentiment: {positive_sentiment:.2f}")
    print(f"Negative sentiment: {negative_sentiment:.2f}")
    print()
