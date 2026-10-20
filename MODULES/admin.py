import mysql.connector as mcp
from MODULES import public
import random

def create_lottery_session():
    mydb = mcp.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LOTTERY"
    )
    query = "SELECT * FROM SESSIONS"
    cnx = mydb.cursor()
    cnx.execute(query)
    records = cnx.fetchall()
    if records:
        allowed = False
    else:
        allowed = True
    input_start = input("Enter lottery start time (YYYY-MM-DD HH:MM:SS): ")
    input_end = input("Enter lottery end time (YYYY-MM-DD HH:MM:SS): ")
    if allowed:
        try: 
            cnx = mydb.cursor()
            query = f"""INSERT INTO SESSIONS VALUES (DEFAULT, "{input_start}", "{input_end}")"""
            cnx.execute(query)
            mydb.commit()
            cnx.close()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
            return
    else:
        print("A lottery session already exists. Please wait for it to end before creating a new one.")

def create_tables():
    mydb = mcp.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LOTTERY"
    )
    cnx = mydb.cursor()
    user_info = "CREATE TABLE IF NOT EXISTS USERS (user_id INT PRIMARY KEY, name VARCHAR(255), password VARCHAR(255), address VARCHAR(255), phone_number VARCHAR(15), email VARCHAR(255), registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
    lottery_logs = "CREATE TABLE IF NOT EXISTS LOTTERY_LOGS (log_id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, lottery_number VARCHAR(10), date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (user_id) REFERENCES USERS(user_id))"
    sessions = "CREATE TABLE IF NOT EXISTS SESSIONS (session_id INT AUTO_INCREMENT PRIMARY KEY, start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, end_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
    cnx.execute(user_info)
    mydb.commit()
    cnx.execute(lottery_logs)
    mydb.commit()
    cnx.execute(sessions)
    mydb.commit()
    cnx.close()

def initialize_database():
    create_tables()

def login():
    id = input("Enter your ADMIN ID: ")
    password = input("Enter your password: ")
    if id == "admin" and password == "la@1234":
        print("Login successful!")
    initialize_database()
    return "admin"

def view_users():
    mydb = mcp.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LOTTERY"
    )
    cnx = mydb.cursor()
    query = "SELECT * FROM USERS"
    cnx.execute(query)
    users = cnx.fetchall()
    if users:
        print("Users:")
        for user in users:
            print(f"- User ID: {user[0]}, Name: {user[1]}")
    else:
        print("No users found.")

def view_lottery_logs():
    mydb = mcp.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LOTTERY"
    )
    cnx = mydb.cursor()
    query = "SELECT * FROM LOTTERY_LOGS"
    cnx.execute(query)
    logs = cnx.fetchall()
    if logs:
        print("Lottery Logs:")
        for log in logs:
            print(f"- User ID: {log[1]}, Lottery Number: {log[2]}, Date: {log[3]}")
    else:
        print("No lottery logs found.")

def purge_lottery_logs():
    mydb = mcp.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LOTTERY"
    )
    cnx = mydb.cursor()
    query = "DELETE FROM lottery_logs"
    cnx.execute(query)
    mydb.commit()
    cnx.close()

def end_lottery_session():
    mydb = mcp.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LOTTERY"
    )
    lottery_number = pick_lottery_number()
    cnx = mydb.cursor()
    query = "DELETE from SESSIONS"
    cnx.execute(query)
    mydb.commit()
    print(f"The lottery session has ended. The winning lottery number is: {lottery_number}")
    if input("Do you want to purge all lottery logs? (yes/no): ").lower() == "yes" or "y":
        purge_lottery_logs()
    else:
        print("Lottery logs have not been purged.")

def pick_lottery_number():
    mydb = mcp.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LOTTERY"
    )
    cnx = mydb.cursor()
    query = "SELECT lottery_number FROM lottery_logs"
    cnx.execute(query)
    lottery_numbers = []
    for numbers in cnx.fetchall():
        lottery_numbers.append(numbers)
    picked_number = random.choice(lottery_numbers)
    return picked_number

def panel(admin_id):
    print(f"Welcome, {admin_id}!")
    while True:
        print("\nAdmin Panel:")
        print("1. INITIALIZE DATABASE")
        print("2. View Users")
        print("3. View Lottery Logs")
        print("4. Create Lottery Session")
        print("5. Pick Lottery Number")
        print("6. End Lottery Session")
        print("7. Exit")
        choice = input("Select an option (1, 2, 3, 4, 5, 6, or 7): ")
        if choice == "1":
            initialize_database()
        elif choice == "2":
            view_users()
        elif choice == "3":
            view_lottery_logs()
        elif choice == "4":
            create_lottery_session()
        elif choice == "5":
            lottery_number = pick_lottery_number()
            print(f"Picked Lottery Number: {lottery_number}")
        elif choice == "6":
            end_lottery_session()
        elif choice == "7":
            print("Exiting Admin Panel.")
            break
        else:
            print("Invalid option. Please try again.")
