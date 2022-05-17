import pandas as pd
import re
import string
from sklearn.feature_extraction.text import CountVectorizer

from .MaxHeap import MaxHeap

#from MaxHeap import MaxHeap

class TextProcessor:
    
    @staticmethod
    def clean_data(data):
        #Removes unnecessary spaces and newlines
        #Removes punctuation
        #Removes non-alphanumerical characters

        for reviewer, review in data.items():
            review = review.lower()

            review = re.sub('[ \n]([ \n])+', ' ', review)
            review = re.sub('[%s]' % re.escape(string.punctuation), '', review)
            review = re.sub(r'\W', ' ', review)

            data[reviewer] = [review]

    @staticmethod
    def generate_corpus(data):
        #Creates corpus of the reviews

        pd.set_option('max_colwidth', 50)
        
        data_df = pd.DataFrame.from_dict(data).transpose()
        data_df.columns = ['reviews']
        data_df = data_df.sort_index()

        return data_df

    @staticmethod
    def tokenize(corpus, stop_words):
        #Generates document term matrix

        cv = CountVectorizer(stop_words=stop_words)
        data_cv = cv.fit_transform(corpus.reviews)
        dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names_out())
        dtm.index = corpus.index

        return dtm
    
    @staticmethod
    def sort_max_words(dtm):
        #Returns the most common words

        maxq = MaxHeap()

        num_occ = dtm.sum(axis=0)

        for key in num_occ.keys():
            maxq.add([key, num_occ[key]])

        max_words = maxq.to_dict()

        return pd.DataFrame.from_dict(max_words).transpose().sort_index()