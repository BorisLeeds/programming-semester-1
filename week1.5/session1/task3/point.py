# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
        """
        Creates a Point, given x and y coordinates.
        """
        self.x = x
        self.y = y
    # Add distance() method here
    def distance(self):
        """
        Returns the distance of this Point from the origin (0, 0).
        """
        return math.hypot(self.x, self.y)
    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, other):
        """
        Returns the distance from this Point to another Point.
        """
        return math.hypot(self.x - other.x, self.y - other.y)



# Finally, add code here to demonstrate use of Point
