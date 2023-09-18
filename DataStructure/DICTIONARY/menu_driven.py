course = {"DBDA":(100,60),"DAI":(100,40)}
def addnewcouserse():
     cname=input("Enter the couse Name: ")
     duration=int(input("Enter the duration: "))
     capacity=int(input("Enter the capacity: "))
     value = course.get(cname,-1)
     if value==-1:
         course[cname]=(duration,capacity)
         return True
     else:
         return False

def displayall(d=course):
    for k,v in d.items():
        print(k,"------>",v)
        
def displaybycapacity(capacity):
    d={}
    for k,v in course.items():
        if v[1]>capacity:
          d[k]=v
    if len(d)!=0:
        return d
    return None

def coursedelete():
    k=input("Enter the couse to delete: ")
    if k in course.keys():
        course.pop(k)
        print("Couse successfully deleted!!")
    else:
        print("Invalid course entered")


def modifycoursecapacity():
    k=input("Enter the couse to modify: ")
    capa=int(input(f"Enter the new capacity of {k}: "))
    for k,v in course.items():
        if k in course.keys():
            course[k]=(v[0],capa)
            print("Successfully updated")
        else:
            print("Wrong course entered")
    
   
        

def modifycoursename():
    k=input("Enter the course to modify its name: ")
    new=input(f"Enter the new name for {k} : ")
    if k in course.keys():
        course[new]= course.pop(k,-1)
        print("Successfully updated")
    else:
        print("Wrong course name entered")
        



choice= 0

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
    
        
    match choice:
        case 1:
            status= addnewcouserse()
            if status:
                print("course added")
            else:
                print("course not added")
        case 2:
            coursedelete()
        case 3:
            modifycoursecapacity()
        case 4:
            modifycoursename()
        case 5:
            displayall()
        case 6:
            capacity=int(input("Enter capacity: "))
            data=displaybycapacity(capacity)
            if data!=None:
                displayall(data)
            else:
                print("No course found")
        case 7:
            print("Thanks to visiting")   
