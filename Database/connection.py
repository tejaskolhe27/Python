import sqlite3
try:
    conn = sqlite3.connect("mydb.db")
    print("connection done")
except Exception as e:
    print("error occured",e)


def addnewproduct():
    try:
        newid=int(input("Enter PID: "))
        newname=input("Enter PNAME: ")
        newqty=int(input("Enter the quantity: "))
        newprice=float(input("Enter price: "))
        cursor.execute(f"insert into product values({newid},'{newname}',{newqty},{newprice})");
        conn.commit()
        print("Successfully added")
    except Exception as e:
        print("Error Ocurred",e)
        conn.rollback()


def deletebyid(pid):
    try: 
        cursor.execute(f"delete from product where pid={pid}");
        conn.commit()
        return True
    except Exception as e:
        print("Error Ocurred",e)
        conn.rollback()
        return False

    
def updatebypid(pid,newname,newqty,newprice):
    try:
        cursor.execute(f"update product  set pname='{newname}',qty={newqty},price={newprice} where pid={pid}");
        conn.commit()
        return True
    except Exception as e:
        print("Error occurred",e)
        conn.rollback()
        return False
    
    
def displayall():    
    cursor.execute("select * from product");
    for row in cursor.fetchall():
        print(f"PID: {row[0]} PNAME: {row[1]} QUANTITY: {row[2]} PRICE: {row[3]}")


def displaybyid(): 
    pid=int(input("Enter the ID you want the info of: "))
    cursor.execute(f"select * from product where pid={pid}");
    for row in cursor.fetchall():
        print(f"PID: {row[0]} PNAME: '{row[1]}' QUANTITY: {row[2]} PRICE: {row[3]}")


cursor = conn.cursor()
choice=0
while choice!=6:
    choice=int(input("""
1. Add new product
2. Delete product by ID
3. Update product by ID
4. Display all
5. Display by ID
6. Exit
Choice: """))
    match choice:
        case 1:
            addnewproduct()
        case 2:
            pid=int(input("Enter the PID: "))
            status=deletebyid(pid)
            if status:
                print("Deleted successfully")
            else:
                print("Invalid PID")
        case 3:
            pid=int(input("Enter PID: "))
            newname=input("Enter new name: ")
            newqty=int(input("Enter the quantity: "))
            newprice=float(input("Enter new price: ")) 
            status=updatebypid(pid,newname,newqty,newprice)
            if status:
                print("Successfully updated")
            else:
                print("Wrong ID entered")
        case 4:
            displayall()
        case 5:
            displaybyid()
        case 6:
            print("THANK YOU")
            conn.close()