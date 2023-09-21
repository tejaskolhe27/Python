class Person:
    count=0
    #constructor
    def __init__(self,etype="",name="",mob=""):
        Person.count=Person.count+1
        self.__pid=etype+str(Person.count)
        self.__name=name
        self.__mob=mob

    #setter methods
    def set_pid(self,pid):
        self.__pid=pid
        
    def set_name(self,name):
        self.__name=name
        
    def set_mobile(self,mob):
        self.__mob=mob
        
    #getter methods
    def get_pid(self):
        return self.__pid
    
    def get_name(self):
        return self.__name
    
    def get_mobile(self):
        return self.__mob
        
    #str method
    def __str__(self):
        return f"Pid:{self.__pid}, Name:{self.__name}, Mobile:{self.__mob}"


class Employee(Person):
    def __init__(self, etype="",name="",mob="",dept="",desg=""):
        super().__init__(etype,name,mob)
        self.__dept=dept
        self.__desg=desg
         
    def set_dept(self,dept):
        self.__dept=dept
    def set_desg(self,desg):
        self.desg=desg
        
    def get_dept(self):
        return self.__dept
    def get_desg(self):
        return self.__desg
    
    def __str__(self):
        return super().__str__()+ f" dept: {self.__dept}, desg: {self.__desg}"
    
class SalariedEmp(Employee):
    def __init__(self,name="",mob="",dept="",desg="",sal=1000):
        super().__init__("S",name,mob,dept,desg)
        self.__sal=sal
        self.__bonus=0.10*sal
        
    def set_sal(self,sal):
        self.__sal=sal
    def set_bonus(self,bonus):
        self.__bonus=bonus
        
    def get_sal(self):
        return self.__sal
    def get_bonus(self):
        return self.__bonus
    
    def __str__(self):
        return super().__str__()+ f" Sal: {self.__sal}, Bonus: {self.__bonus}"
    
    
class ContractEmp(Employee):
    def __init__(self,name="",mob="",dept="",desg="",charges=1000,hrs=0):
        super().__init__("C",name,mob,dept,desg)
        self.__hrs=hrs
        self.__charges=charges
        
    def set_hrs(self,hrs):
        self.__hrs=hrs
    def set_charges(self,charges):
        self.__charges=charges
        
    def get_hrs(self):
        return self.__hrs
    def get_charges(self):
        return self.__charges
    
    def __str__(self):
        return super().__str__()+ f" Charges: {self.__charges}, Hours: {self.__hrs}"
    
if __name__=="__main__":
    s=SalariedEmp("Atharva","1111","AI","Mgr",100000)
    c=ContractEmp("Tejas","2222","AI","Mgr",5000,5)
    c.set_charges(2000)
    print(s)
    print(c)