from auth import register, login
from library import add_book, view_books
from issue_return import issue_book, return_book

def main():
    while True:
        print("=" * 50)
        print("LIBRARY MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1.Register")
        print("2.Login")
        print("3.Exit")
        print("=" * 50)
        
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            role = input("Enter your Role (admin/user): ")
            
            register(username, password, role)

        elif choice == '2':
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            user = login(username, password)

            if user:
                print("\nLogin Successful!!")
                
                user_id = user[0]
                role = user[3]

                while True:
                    print("*" * 40)
                    print("USER DASHBOARD")
                    print("*" * 40)
                    print("1.View Books")    
                    print("2.Add Book (Admin Only)")    
                    print("3.Issue Book")    
                    print("4.Return Book")    
                    print("5.Logout")   
                    print("*" * 40) 

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        view_books()
                

                    elif choice == '2':
                        if role == 'admin':
                            title = input("Enter the Title: ")
                            author = input("Enter the Author Name: ")
                            quantity = int(input("Quantity of Book: "))
                            add_book(title, author, quantity)
                        else:
                            print("\nAccess Denied! Admin only.")

                    elif choice == '3':
                        book_id = int(input("Enter Book Id: "))
                        issue_book(user_id, book_id)

                    elif choice == '4':
                        issue_id = int(input("Enter Issue Id: ")) 
                        return_book(issue_id)

                    elif choice == '5':
                        print("\nLogged out")
                        break

                    else:
                        print("\nInvalid choice!")

            else:
                print("\nInvalid username or password!")

        elif choice == '3':
            print("\nExited")
            break

        else:
            print("\nInvalid choice!")

if __name__ == "__main__":
    main()
