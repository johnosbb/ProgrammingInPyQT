import time
import nltk
import spacy
import string
import csv
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import KeyedVectors
import numpy as np
from nltk import FreqDist
import gensim
import pickle
from os import listdir
from os.path import isfile, join
import json
import pandas as pd
from langdetect import detect

tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
nlp = spacy.load("en_core_web_sm")
stemmer = SnowballStemmer('english')


def train_word2vec(words, word2vec_model_path):
    # model = gensim.models.Word2Vec(
    #    words,
    #    size=50,
    #    window=7,
    #    min_count=1,
    #    workers=10)
    model = gensim.models.Word2Vec(words, window=5, size=200, min_count=5)
    model.train(words, total_examples=len(words), epochs=200)
    pickle.dump(model, open(word2vec_model_path, 'wb'))
    return model


def create_and_save_word2vec_model(words, filename):
    model = gensim.models.Word2Vec(words, min_count=1)
    model.train(words, total_examples=model.corpus_count, epochs=400)
    pickle.dump(model, open(filename, 'wb'))
    return model


def evaluate_model(model, filename):
    return model.wv.evaluate_word_analogies(filename)


def get_phrases(text, stopwords):
    words = nltk.tokenize.word_tokenize(text)
    phrases = {}
    current_phrase = []
    for word in words:
        if (word in stopwords or word in string.punctuation):
            if (len(current_phrase) > 1):
                phrases[" ".join(current_phrase)] = "_".join(current_phrase)
                current_phrase = []
        else:
            current_phrase.append(word)
    if (len(current_phrase) > 1):
        phrases[" ".join(current_phrase)] = "_".join(current_phrase)
    return phrases


def tokenize_nltk(text):
    return nltk.tokenize.word_tokenize(text)


def get_all_book_sentences(directory):
    text_files = [join(directory, f) for f in listdir(
        directory) if isfile(join(directory, f)) and ".txt" in f]
    all_sentences = []
    for text_file in text_files:
        sentences = get_sentences(text_file)
        all_sentences = all_sentences + sentences
    return all_sentences

# Model Training Parameters:
# min_count is the minimum number of times a word
# has to occur in the training corpus, with the default being 5. The size parameter sets the
# size of the word vector. window restricts the maximum number of words between the
# predicted and current word in a sentence. workers is the number of working threads;
# the more there are, the quicker the training will proceed. When training the model, the
# epoch parameter will determine the number of training iterations the model will
# go through.


def train_word2vec(words, word2vec_model_path):
    # model = gensim.models.Word2Vec(
    #    words,
    #    size=50,
    #    window=7,
    #    min_count=1,
    #    workers=10)
    model = gensim.models.Word2Vec(
        words, window=5, vector_size=200, min_count=1)
    model.train(words, total_examples=len(words), epochs=200)
    pickle.dump(model, open(word2vec_model_path, 'wb'))
    return model


def show_vector_matrix(vectorizer, matrix):
    # Convert sparse matrix to COO format
    matrix_coo = matrix.tocoo()
    feature_names = vectorizer.get_feature_names_out()
    densematrix = matrix.todense()
    print(f"Dense Matrix: {densematrix}")
    print(f"Sparse Matrix: \n")
    for row, col, value in zip(matrix_coo.row, matrix_coo.col, matrix_coo.data):
        print(
            f"Row: {row}, Index: {col}, Value: {value} Term: {feature_names[col]}")


def create_and_save_frequency_dist(word_list, filename):
    fdist = FreqDist(word_list)
    pickle.dump(fdist, open(filename, 'wb'))
    return fdist


def read_in_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as fp:
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        data_read = [row[0] for row in reader]
    return data_read


def replace_phrases(phrases_dict, text):
    for phrase in phrases_dict.keys():
        text = text.replace(phrase, phrases_dict[phrase])
    return text


def read_text_file(filename):
    file = open(filename, "r", encoding="utf-8")
    return file.read()


def write_text_to_file(text, filename):
    text_file = open(filename, "w", encoding="utf-8")
    text_file.write(text)
    text_file.close()


def get_json_as_text(filename):
    reader = pd.read_json(filename, orient="records",
                          lines=True, chunksize=10000)
    chunk = next(reader)
    text = ''
    for index, row in chunk.iterrows():
        row_text = row['text']
        lang = detect(row_text)
        if (lang == "en"):
            text = text + row_text.lower()
    return text


