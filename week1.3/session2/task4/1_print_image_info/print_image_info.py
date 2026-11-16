# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)
def read_pgm_info(filepath: str) -> None:
    """Open PGM image and print its dimensions and max gray value"""
    with open(filepath, "r", encoding="utf-8") as infile:
        lines = [
            line.strip()
            for line in infile
            if line.strip() and not line.strip().startswith("#")
        ]

    if len(lines) < 3 or lines[0] != "P2":
        print(f"Error: '{filepath}' is not a valid PGM file.")
        return

    width, height = lines[1].split()
    max_gray_value = lines[2]

    print(f"Dimensions: {width} x {height} pixels")
    print(f"Max Gray Value: {max_gray_value}")