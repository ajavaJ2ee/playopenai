import json
"""
storing and retrieving books from list
[
    {'name':'Alchemist1',
     'author':'Paulo coelho',
     'read': False
     },
    {'name':'Alchemist2',
     'author':'Paulo coelho2',
     'read': False
     },
    {'name':'Alchemist3',
     'author':'Paulo coelho3',
     'read': False
     }
]
"""

# From External file

# with open('books.txt','r') as file:
#     books = file.readlines()
#
# print(books.__iter__())
# for book in books:
#     print('book is:{book}')
books_file='books.json'

def create_book_table():
    with open(books_file,'w') as file:
        json.dump([],file)


def add_book(name,author):
    books=get_all_books()
    books.append({'name':name,'author':author,'read':False})
    _save_all_books(books)

    print(f'Books with {name} is added')

def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def mark_book_as_read(name):
    books= get_all_books()
    for book in books:
        if book['name']==name:
            book['read']='True'
    _save_all_books(books)

def _save_all_books(books):
    with open(books_file,'w') as file:
        json.dump(books,file)


def delete_book(name):
    books=get_all_books()
    books=[book for book in books if book['name']!=name]
    _save_all_books(books)

    print(f'Book with {name} is deleted')


