from db import get_connection
from tabulate import tabulate

def add_book(title, author, quantity):
    try:
        mydb = get_connection()
        cursor = mydb.cursor()

        query = "INSERT INTO books (title, author, quantity) VALUES (%s, %s, %s)"
        cursor.execute(query, (title, author, quantity))

        mydb.commit()
        print("Book added successfully!")

    except Exception as e:
        print("Error adding book:", e)

    finally:
        cursor.close()
        mydb.close()


def view_books():
    try:
        mydb = get_connection()
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM books")
        data = cursor.fetchall()
        
        if data:
            record = [col[0] for col in cursor.description]
            print(tabulate(data,record,tablefmt='grid'))
        else:
            print("\nLibrary is Empty")    

    except Exception as e:
        print("Error fetching books:", e)
        return []

    finally:
        cursor.close()
        mydb.close()
