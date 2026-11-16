import random

# Get user to input how many random numbers they want
num =int(input("how many numbers do u want"))
# Generate this many random numbers
randomnumbers = []
while num !=0:
    randomnumbers.append(random.randint(0,100))
    num-=1
# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as file1:
    for elem in randomnumbers:
        file1.write(f"{elem}\n")