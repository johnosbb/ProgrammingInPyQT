
import utilities

stopwords_file = "./data/Stopwords/stopwords.csv"

yelp_reviews_file = "./data/Yelp/yelp_academic_dataset_review.json"


def main():
    stopwords = utilities.read_in_csv(stopwords_file)
    text = utilities.get_json_as_text(yelp_reviews_file)
    phrases = utilities.get_phrases(text, stopwords)
    text = utilities.replace_phrases(phrases, text)
    utilities.write_text_to_file(text, "./data/all_text.txt")


if (__name__ == "__main__"):
    main()
