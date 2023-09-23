class A:
    def __init__(self,a1=0,a2=0):
        print("In A constructor: ",a1,a2)
        self.__a1=a1
        self.__a2=a2
    def __str__(self):
        return f"A1: {self.__a1} A2: {self.__a2}\n"
    
class B(A):
    def __init__(self,b1=0,**kwarg):
        print("In B constructor: ",b1,kwarg)
        super().__init__(**kwarg)
        self.__b1=b1
    def __str__(self):
        return super().__str__()+ f"B1: {self.__b1}\n"
    
class C(A):
    def __init__(self,c1=0,c2=0,**kwarg):
        print("In C constructor: ",c1,c2,kwarg)
        super().__init__(**kwarg)        
        self.__c1=c1
        self.__c2=c2
    def __str__(self):
        return super().__str__()+f"C1: {self.__c1} C2: {self.__c2}\n"
    
class D(C,B):
    def __init__(self,d1=0,d2=0,**kwarg):
        print("In D constructor: ",d1,d2,kwarg)
        super().__init__(**kwarg)
        self.__d1=d1
        self.__d2=d2
    def __str__(self):
        return super().__str__()+ f"D1: {self.__d1} D2: {self.__d2}\n"

obj=D(a1=10,a2=11,b1=12,c1=13,c2=14,d1=15,d2=16)
print(obj)
print(D.mro()) #Method Resolution Operator
