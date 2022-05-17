from typing import Text
import pandas as pd
from struct import unpack
from sklearn.feature_extraction import text
from textblob import TextBlob

from util.Parser import Parser
from util.Pickler import Pickler
from util.TextProcessor import TextProcessor
from util.Visualizer import Visualizer

#Initial manual input of URL, will change to interactive input box
url = 'https://www.amazon.com/Amazon-Essentials-Straight-Fit-Jogger-Khaki/product-reviews/B07F2K9R2T/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

parser = Parser(url)
first = True
pickler = Pickler()

#Boolean to decide if need to scrape the URL
pickled = True

while (not pickled and (first or next_ref != None)):
    first = False
    page = parser.get_page()

    if (page == None): break

    reviews = parser.get_reviews(page)

    if (len(reviews) == 0): break

    for review in reviews:
        #Gets the title and review

        title_obj = review.find('a', {'data-hook': 'review-title'})
        body_obj = review.find('span', {'data-hook': 'review-body'})

        if title_obj == None:
            title = ""
        else:
            title = title_obj.text
        
        if body_obj == None:
            body = ""
        else:
            body = body_obj.text

        print(title)
        print(body)

        pickler.add_review(title + body)

    next_ref = parser.get_next_page(page)

    if next_ref != None:
        #Goes to the next page if it exists

        next_path = next_ref.find('a').get('href')
        print(next_path)
        parser.set_path(next_path)

if not pickled:
    pickler.pickle_reviews()

data = pickler.unpack()

TextProcessor.clean_data(data)

corpus = TextProcessor.generate_corpus(data)

hardset_stop_words = ['amazon', 'buy', 'bought', 'buying']
stop_words = text.ENGLISH_STOP_WORDS.union(hardset_stop_words)

while(True):
    dtm = TextProcessor.tokenize(corpus, stop_words)
    dtm = TextProcessor.sort_max_words(dtm)

    new_stop_words = []

    dtm = dtm.transpose()

    for key in dtm.keys():
        #Sentiment Analysis for more cleaning

        if abs(TextBlob(key).sentiment.polarity) > 0.5 and TextBlob(key).sentiment.subjectivity > 0.5:
            new_stop_words.append(key)
    
    if len(new_stop_words) != 0:
        stop_words = stop_words.union(new_stop_words)
    else:
        break

dtm = dtm.transpose()

print(dtm)

Visualizer.generate_word_cloud(dtm, stop_words)