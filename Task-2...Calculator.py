print("Simple Calculator")
print("Select an Operation")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

while True:
    operation=int(input("Enter choice(1/2/3/4)>> "))
    num1=float(input("Enter num1>> "))
    num2=float(input("Enter num2>> "))
    if operation==1:
        print(num1+num2)
    elif operation==2:
        print(num1-num2)
    elif operation==3:
        print(num1*num2)
    elif operation==4:
        print(num1/num2)
    else:
        print("Invalid option! Please Try Again")