import mysql.connector as mcp
from MODULES import public
from MODULES import admin

try:
  mydb = mcp.connect(
      host="localhost",
      user="root",
      password="123456",
  )
  cnx = mydb.cursor()
  query = "CREATE DATABASE IF NOT EXISTS LOTTERY"
  cnx.execute(query)
  mydb.commit()
  cnx.close()
except mcp.Error as err:
  print("Technical Error Occurred:", err)

while True:
  input_user = input("""
╔══════════════════════════════════════════╗
║                                          ║
║        LOTTERY MANAGEMENT SYSTEM         ║
║                                          ║
╚══════════════════════════════════════════╝
  Welcome! Please select your account type.
  [1]  Public User     — Get tickets & view entries
  [2]  Administrator   — Manage lottery sessions
  [3]  Exit            — Close the application
────────────────────────────────────────────
  Enter your choice (1-3): """)
  if input_user.strip() == "1":
    user_id = public.resgister_or_login()
    try:
      public.panel(user_id)
    except mcp.Error as err:
      print("Technical Error Occurred:", err)
      print("Returning to Main Menu")
  elif input_user.strip() == "2":
    admin_id = admin.login()
    if admin_id == "admin":
      try:
        admin.panel(admin_id)
      except mcp.Error as err:
        print("Technical Error Occurred:", err)
        print("Returning to Main Menu")
    else:
      print("Failed to log in as Admin. Please try again.")
  elif input_user.strip() == "3":
    print("Exiting the program...")
    break
  else:
    print("Invalid option. Please try again.")
  