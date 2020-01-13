import re
from locators.book_locator import BookLocators

class BookParser:

    RATINGS = {
        "One":   1,
        "Two":   2,
        "Three": 3,
        "Four":  4,
        "Five":  5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"BOOK: {self.name}, Price: ${self.price}, Rating: {self.rating} Star"


    @property
    def name(self):
        locator = BookLocators.NAME
        item_link = self.parent.select_one(locator) #CSS Locator
        item_name = item_link.attrs["title"]
        return item_name

    @property
    def link(self):
        locator = BookLocators.LINK
        item_link = self.parent.select_one(locator)  # CSS Locator
        item_link_name = item_link.attrs["href"]
        return item_link_name

    @property
    def price(self):
        locator = BookLocators.PRICE
        price_is = self.parent.select_one(locator).string
        pattern = "£(([0-9]+)\.[0-9]+)"
        matcher = re.search(pattern, price_is)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = BookLocators.RATING
        rating_is = self.parent.select_one(locator)
        classes = rating_is.attrs["class"]
        class_rating_is = [r for r in classes if r != "star-rating"]
        rating_num = BookParser.RATINGS.get(class_rating_is[0])
        return rating_num