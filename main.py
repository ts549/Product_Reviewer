from struct import unpack
from util.Parser import Parser
from util.Pickler import Pickler
from util.TextProcessor import TextProcessor

url = 'https://www.amazon.com/Amazon-Essentials-Straight-Fit-Jogger-Khaki/product-reviews/B07F2K9R2T/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

parser = Parser(url)

#parser.set_path('/Amazon-Essentials-Straight-Fit-Jogger-Khaki/product-reviews/B07F2K9R2T/ref=cm_cr_arp_d_paging_btm_80?ie=UTF8&pageNumber=80')

first = True

pickler = Pickler()

pickled = True

while (not pickled and (first or next_ref != None)):
    first = False
    page = parser.get_page()

    if (page == None): break

    reviews = parser.get_reviews(page)

    if (len(reviews) == 0): break

    for review in reviews:
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
        #next_path = next_ref.contents[0].get('href')
        next_path = next_ref.find('a').get('href')
        print(next_path)
        parser.set_path(next_path)

if not pickled:
    pickler.pickle_reviews()

data = pickler.unpack()

print(data[1])