def preprocess_text(text):
    text = text.replace("\n", " ")
    return text


def divide_into_sentences_nltk(text):
    sentences = tokenizer.tokenize(text)
    return sentences

# Out-of-vocabulary words: Character n-gram models are more robust when dealing with out-of-vocabulary words, i.e.,
# words that are not present in the training data.
# Since character n-grams operate on individual characters,
# they can still capture useful information from unseen words by considering their character-level patterns.
# In contrast, word-based models typically struggle
# with out-of-vocabulary words because they treat each word as a discrete unit.

# Morphologically rich languages: Character n-gram models are particularly useful for morphologically rich languages,
# where words undergo various inflections and morphological changes.
# By considering character-level information, these models can capture the underlying morphological
# structure and handle word forms more effectively.
# In such cases, word-based models may struggle due to the increased vocabulary size and sparsity.

# Misspellings and noisy text: Character n-gram models can handle misspelled words and noisy text better
# than word-based models. By considering the character-level patterns,
# these models can identify similarities between correct and misspelled versions of words,
# improving their ability to recognize and correct misspellings

# Short and contextually ambiguous text: In scenarios where the input text is short or lacks sufficient context,
# character n-gram models can often provide more reliable results.
# By focusing on character-level patterns, these models can leverage smaller units of information
# and make predictions based on the available characters, even when the overall context is limited.


def create_char_vectorizer_tfid(sentences):
    # Create TF-IDF object
    tfidf_char_vectorizer = TfidfVectorizer(analyzer='char_wb', max_df=0.90, max_features=200000,
                                            min_df=0.05, use_idf=True, ngram_range=(1, 3))
    tfidf_char_vectorizer = tfidf_char_vectorizer.fit(sentences)
    tfidf_matrix = tfidf_char_vectorizer.transform(sentences)
    return (tfidf_char_vectorizer, tfidf_matrix)


# Word frequencies are calculated as follows. For each word, the overall
# frequency is a product of the term frequency and the inverse document frequency. Term
# frequency is the number of times the word occurs in the document. Inverse document
# frequency is the total number of documents divided by the number of documents where
# the word occurs.

def create_vectorizer_tfid(sentences, stopword_list):
    # Create TF-IDF object

    stemmed_stopwords = [tokenize_and_stem(
        stopword)[0] for stopword in stopword_list]
    stopword_list = stopword_list + stemmed_stopwords
    tfidf_vectorizer = TfidfVectorizer(max_df=0.90, max_features=200000,
                                       min_df=0.05, stop_words=stopword_list,
                                       use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1, 3))
    tfidf_vectorizer = tfidf_vectorizer.fit(sentences)
    tfidf_matrix = tfidf_vectorizer.transform(sentences)
    return (tfidf_vectorizer, tfidf_matrix)


def get_w2vec_word_vectors(sentence, model):
    word_vectors = []
    for word in sentence:
        try:
            word_vector = model.get_vector(word.lower())
            word_vectors.append(word_vector)
        except KeyError:
            continue
    return word_vectors

# In the function below we average the word vectors. Averaging the word vectors to get the sentence vector is only one way of
# approaching this task, and is not without its problems. One alternative is to
# train a doc2vec model, where sentences, paragraphs, and whole documents can
# all be units instead of words.


def get_w2vec_sentence_vector(word_vectors):
    matrix = np.array(word_vectors)
    centroid = np.mean(matrix[:, :], axis=0)
    return centroid  # returns the average vector length


def load_w2vec_model(w2vec_model_path):
    model = KeyedVectors.load_word2vec_format(w2vec_model_path, binary=True)
    return model


def tokenize_and_stem(sentence):
    tokens = nltk.word_tokenize(sentence)
    filtered_tokens = [t for t in tokens if t not in string.punctuation]
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def divide_into_sentences_spacy(text):
    doc = nlp(text)
    return [sentence.text for sentence in doc.sents]


def divide_into_sentences(text):
    return divide_into_sentences_nltk(text)


def get_sentences(filename):
    text = read_text_file(filename)
    text = preprocess_text(text)
    sentences = divide_into_sentences_nltk(text)
    return sentences
