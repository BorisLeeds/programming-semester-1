# Worksheet 1.2: Task 1 Solution
import sys
try:
    score = int(input("Enter a score from 1-100 "))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")
if score < 0 or score > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")
elif score < 40:
    print(f"{score} is a fail")
elif score < 70:
    print(f"{score} is a Pass")
else:
    print(f"{score} is a Distinction")