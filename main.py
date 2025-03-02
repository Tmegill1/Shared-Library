from books import book_title
import share_book
import ping_user

def main():
    #books call here for inputs
    print("What is the title of the book?")
    title = input()
    book = books.book_title()
    #share the book using SQL or google sheets
    #ping the other user if book is of interest