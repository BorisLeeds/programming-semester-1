# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.

# Open a file called 'user_info.txt' for reading

# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'

with open("user_info.txt", "a") as outfile:
    while True:
        name = input("Enter your name: ").strip()
        age = input("Enter your age: ").strip()
        colour = input("Enter your favourite colour: ").strip()

        outfile.write(f"Name: {name}\n")
        outfile.write(f"Age: {age}\n")
        outfile.write(f"Favourite colour: {colour}\n")
        outfile.write("\n")

        again = input("Add another person? (y/n): ").strip().lower()
        if again != "y":
            break

print("User information saved to user_info.txt.")
