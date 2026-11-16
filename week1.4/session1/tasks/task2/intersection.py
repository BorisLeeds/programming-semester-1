set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7}
set_c = [3, 4, 5, 8]

print("Intersection of A and B:", set_a.intersection(set_b))
print("Intersection of A, B, and C:", set_a.intersection(set_b, set_c))
print("Type of output:", type(set_a.intersection(set_b)))