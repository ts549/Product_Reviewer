from parser.Parser import Parser

url = 'https://www.amazon.com/Amazon-Essentials-Straight-Fit-Jogger-Khaki/product-reviews/B07F2K9R2T/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

parser = Parser(url)

first = True

while (first or next_ref != None):
    first = False
    page = parser.get_page()

    if (page == None): break

    reviews = parser.get_reviews(page)

    for review in reviews:
        print(review.find('a', {'data-hook': 'review-title'}).text)

    next_ref = parser.get_next_page(page)

    if next_ref != None:
        next_path = next_ref.contents[0].get('href')
        parser.set_path(next_path)