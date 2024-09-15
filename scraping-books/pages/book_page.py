from bs4 import BeautifulSoup

from locators.books_page_locator import BooksPageLocators
from parsers.book_parser import BooksParser


class BooksPage:
    def __init__(self,page_content):
        self.soup=BeautifulSoup(page_content,'html.parser')

    # @property
    # def books(self):
    #     locator=BooksPageLocators.BOOKS
    #     books_tags=self.soup.select(locator)
    #     return [BooksParser(e) for e in books_tags]
    @property
    def books(self):
        return [BooksParser(e) for e in self.soup.select(BooksPageLocators.BOOKS)]