import sys
import re
class Friend:
    cnt=0
    def __init__(self,fname="",lastname="",hobbies="",mobno="",email="",bdate="",address="" ):
        Friend.cnt=Friend.cnt+1
        self.__fid=Friend.cnt
        self.__fname=fname
        self.__lname=lastname
        self.__hobbies=hobbies
        self.__mobno=mobno
        self.__email=email
        self.__bdate=bdate
        self.__address=address
        
    def __str__(self):
        return f"fid:{self.__fid} Fname:{self.__fname} lastname={self.__lname} hobbies:{self.__hobbies} Mobile NO:{self.__mobno} email:{self.__email} bdate:{self.__bdate} address:{self.__address}"
    #setter methods
    def set_fname(self,fname):
        self.__fname=fname
    def set_lastname(self,lastname):
        self.__lastname=lastname
    def set_hobbies(self,hobbies):
        self.__hobbies=hobbies
    def set_mobno(self,mobno):
        self.__mobno=mobno
    def set_email(self,email):
        self.__email=email
    def set_bdate(self,bdate):
        self.__bdate=bdate
    def set_address(self,address):
        self.__address=address
    #Getter Methods
    def get_id(self):
        return self.__fid
    def get_fname(self):
        return self.__fname
    def get_lastname(self):
        return self.__lastname
    def get_hobbies(self):
        return self.__hobbies
    def get_mobno(self):
        return self.__mobno
    def get_email(self):
        return self.__email
    def get_bdate(self):
        return self.__bdate
    def get_address(self):
        return self.__address
    
lst=[]
n=int(input("Enter No of students: "))
for i in range(n):
    obj="s"+str(i+1)
    obj=Friend()
    obj.set_fname(input("Enter First Name:"))
    obj.set_lastname(input("Enter last name: "))
    obj.set_hobbies(input("Enter hobbies: "))
    obj.set_mobno(int(input("Enter mobile number: ")))
    obj.set_email(input("Enter email address: "))
    obj.set_bdate(input("Enter date of birth: "))
    obj.set_address(input("Enter address: "))
    lst.append(obj)

def searchbyid(n):
    for s in lst:
        if i==s.get_id():
            return s
            break
    else:
        return -1

ch='y'
while ch=='y':
    choice=int(input("""
    1. Display All Friend
    2. Search by id
    3. Search by name
    4. Display all friend with a particular hobby
    5. Exit 
    Choice :"""))
    match choice:
        case 1:
            for s in lst:
                print(s)
        case 2:
            i=int(input("Enter Friend ID: "))
            f=searchbyid(i)
            if f!=-1:
                print(f)
            else:
                print("Friend not Found")
        case 3:
            i=input("Enter Friend's First Name: ")
            for s in lst:
                if i==s.get_fname():
                    print(s)
                    break
            else:
                print("Friend not Found")
        case 4:
            hob=input("Enter Hobby: ")
            for s in lst:
                m=re.search(hob, s.get_hobby())
                if m!=None:
                    print(s)
            
        case 5:
            sys.exit(0)
        case _:
            print("Wrong Choice")