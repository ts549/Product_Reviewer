import pandas as pd
import re
import string

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
