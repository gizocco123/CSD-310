import mysql.connector
import sys
from mysql.connector import errorcode

connection = {
    "user": "whatabook_user",
    "host": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

cursor = connection.cursor()
query="Select user_user_id, user.first_name, user.last_name, user.user_name FROM user INNER JOIN user ON user.users_id=users.user_id"
cursor.execute(query)
rows=cursor.fetchall()
for x in rows:
    print(x)

connection.close()

def show_menu():
    print("Welcome to Main Menu")
    print("Browse Books")
    print("Store Locale")
    print("user_menu")
    print("Exit")

    try:
        user_choice = int(input(' <Ex : 1 for book listing>: '))
        
        return user_choice
    except ValueError:
        print("Invalid Selection")

        sys.exit(0)

def show_locale(): 
    locale = cursor.fetchall()
    print(store_locale)

def user_validation():
    try:
        user_id = int(input('\n   Type your name   >: '))

        if not Zac:
            print("\n  Incorrect User  \n")
            sys.exit(0)

        if not Nader:
            print("\n  Incorrect User  \n")
            sys.exit(0) 

        if not Gino:
            print("\n  Incorrect User  \n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Not a user  \n")

        sys.exit(0)

    

def show_user_menu():
    try:
        print("\n -- User Menu --")
        print("        1. Select book    2. Wishlist   3. User Menu")
        user_option = int(input('    <Ex: 3 for User Menu>: '))

        return user_option
    except ValueError:
        print("Invalid Selection")

        sys.exit(0)

def show_books(cursor):
    # inner join 
    cursor.execute("SELECT book_id, book_name, author, book details")

    books = cursor.fetchall()

    print("\n Displaying Books ")
    
    # loop
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

def add_book_to_wishlist(cursor, user_id, _book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    
    db = mysql.connector.connect(config) 

    cursor = db.cursor()

    print("\n  WhatAbook database ")
    

    cursor = show_menu()
        # if user input is wrong
    if cursor < 0 or cursor > 9:
            print("\n  Invalid Selection, please enter a valid selection")
            
            cursor = show_menu()
  
finally:
    db.close()