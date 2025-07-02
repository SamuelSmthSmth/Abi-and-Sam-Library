import os
import json

def readbooks():
    with open('Books/list.json', 'r') as f:
        books = json.load(f)
    return books

def writebooks(booktags): #booktags is a dict type
    with open('Books/list.json', 'r+') as f:
        books = json.load(f) #dict
        books.append(booktags)
        print(books)
        f.seek(0) #moves cursor to the start
        json.dump(books, f, indent = 2)



def menu():
    print("Library\n")
    print("" \
    "\nPlease Select an option:" \
    "\n1.   Show Books" \
    "\n2.   Add Book" \
    "\n3.   Remove Book" \
    "\n4.   Exit")
    choice = int(input())
    return choice

def menu_ft(option):
    books = readbooks()
    if option == 1:
        for i in range(len(books)):
            print(books[i]['title'])
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    else:
        os.system('cls')
        print("That is not an option")
    

while True:
    menu_ft(menu())

