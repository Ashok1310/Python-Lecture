def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def calc(a,b,op):
    if op=="+":
       return add(a,b)
    elif op=="-":
       return sub(a,b)
    elif op=="*":
       return mul(a,b)
    elif op=="/":
       return div(a,b)
    else:
        print("Invalid Operation")

a=float(input("Enter 1st value:"))
b=float(input("Enter 1st value:"))
op=input("Enter operation (+,-,*,/):")
print("Answer",calc(a,b,op))