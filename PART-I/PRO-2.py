a=float(input("Enter value of A:"))
b=float(input("Enter value of B:"))

#METHOD 1
a=a+b
b=a-b
a=a-b
print("METHOD 1")
print(f"A:{a}")
print(f"B:{b}")


#METHOD 2
a=a*b
b=a/b
a=a/b
print("METHOD 2")
print(f"A:{a}")
print(f"B:{b}")

#METHOD 3 work only with int value
a=int(a)
b=int(b)
a=a^b
b=a^b
a=a^b
print("METHOD 3")
print(f"A:{a}")
print(f"B:{b}")


#METHOD 4 
a,b=b,a
print("METHOD 4")
print(f"A:{a}")
print(f"B:{b}")
