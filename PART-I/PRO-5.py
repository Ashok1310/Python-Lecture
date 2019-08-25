a=float(input("Enter value of A:"))
b=float(input("Enter value of B:"))
c=float(input("Enter value of C:"))

if a>b:
    if a>c:
        print("MAX A",a)
        if b>c:
            print("MIN C",c)
        else:
            print("MIN B",b)
    else:
        print("MAX C",c)
        if a>b:
            print("MIN B",b)
        else:
            print("MIN A",a)
else:
    if b>c:
        print("MAX B",b)
        if a>c:
            print("MIN C",c)
        else:
            print("MIN A",a)
    else:
        print("MAX C",c)
        if a>b:
            print("MIN B",b)
        else:
            print("MIN A",a)
            

        
    
