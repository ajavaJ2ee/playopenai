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
books_file='books.txt'

def create_book_table():
    with open(books_file,'w'):
        pass
#def addblock():

def add_book(name,author):
    with open(books_file,'a') as file:
        file.write(f'{name},{author},0\n')
    print(f'Books with {name} is added')

def get_all_books():
    with open(books_file, 'r') as file:
        lines=[ line.strip().split(',') for line in file.readlines()]
    # for line in lines:
    #     print(f'line is:{line}')
    books= [
        {'name':line[0],'author':line[1],'read':line[2]}
        for line in lines
    ]
    return books



def mark_book_as_read(name):
    books= get_all_books()
    for book in books:
        if book['name']==name:
            book['read']='1'
    _save_all_books(books)

def _save_all_books(books):
    with open(books_file,'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{[book['read']]}\n")


def delete_book(name):
    name = input('Please enter the book  name ')

    books=get_all_books()
    books=[book for book in books if book['name']!=name]
    _save_all_books(books)
    # for book in books:
    #     if book['name'] == name:
    #         books.remove(book)
    #         print(f'Book with {name} is deleted')
    #books = [book for book in books if book['name'] != name]
    print(f'Book with {name} is deleted')


