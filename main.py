import os
import json
def readbooks():
    with open('Books/list.json', 'r') as f:
        books = json.load(f)
    with open('Books/list.json', 'a') as f:
        json.dump(books[0], f)

def menu():
    print("[INSERT NAME HERE]\n")
    print("" \
    "\nPlease Select an option:" \
    "\n1.   Show Books" \
    "\n2.   Add Book" \
    "\n3.   Remove Book" \
    "\n4.   Exit")
    choice = int(input())
    return choice

def menu_ft(option):
    if option == 1:
        pass

readbooks()