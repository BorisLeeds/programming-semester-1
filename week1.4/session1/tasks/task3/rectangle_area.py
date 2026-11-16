
# function implementation

def rectangle_area(width, height):  # define suitable input data
    # ...               # implement the function
    return width * height        # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(5,3)}")   # provide suitable data matching your inputs

def mean_average(numbers):
    """Return the arithmetic mean of a list of integers, or None if empty."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


print(mean_average([10, 20, 30, 40]))
print(mean_average([1, 2, 3]))
print(mean_average([]))
