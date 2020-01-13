import re
from bs4 import BeautifulSoup
from locators.book_page_locator import BooksPageLocators
from parsers.book_data import BookParser

class AllBooksPage():

    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, "html.parser")

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(BooksPageLocators.BOOKS)]

    @property
    def totalpages(self):
        content = self.soup.select_one(BooksPageLocators.PAGER).string
        pattern = "Page [0-9] of ([0-9]+)"
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        return pages


