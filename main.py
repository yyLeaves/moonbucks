from Trie import *
from articles import articles

if __name__ == '__main__':
    trie = trie_utils().pickle_load_trie()

    for country in articles.keys():
        article_arr = trie_utils().preprocess(articles[country])
        res = trie.generate_sentiment_search_report(article_arr)
        sentiment = res['sentiment']
        score = trie_utils().get_score(sentiment)
        print(
            f"{country} has {sentiment[0]} neutral words, {sentiment[-1]} negative words, {sentiment[1]} positive words, {sentiment[11]} stop words")
        print(f"{country} has a score of {score}")