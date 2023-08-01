from sentence_transformers import SentenceTransformer
import utilities


def main():
    text = utilities.read_text_file(
        "./data/Gutenberg/Chapter01/sherlock_holmes_1.txt")
    sentences = utilities.divide_into_sentences_nltk(text)
    print(sentences)
    # The sentence transformer's BERT model is a pre-trained model, just like a word2vec
    # model, that encodes a sentence into a vector. The difference between a word2vec model
    # and a sentence transformer model is that we encode sentences in the latter, and not words.
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    sentence_embeddings = model.encode(sentences)
    sentence_embeddings = model.encode(["the beautiful lake"])

    print("Sentence embeddings:")
    print(sentence_embeddings)


if (__name__ == "__main__"):
    main()
