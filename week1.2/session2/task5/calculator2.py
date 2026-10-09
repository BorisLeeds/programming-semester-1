# Week 1.2, Session 2: Task 5
# Calculator
num1="" 
num2=""
x = input("Enter a calculation: ")
x.replace(" ","")
switch=False
for char in x:
    if char.isdecimal() and switch == False:
        num1 +=char
    elif char.isdecimal() and switch == True:
        num2+=char
    else:
        switch=True
        operation =char
num1=int(num1)
num2=int(num2)
if operation == "+":
    result = num1 + num2
    print(f"The result is: {result}")
elif operation =="-":
    result = num1 - num2
    print(f"The result is: {result}")
elif operation =="*":
    result = num1 * num2
    print(f"The result is: {result}")
elif operation =="/":
    if num2 == 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Cannot divide by zero.")
