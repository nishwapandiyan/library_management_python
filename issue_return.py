from db import get_connection
from datetime import date


def issue_book(user_id, book_id):
    
    mydb = get_connection()
    cursor = mydb.cursor()
    
    cursor.execute(" SELECT quantity FROM books WHERE book_id = %s",(book_id,))
    result = cursor.fetchone()
    
    if result and result[0] > 0:
        cursor.execute(" INSERT INTO issued_books (user_id, book_id, issue_date, status) VALUES(%s,%s,%s,%s)", (user_id, book_id, date.today(),"issued"))
        
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE book_id = %s", (book_id,))

        mydb.commit()
        print("\nBook Issued Successfully")
    else:
        print("\nBook Not Available")
    mydb.close()
    
    
def return_book(issue_id):
    
    mydb = get_connection()
    cursor = mydb.cursor()
    
    cursor.execute("SELECT issue_date, book_id FROM issued_books WHERE issue_id = %s AND status = %s",(issue_id, 'issued'))

    
    result = cursor.fetchone()
    
    if result:
        issue_date, book_id = result
        days = (date.today() - issue_date).days
        fine = 0
        if days > 7:
            fine = (days - 7) * 5
        cursor.execute("UPDATE issued_books SET return_date = %s, fine = %s, status = %s WHERE issue_id = %s", (date.today(), fine, 'returned', issue_id))

        cursor.execute(" UPDATE books SET quantity = quantity + 1 WHERE book_id = %s",(book_id,))
        
        mydb.commit()
        print(f"\nBook Retunred! Fine:${fine}")
    else:
        print("\nInavlid issue_id!")    
    mydb.close()   
    