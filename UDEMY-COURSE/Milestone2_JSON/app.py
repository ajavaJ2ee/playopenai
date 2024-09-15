from utils_json import database_json

USER_CHOICE="""
Enter:
- 'a' to add a new book
- 'l' to list 
- 'r' to mark 
- 'd' to delete 
- 'q' to quit

your choice:"""

def menu():
    database_json.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input!='q':
        if user_input=='a':
            prompt_add_book()
            #exit()
        elif user_input=='l':
            list_books()
            #exit()
        elif user_input=='r':
            prompt_read_book()
            #exit()
        elif user_input=='d':
            prompt_delete_book()
            #exit()
        else:
            print('Unknown command')
        user_input = input(USER_CHOICE)
def prompt_add_book():
    name=input('Please enter the book  name ')
    author = input('Please enter the author  name ')
    database_json.add_book(name,author)
def prompt_read_book():
    name = input('Please enter the book  name ')
    database_json.mark_book_as_read(name)
def prompt_delete_book():
    name = input('Please enter the book  name ')
    database_json.delete_book(name)
def list_books():
    books=database_json.get_all_books()
    for book in books:
        read= True if book['read']==1 else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")

menu()

