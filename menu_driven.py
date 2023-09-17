import sys
courselist = [("DAI",40),("DBDA",60)]

def addnewcourse():
    new=input("Enter the name of new course: ")
    cap= int(input("Enter the capacity of new course: "))
    courselist.append((new,cap))
    return True

# def deletecourse():
#     delete=int(input("Enter course to delete: "))
#     for i in courselist:
#         if delete==courselist[i]



def searchbycname(old):
    for pos,c in enumerate(courselist): #[(0,("DBDA",100)),(1,("DAI",40)))
        if c[0]==old:
            return pos,c
    else:
        return -1,None
    
       
def modifycoursecapacity(cname,ccap):
    pos,cdetails=searchbycname(cname)
    if pos!=-1:
        ans=input(f"Do you want to modify the course {cname} with new capacity {ccap}: ")
        if ans=='y':
            courselist[pos]  =(cdetails[0],ccap)
            return 1
        else:
            return 2
    else:
        return 3



def modifybycourseName(old,new):
    pos,cdetails=searchbycname(old)
    if pos!=-1:
        ans=input(f"Do you want to modify {old} with {new}: ")
        if ans=="y":
            courselist[pos]=(new,cdetails[1])
            return 1
        else:
            return 2
    else:
        return 3



def display():
    print("THE COURSES WITH CAPACITY ARE: ")
    for x,y in courselist:
        print(x,"----->",y)

def givencapacity():
    c=int(input("Enter capacity: "))
    for cname,capa in courselist:
        if(capa>c):
            print(cname,"---->",capa)



choice=0
while choice!=7:
    choice = int(input("""
    1. add new course
    2. delete the course
    3. modify course capacity
    4. modify course name
    5. display all
    6. display only courses with capacity > given capacity
    7. exit
    choice:"""))
    if choice==1:
        status=addnewcourse()

        if status:
            print("New course added!!!")
        else:
            print("New course not added")

    elif choice==2:
        pass

    elif choice ==3:
        cname=input("Enter course name to modify capacity: ")
        ccap=int(input("Enter new capacity: "))
        status=modifycoursecapacity(cname,ccap)
        if status==1:
            print("found and modification done")
        elif status==2:
            print("found and not modified")
        else:
            print("not found")

    elif choice==4:
        oldcourse=input("enter old course name: ")
        newcourse=input("enter new course name: ")
        status=modifybycourseName(oldcourse,newcourse)
        if status==1:
            print("found and modification done")
        elif status==2:
            print("found and not modified")
        else:
            print("not found")

    elif choice==5:
        display()

    elif choice==6:
        givencapacity()

    elif choice==7:
        print("THANK YOU!!!")
        sys.exit(0)