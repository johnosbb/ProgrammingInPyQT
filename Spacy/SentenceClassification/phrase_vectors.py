
import utilities
import gensim

stopwords_file = "./data/Stopwords/stopwords.csv"

yelp_reviews_file = "./data/Yelp/yelp_academic_dataset_review.json"
chunksize = 1000


def create_model():
    stopwords = utilities.read_in_csv(stopwords_file)
    text = utilities.get_json_as_text(yelp_reviews_file, chunksize)
    phrases = utilities.get_phrases(text, stopwords)
    text = utilities.replace_phrases(phrases, text)
    utilities.write_text_to_file(text, "./data/all_text.txt")
    sentences = utilities.divide_into_sentences_nltk(text)
    all_sentence_words = [utilities.tokenize_nltk(
        sentence.lower()) for sentence in sentences]
    flat_word_list = [word.lower()
                      for sentence in all_sentence_words for word in sentence]
    fdist = utilities.create_and_save_frequency_dist(
        flat_word_list, "./data/fdist.bin")

    print(fdist.most_common()[:1000])

    phrases_model = utilities.create_and_save_word2vec_model(
        all_sentence_words, "./data/phrases.model")


def main():
    # create_model()

    model = gensim.models.Word2Vec.load("./data/phrases.model")

    words = model.wv.most_similar("highly_recommend", topn=10)
    print(words)
    words = model.wv.most_similar("happy_hour", topn=10)
    print(words)
    words = model.wv.most_similar("fried_rice", topn=10)
    print(words)
    # words = model.wv.most_similar("dim_sum", topn=10)
    # print(words)


if (__name__ == "__main__"):
    main()
