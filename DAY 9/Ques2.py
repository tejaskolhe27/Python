import sys
class Student:
    cnt=0
    def __init__(self,sname="",m1=0,m2=0,m3=0):
        Student.cnt=Student.cnt+1
        self.__sid=Student.cnt
        self.__sname=sname
        self.__m1=m1
        self.__m2=m2
        self.__m3=m3
       
        
    def __str__(self):
        return f"ID: {self.__sid}, Name: {self.__sname}, M1: {self.__m1}, M2: {self.__m2}, M3: {self.__m3}"
    
    def calgpa(self):
        return (1/3)*self.__m1+(1/2)*self.__m2+(1/4)*self.__m3
    
    #Setter methods
    def set_sid(self,x):
        self.__sid=x
    def set_sname(self,x):
        self.__sname=x
    def set_m1(self,x):
        self.__m1=x
    def set_m2(self,x):
        self.__m2=x
    def set_m3(self,x):
        self.__m3=x
        
    #getter methods
    def get_m1(self,x):
        self.__m1=x
    def get_m2(self,x):
        self.__m2=x
    def get_m3(self,x):
        self.__m3=x
    def get_id(self):
        return self.__sid
    def get_name(self):
        return self.__sname

lst=[]
n=int(input("Enter No of students: "))
for i in range(n):
    obj=str(i+1)
    obj=Student()
    obj.set_sname(input("Enter a Name:"))
    obj.set_m1(int(input("Enter a Marks1:")))
    obj.set_m2(int(input("Enter a Marks2:")))
    obj.set_m3(int(input("Enter a Marks3:")))
    lst.append(obj)

def searchbyid(n):
    for s in lst:
        if i==s.get_id():
            return s
    else:
        return -1

ch='y'
while ch=='y':
    choice=int(input("""
    1. Display All Student
    2. Search by id
    3. Search by name
    4. calculate GPA of a student
    5. Exit 
    Choice :"""))
    match choice:
        case 1:
            for s in lst:
                print(s)
        case 2:
            i=int(input("Enter Student ID: "))
            stud=searchbyid(i)
            if stud!=-1:
                print(stud)
            else:
                print("Student not Found")
        case 3:
            i=input("Enter Student name: ")
            for s in lst:
                if i==s.get_name():
                    print(s)
                    break
            else:
                print("Student not Found")
        case 4:
            i=int(input("Enter Student ID: "))
            stud=searchbyid(i)
            if stud!=-1:
                print(f"gpa of student {stud.get_id()} :{stud.calgpa()}")
            else:
                print("Student not Found")
        case 5:
            sys.exit(0)
        case _:
            print("Wrong Choice")
        
        
        
        
        
        
        
        
        
