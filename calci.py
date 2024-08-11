print("------------------------Calculator-------------------------")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder")

ch = int(input("Enter the choice: "))
if ch==1:
         c= a+b
         print(c)
elif ch==2:
         d= a-b
         print(d)
elif ch==3:
         e= a*b
         print(e)
elif ch==4:
         f= a/b
         print(f)
elif ch==5:
         g= a%b
         print(g)
         
else:
    print("Wrong Choice")







                  
