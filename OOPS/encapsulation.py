class student:
    count=0
    #constructor
    def __init__(self,pid=0,pname="",mob=""):
        student.count=student.count+1
        self.__pid=student.count
        self.__pname=pname
        self.__mob=mob
    
    #Decorator
    @staticmethod             
    def function1(val):
        print("in my function1",val,student.count)
        
    #setter methods
    def set_pid(self,pid):
        self.__pid=pid
        
    def set_pname(self,pname):
        self.__pname=pname
        
    def set_mobile(self,mob):
        self.__mob=mob
        
    #getter methods
    def get_pid(self):
        return self.__pid
    
    def get_pname(self):
        return self.__pname
    
    def get_mobile(self):
        return self.__mob
        
    #str method
    def __str__(self):
        return f"Pid:{self.__pid}, PName:{self.__pname}, Mobile:{self.__mob}"


p1= student(1,"atharva","1234")
p2= student(2,"tejas","1234")
#to print all the data
print(p1)
print(p2)

print(p1.get_pname())
p1.set_mobile("2345")
print(p1)

student.function1(4)