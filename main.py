import os
import json

def readbooks():
    with open('Books/list.json', 'r') as f:
        books = json.load(f)
    return books

def writebooks(booktags): #booktags is a dict type
    with open('Books/list.json', 'r+') as f:
        books = json.load(f) #books is a list!
        books.append(booktags)
        f.seek(0) #moves cursor to the start
        json.dump(books, f, indent = 2)

def delbooks(booktags): #booktags is a library
    with open('Books/list.json', 'r+') as f:
        books = json.load(f) #books is a list of dictionaries
        books.remove(booktags)
        print(books)
        f.seek(0) #moves cursor to the start
        json.dump(books, f, indent = 2)




def menu():
    print("" \
    "\nPlease Select an option:" \
    "\n1.   Show Books" \
    "\n2.   Add Book" \
    "\n3.   Remove Book")
    choice = int(input())
    return choice

def menu_ft(option):
    books = readbooks()
    if option == 1:
        for i in range(len(books)):
            print(books[i]['title'])
    elif option == 2:
        title = input('title    ')
        author = input('author  ')
        genre = input('genre    ')
        bookmd = dict(title=title, author=author, genre=genre)
        writebooks(bookmd)
    elif option == 3:
        title = input('title    ')
        author = input('author  ')
        genre = input('genre    ')
        bookmd = dict(title=title, author=author, genre=genre)
        delbooks(bookmd)
    else:
        os.system('cls')
        print("That is not an option")
    

while True:
    menu_ft(menu())

