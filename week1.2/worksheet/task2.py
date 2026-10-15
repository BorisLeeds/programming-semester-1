# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
list1 = read_numbers()
list1.sort()
if len(list1)==0:
    print("Error: no numbers provided", file = sys.stderr)
else:
    try:
        print(f"Minimum = {min(list1)}")
        print(f"Maximum = {max(list1)}")
        print(f"Mean = {sum(list1)/len(list1)}")
        try:
            middle= (len(list1)-1)/2
        except:
            middle=0
        
        if len(list1)%2 != 0:
            mid = list1[int(middle)]
        else:
            x = int(middle)
            y= x+1
            print(x,y)
            mid = (list1[x] + list1[y]) / 2
        print(f"Median = {mid}")
    except:
        print("Error: no numbers provided")
