class A:
    def __init__(self,a1=0,a2=0):
        print("In A constructor: ",a1,a2)
        self.__a1=a1
        self.__a2=a2
    def __str__(self):
        return f"A1: {self.__a1} A2: {self.__a2}\n"
    
class B(A):
    def __init__(self,a1=0,a2=0,b1=0):
        print("In B constructor: ",b1)
        A.__init__(self,a1,a2)
        self.__b1=b1
    def __str__(self):
        return A.__str__(self)+ f"B1: {self.__b1}\n"
    
class C(A):
    def __init__(self,a1=0,a2=0,c1=0,c2=0):
        print("In C constructor: ",c1,c2)
        A.__init__(self,a1,a2)
        self.__c1=c1
        self.__c2=c2
    def __str__(self):
        return A.__str__(self)+ f"C1: {self.__c1} C2: {self.__c2}\n"
    
class D(B,C):
    def __init__(self,a1=0,a2=0,b1=0,c1=0,c2=0,d1=0,d2=0):
        print("In D constructor: ",d1,d2)
        B.__init__(self,a1,a2,b1)
        C.__init__( self,a1,a2,c1,c2)
        self.__d1=d1
        self.__d2=d2
    def __str__(self):
        return B.__str__(self)+C.__str__(self)+ f"D1: {self.__d1} D2: {self.__d2}\n"

obj=D(10,11,12,13,14,15,16)
print(obj)