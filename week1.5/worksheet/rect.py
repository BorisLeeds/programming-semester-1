# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Width should be an int")
        if width <= 0 or height <=0:
            raise ValueError("Width must be bigger than 0")
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    def is_square(self):
        '''checks if the rectange is a square'''
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        '''returns area of rectange'''
        return (self.width * self.height)

    def perimeter(self):
        '''returns perimeter of rectange'''
        return ((2*self.width)+(2*self.height))

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
