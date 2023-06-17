import wikipediaapi


def get_wikipedia_article(title):
    wiki = wikipediaapi.Wikipedia('en')  # Create a Wikipedia object
    page = wiki.page(title)  # Get the Wikipedia page

    if page.exists():
        return page.text  # Return the text content of the article
    else:
        return None  # Return None if the article does not exist


# Example usage
article_title = 'Martin Luther King'
article_text = get_wikipedia_article(article_title)
print(article_text)
with open("data/wiki_mlk.txt", "w") as f:
    f.write(article_text)
