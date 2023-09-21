class ABCTel:
    cnt=0
    def __init__(self,ctype="",name="",email=""):
        ABCTel.cnt=ABCTel.cnt+1
        self.__cid=ctype+str(ABCTel.cnt)
        self.__ctype=ctype
        self.__name=name
        self.__email=email
        
    def __str__(self):
        return f"Type:{self.__ctype} ID:{self.__cid} Name:{self.__name} Email:{self.__email} "
    
    #Setter Methods
    def set_email(self,x):
        self.__email=x
    def set_name(self,x):
        self.__name=x
        
    #Getter Method
    def get_email(self):
        return self.__email
 
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__cid
    def get_type(self):
        return self.__ctype
    
    
class Vendor(ABCTel):
    def __init__(self,name="",email="",lst=[]):
        super().__init__("V",name,email)
        self.__plst=lst
        
    def __str__(self):
        return super().__str__()+f"Product List:{self.__plst} "
    
class Customer(ABCTel):
    def __init__(self,ctype="",name="",email="",crclass="",disc=0,plan=""):
        super().__init__(ctype,name,email)
        self.__crclass=crclass
        self.__disc=disc
        self.__plan=plan
        
    def __str__(self):
        return super().__str__()+f"Credit Class:{self.__crclass} Discount: {self.__disc} Plan: {self.__plan}"
    
class Company(Customer):
    def __init__(self,name="",email="",crclass="",disc=0,plan="",comptype="",rman="",crline=0,ext=[]):
        super().__init__("Comp",name,email,crclass,disc,plan)
        self.__comptype=comptype
        self.__rman=rman
        self.__crlineno=crline
        self.__extlst=ext
        
    def __str__(self):
        return super().__str__()+f"Company Type: {self.__comptype} Relational Manager: {self.__rman} Cr Line No: {self.__crlineno} Extension List: {self.__extlst}"

class Individual(Customer):
    def __init__(self,name="",email="",crclass="",disc=0,plan="",phno=""):
        super().__init__("I",name,email,crclass,disc,plan)
        self.__phno=phno
        
    def __str__(self):
        return super().__str__()+f"Phone No: {self.__phno}"
    
i=Individual("Prada","prada@gmail.com","Regular",20,"Gold","899898")
print(f"Individual Customer: \n{i}\n")
c=Company("Dell","admin@dell.com","Premium",0.2,"Diamond","IT Service","Pradhyumn",121,[1001,1002,1003,1004,1005])
print(f"Company Customer: \n{c}\n")   
v=Vendor("XYZ","admin@xyz.com",['Prod1','Prod2','Prod3','Prod4'])
print(f"Vendor: \n{v}\n")