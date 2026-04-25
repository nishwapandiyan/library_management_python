from db import get_connection
import hashlib

def register(username, password, role):
    try:
        mydb = get_connection()
        cursor = mydb.cursor()


        hashed = hashlib.sha256(password.encode()).hexdigest()

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            print("\nUsername already exists!")
            return

        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
            (username, hashed, role)
        )

        mydb.commit()
        print("\nRegistration Successful!!")

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        mydb.close()


def login(username, password):
    try:
        mydb = get_connection()
        cursor = mydb.cursor()

        hashed = hashlib.sha256(password.encode()).hexdigest()

        cursor.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s",
            (username, hashed)
        )

        user = cursor.fetchone()
        return user

    except Exception as e:
        print("Error:", e)
        return None

    finally:
        cursor.close()
        mydb.close()
