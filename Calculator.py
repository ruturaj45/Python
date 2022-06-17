from calendar import c
from ctypes.wintypes import FLOAT
from http.client import SWITCHING_PROTOCOLS

a = input("Enter The value of A : ")
op = input("Enter the operator ( + , - , * , / , % ) : ")
b = input("Enter The value of B : ")

if(op == '+'):
    c = int(a)+int (b)
    print(a+" + "+b+" = "+str(c))
elif(op == '-'):
    c = int(a)-int(b)
    print(a+" - "+b+" = "+str(c))
elif(op == '*'):
    c = int(a)*int(b)
    print(a+" * "+b+" = "+str(c))


elif(op == '%'):
    c = float(a) % float(b)
    print(a+" % "+b+" = "+str(c))
elif (op == '/') :
    
        if(b == '0'):
        
            print("Cannot devide by zero.")
        
        else:
        
            c = float(a) / float(b)
            print(a+" / "+b+" = "+str(c))
        

    
else:
    print("Invalid!!! Wrong operator !!!")
