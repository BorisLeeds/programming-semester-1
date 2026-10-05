# Worksheet 1.2: Task 2 Solution
from util import read_numbers
list1 = read_numbers()
list1.sort()
print(f"minimum = {min(list1)}")
print(f"maximum = {max(list1)}")
print(f"mean = {sum(list1)/len(list1)}")
try:
    middle= (len(list1)-1)/2
except:
    middle=0

if len(list1)%2 != 0:
    mid = list1[middle]
else:
    x = int(middle)
    y= x+1
    mid = (list1[x] + list1[y]) / 2
print(f"median = {mid}")
