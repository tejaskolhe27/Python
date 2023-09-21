
list1=[]
class student():
    count=0
    def __init__(self,studid=0,name="",marks1="",marks2="",marks3="",gpa=0):
        
        self.__studid=studid
        self.__name=name
        self.__marks1=marks1
        self.__marks2=marks2
        self.__marks3=marks3
        self.__gpa=student.calculateGPA()
    @staticmethod
    def calculateGPA():
        gpa=(1/3)*int(m1)+(1/2)*int(m2)+(1/4)*int(m3)
        return gpa
    

    #getter
    def get_studid(self):
        return self.__studid
    def get_name(self):
        return self.__name
    def get_marks1(self):
        return self.__marks1
    def get_marks2(self):
        return self.__marks2
    def get_marks3(self):
        return self.__marks3
    
    #setter
    def set_studid(self,studid):
        self.__studid=studid
    def set_name(self,name):
        self.__name=name
    def set_marks1(self,marks1):
        self.__marks1=marks1
    def set_marks2(self,marks2):
        self.__marks2=marks2
    def set_marks3(self,marks3):
        self.__marks3=marks3
    
    def __str__(self):
       return f"Student Details: \n -----------\n Student ID: {self.__studid}\n Name: {self.__name}\n M1: {self.__marks1}\n M2: {self.__marks2}\n M3: {self.__marks3}\n GPA:{self.__gpa} "
        

lst=[]
for i in range(2):
        id=int(input("Enter the student id: "))
        name=input("Enter the name: ")
        m1=input("Enter marks1: ")
        m2=input("Enter marks2: ")
        m3=input("Enter marks3: ")
        
        s=student(id,name,m1,m2,m3)
        print(s)
        lst.extend((id,name,m1,m2,m3))
print(lst)

choice=0
while choice!=5:
    choice = int(input("""
    1. Display All Student
    2. Search by id
    3. Search by name
    4. calculate GPA of a student
    5. Exit
    choice:"""))
    match choice:
        case 1:
            print("All students are: ")
            for i in lst:
                print(i)
        
        case 2:
            pass
        case 4:
            student.calculateGPA()