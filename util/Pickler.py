import pickle
import os, os.path

class Pickler:

    def __init__(self):
        self.review_list = []
        self.num_reviews = 0

    def add_review(self, review):
        self.review_list.append(review)
        self.num_reviews += 1

    def pickle_reviews(self):

        reviewers = []
        for i in range(1, self.num_reviews + 1):
            reviewers.append(i)

        for ind, reviewer in enumerate(reviewers):
            with open("reviews/" + str(reviewer) + ".txt", "wb") as file:
                pickle.dump(self.review_list[ind], file)

    def unpack(self):
        data = {}

        DIR = './reviews'
        self.num_reviews = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

        reviewers = []
        for i in range(1, self.num_reviews + 1):
            reviewers.append(i)

        for reviewer in reviewers:
            with open("reviews/" + str(reviewer) + ".txt", "rb") as file:
                data[reviewer] = pickle.load(file)
        
        return data