class student():
    count=0
    def __init__(self,studid=0,name="",marks1="",marks2="",marks3=""):
        student.count=student.count+1
        self.__studid=student.count
        self.__name=name
        self.__marks1=marks1
        self.__marks2=marks2
        self.__marks3=marks3

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
        return f"Student Details: \n -----------\n Student ID: {self.__studid}\n Name: {self.__name}\n M1: {self.__marks1}\n M2: {self.__marks2}\n M3: {self.__marks3} "





for i in range(2):   
    name=input("Enter the name:  ")
    m1=input("Enter marks1: ")
    m2=input("Enter marks2: ")
    m3=input("Enter marks3: ")

    s=student(id,name,m1,m2,m3)
    print(s)