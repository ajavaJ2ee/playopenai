import requests
from bs4 import BeautifulSoup

from pages.book_page import BooksPage

#book_content= requests.get('http://quotes.toscrape.com').content
book_content= requests.get('http://books.toscrape.com').content


page=BooksPage(book_content)

books=page.books

for book in books:
    print(book)
