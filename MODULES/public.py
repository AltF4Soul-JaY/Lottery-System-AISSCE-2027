import datetime
import mysql.connector as mcp
from MODULES import admin
import random

def user_id_generator():
    mydb = mcp.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LOTTERY"
    )
    cnx = mydb.cursor()
    query = "SELECT user_id FROM USERS"
    cnx.execute(query)
    existing_ids = [row[0] for row in cnx.fetchall()]
    while True:
        user_id = random.randint(100000, 999999)
        if user_id not in existing_ids:
            break
    return user_id

def register_user():
    mydb = mcp.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LOTTERY"
    )
    input_name = input("Enter your name: ")
    password = input("Enter your password: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    user_id = user_id_generator()

    query = f"""INSERT INTO USERS VALUES
    ({user_id}, "{input_name}", "{password}", "{address}", "{phone_number}", "{email}", DEFAULT)"""

    cnx = mydb.cursor()
    cnx.execute(query)
    mydb.commit()
    cnx.close()
    return user_id

def user_login():
    id = input("Enter your USER ID: ")
    password = input("Enter your password: ")
    mydb = mcp.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LOTTERY"
    )
    cnx = mydb.cursor()
    query = f"SELECT * FROM USERS WHERE user_id = {id} AND password = '{password}'"
    cnx.execute(query)
    result = cnx.fetchall()
    for row in result:
        if row[0] == int(id) and row[2] == password:
            print("Login successful!")
        cnx.close()
        return id
    else:
        print("Invalid USER ID or password.")
        print("Please register if you don't have an account.")
        cnx.close()

def resgister_or_login():
    while True:
        choice = input("Do you want to register or login? (r/l): ")
        if choice.lower() == 'r':
            user_id = register_user()
            print(f"Registration successful! Your USER ID is: {user_id}")
            return user_id
        elif choice.lower() == 'l':
            user_id = user_login()
            if user_id:
                return user_id
            else:
                print("Invalid USER ID or password.")
                return None
        else:
            print("Invalid choice. Please enter 'r' to register or 'l' to login.")

def panel(user_id):
    while True:
        print(f"Welcome, User {user_id}!")
        print("Choose an option:")
        print("1. Join Lottery")
        print("2. View My Lottery Tickets")
        print("3. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            join_lottery(user_id)
        elif choice == "2":
            view_lottery_tickets(user_id)
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def join_lottery(user_id, database="LOTTERY"):
    with mcp.connect(
        host="localhost",
        user="root",
        password="123456",
        database=database
    ) as mydb:
        cnx = mydb.cursor()
        query = """
        SELECT * FROM SESSIONS
    """
        cnx.execute(query)
        records = cnx.fetchall()
        for sessions in records:
            now = datetime.datetime.now()
            if now >= sessions[2]:
                print("The lottery session has ended. Please wait for the next session.")
            elif now < sessions[1]:
                print("The lottery session has not started yet. Please wait for the next session.")
            else:
                lottery_number = ticket()
                query = f"INSERT INTO LOTTERY_LOGS (user_id, lottery_number) VALUES ({user_id}, '{lottery_number}')"
                cnx.execute(query)
                mydb.commit()
                print(f"You have successfully joined the lottery! Your lottery number is: {lottery_number}")

def view_lottery_tickets(user_id, database="LOTTERY"):
    with mcp.connect(
        host="localhost",
        user="root",
        password="123456",
        database=database
    ) as mydb:
        cnx = mydb.cursor()
        query = f"SELECT * FROM LOTTERY_LOGS WHERE user_id = {user_id}"
        cnx.execute(query)
        tickets = cnx.fetchall()
        if tickets:
            print("Your lottery tickets:")
            for ticket in tickets:
                print(f"- Lottery Number: {ticket[2]}")
        else:
            print("You have no lottery tickets.")

def ticket():
    mydb = mcp.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LOTTERY"
    )
    cnx = mydb.cursor()
    query = "SELECT lottery_number FROM LOTTERY_LOGS"
    cnx.execute(query)
    existing_numbers = [row[0] for row in cnx.fetchall()]
    temp_char = "#"
    ticket_number = temp_char + str(random.randint(100000, 999999))
    while ticket_number in str(existing_numbers):
        ticket_number = temp_char + str(random.randint(100000, 999999))
    return ticket_number