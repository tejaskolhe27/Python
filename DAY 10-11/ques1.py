import sqlite3
try:
    conn=sqlite3.connect("employee.db")
    
    print("CONNECTION SUCCESSFUL!!")
except Exception as e:
    print("Error Occurred",e)
    
def addemployee():
    try:
        eid=int(input("Enter EID: "))
        newname=input("Enter NAME: ")
        newsal=float(input("Enter the salary: "))
        cursor.execute(f"insert into employee values({eid},'{newname}',{newsal})");
        conn.commit()
        print("Successfully added")
    except Exception as e:
        print("Error Ocurred",e)
        conn.rollback()

        
def deleteemployee(eid):
    try: 
        cursor.execute(f"delete from employee where eid={eid}");
        conn.commit()
        return True
    except Exception as e:
        print("Error Ocurred",e)
        conn.rollback()
        return False
 
    
def updatebypid(eid,newname,newsalary):
    try:
        cursor.execute(f"update employee  set name='{newname}',salary={newsalary} where eid={eid}");
        conn.commit()
        return True
    except Exception as e:
        print("Error occurred",e)
        conn.rollback()
        return False
    
    
def displayall():
    cursor.execute(("select * from employee"))
    for row in cursor.fetchall():
        print(f"ID:{row[0]} NAME:'{row[1]}' SALARY:{row[2]}")

        
def displaybyid():
    eid=int(input("Enter the employee ID: "))
    cursor.execute(f"select * from employee where eid={eid}")
    for row in cursor.fetchall():
        print(f"ID:{row[0]} NAME:'{row[1]}' SALARY:{row[2]}")
 
        
def salgreater():
    salary=float(input("Enter the salary: "))
    cursor.execute(f"select * from employee where salary>{salary}")
    for row in cursor.fetchall():
        print(f"ID:{row[0]} NAME:'{row[1]}' SALARY:{row[2]}")


cursor = conn.cursor()
choice=0
while choice!=7:
    choice=int(input("""
1. Add new Employee
2. Delete Employee by ID
3. Update Employee by ID
4. Display all employees
5. Display by ID
6. Display employees with sal>given sal
7. Exit
Choice: """))
    match choice:
        case 1:
            addemployee()
        case 2:
            eid=int(input("Enter the EID: "))
            status=deleteemployee(eid)
            if status:
                print("Deleted successfully")
            else:
                print("Invalid PID")
        case 3:
            eid=int(input("Enter EID: "))
            newname=input("Enter new name: ")
            newsalary=float(input("Enter new salary: ")) 
            status=updatebypid(eid,newname,newsalary)
            if status:
                print("Successfully updated")
            else:
                print("Wrong ID entered")
        case 4:
            displayall()
        case 5:
            displaybyid()
        case 6:
            salgreater()
        case 7:
            print("THANK YOU!!!")
            conn.close()