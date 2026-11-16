import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
num = int(input("how many names do u want"))
lis =random.sample(names, num)
# Display the chosen names, one per line
for elem in lis:
    print(elem)