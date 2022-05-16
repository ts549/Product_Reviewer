import pickle

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