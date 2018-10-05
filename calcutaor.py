n=int(input("Enter the first number:"))
m=input("Enter the operator(+,-,/,*,%):")
o=int(input("Enter the second number:"))
add=n+o
subtract=n-o
multiply=n*o
divide=n/o
percentage=(n/o)*100
if m == '+':
    print(add)

elif m == '-':
    print(subtract)

elif m == '*':
    print(multiply)

elif m == '/':
    print(divide)

elif m == '%':
    print(percentage)

else:
    print("Invalid input !!!")
    

