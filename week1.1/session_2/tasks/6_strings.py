# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") #the original string
print(f"Modified String 1: {user_string.lower()}")#makes it lower case
print(f"Modified String 2: {user_string.upper()}")#makes it upper case
print(f"Modified String 3: {user_string.strip()}")#removes whitespaces on edges
print(f"Modified String 4: {user_string.replace('a', '@')}")#replaces the letter a with @
print(f"Modified String 5: {user_string.capitalize()}")#makes the first character uppercase
print(f"Modified String 6: {user_string[::-1]}")#reverses the string
print(f"Modified String 7: {user_string.title()}")#makes the first letter in every word upper case
print(f"Modified String 8: {len(user_string)}")#prints length of string
print(f"Modified String 9: {user_string.find('a')}")#finds every location of the letter a
print(f"Modified String 10: {user_string.count('a')}")#prints number of a's
print(f"Modified String 11: {user_string.startswith('Hello')}")# checks if it starts with Hello
print(f"Modified String 12: {user_string.endswith('!')}")# checks if it ends with !
print(f"Modified String 13: {user_string.isalnum()}")# checks if is a number or letter
print(f"Modified String 14: {user_string.isalpha()}")#checks if all characters are in the al
print(f"Modified String 15: {user_string.isdigit()}")#checks if is a number



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!