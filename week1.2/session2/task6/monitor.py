# Week 1.2, Session 2: Task 6
temp = int(input("Enter the machine's temperature in degrees Celsius "))
Pressure =int(input("Enter The machine's pressure in PSI "))
status = int(input("Enter The machine's operational status (1 for operating, 0 for stopped )"))

if temp > 80:
  print("temps too high, recommeded machine shut down")
elif temp >=50:
  print("temps in safe limits")
else:
  print("temps low no action needed")

