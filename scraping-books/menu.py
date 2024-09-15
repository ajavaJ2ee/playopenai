from app import books


USER_CHOICE="""
Enter one of the following
-'b' for 5-star
-'c' to look at cheapest books
-'n' to just get next available book on the catalogue
-'q' to quit

Enter your choice:"""

def sort_best_book():
    best_books=sorted(books, key=lambda x: x.rating)[:10]
    for book in best_books:
        print(book)
def sort_cheap_book():
    cheap_book=sorted(books,key=lambda x:x.price)
    for book in cheap_book:
        print(book)


books_generator= (book for book in books)

def get_next_book():
    print(next(books_generator))

'''
Shorter implementation
'''
user_choices={
    'b':sort_best_book,
    'c':sort_cheap_book,
    'n':get_next_book
}

def menu():
    user_input=input(USER_CHOICE)
    while user_input!='q':
        if user_input in ('b','c','n'):
            user_choices[user_input]()
        else:
            print('Please choose a valid command')
        user_input=input(USER_CHOICE)

'''
Lengthy implementation
'''
# def menu():
#     user_input=input(USER_CHOICE)
#     while user_input!='q':
#         if user_input=='b':
#             sort_best_book()
#         elif user_input=='c':
#             sort_cheap_book()
#         elif user_input=='n':
#             get_next_book()
#         else:
#             print('Please choose a valid command')
#         user_input=input(USER_CHOICE)
# sort_best_book()
# print('CHEAPPP')
# sort_cheap_book()

menu()