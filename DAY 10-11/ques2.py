import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='phpmyadmin',password='dai', db='test')

if conn!=None:
    print("connection done")
else:
    print("fail")

cursor = conn.cursor()



#display all the records
def displayall():
    cursor.execute("select * from product")
    for row in cursor.fetchall():  #[(123,"xx",34,3456),(124,yyyy,56,7777)]
        print(f"pid: {row[0]} pname: {row[1]} qty: {row[2]} price: {row[3]}")

def displaybyid(pid):
    try:
        cursor.execute("select * from product where pid=%s",(pid))
        #cursor.execute(f"select * from product where pid={pid}")
        row=cursor.fetchone()
        print(f"pid: {row[0]} pname: {row[1]} qty: {row[2]} price: {row[3]}")
    except Exception as e:
        print("error occured",e)

def addnewproduct():
    try:
        pid=int(input("enetr pid"))
        pnm=input("enetr name")
        qty=int(input("enetr pid"))
        price=float(input("enetr pid"))
        cursor.execute("insert into product values(%s,%s,%s,%s)",(pid,pnm,qty,price))
        conn.commit()
    except Exception as e:
        print("error ocuured ",e)
        conn.rollback()

def deletebyid(pid):
    try:
        cursor.execute("delete from product where pid=%s",(pid,))
        conn.commit()
        return True
    except Exception as e:
        print("error ocuured ",e)
        conn.rollback()
        return False

def updatebyid(pid,pnm,qty,pr):
    try:
        cursor.execute("update product set pname=%s,qty=%s,price=%s where pid=%s",(pnm,qty,pr,pid))
        conn.commit()
        return True
    except Exception as e:
        print("error ocuured ",e)
        conn.rollback()
        return False
    
cursor=conn.cursor()
choice=0
while choice!=6:
    choice=int(input("""
                     1. add new product
                     2. delete product by id
                     3. update product by id
                     4. display all
                     5. display by id
                     6. exit"""))
    match choice:
        case 1:
            addnewproduct()
        case 2:
            pid=int(input("enter id"))
            status=deletebyid(pid)
            if status:
                print("deleted successfully")
            else:
                print("not found")
        case 3:
            pid=int(input("enter id"))
            pnm=input("enter new name")
            qty=int(input("enter new qty"))
            pr=float(input("enter new price"))
            status=updatebyid(pid,pnm,qty,pr)
            if status:
                print("updated successfully")
            else:
                print("not found")
        case 4:
            displayall()
        case 5:
            pid=int(input("enter id"))
            displaybyid(pid)
        case 6:
            print("Thank you for visiting....")
            conn.close()