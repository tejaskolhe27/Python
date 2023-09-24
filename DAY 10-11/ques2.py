"""
Write a python program to accept username and address from user check whether user exists in
user table. If exists, then display details of user on the screen and if user not found then accept user
details and store it in the table (Use sqlit3)
"""

import sqlite3
try:
    conn=sqlite3.connect("details.db")
    
    print("CONNECTION SUCCESSFUL!!")
except Exception as e:
    print("Error Occurred",e)
    

cursor = conn.cursor()

username=input("Enter the username: ")
add=input("Enter the address: ")
try: 
    cursor.execute(f"select * from details where username='{username}' AND address='{add}'");

    for row in cursor.fetchall():
        print(f"Username:'{row[0]}' ADDRESS:'{row[1]}' MOBILE:{row[2]} EMAIL:'{row[3]}'")
except Exception as e:
    print("ERROR OCCURRED",e)
    
conn.close()