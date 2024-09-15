import requests
import logging
from pages.book_page import BooksPage
'''
Abhi's implementation
'''
# book_content_page=[]
# for i in range(1,10):
#     url=f'http://books.toscrape.com/catalogue/page-{i}.html'
#     book_content_page.append(requests.get(url).content)
#
# def book_content():
#     for book_content in book_content_page:
#         page=BooksPage(book_content)
#         books = page.books
#         for book in books:
#             print(book)
#         print('Printed')
#
# book_content()

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H%:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger= logging.getLogger('scraping')

logger.info('Multiple pages Books app')

'''
Tutor implementation
'''
page_content=requests.get('http://books.toscrape.com').content
page= BooksPage(page_content)

books= page.books


for page_num in range(1,10):
    url=f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content=requests.get(url).content
    logger.debug('Creating books content from all pages')
    page=BooksPage(page_content)
    books.extend(page.books)





