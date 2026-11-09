# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self,n,b):
        '''initalises the class'''
        if not isinstance(n, str):
            raise TypeError("name should be a string")
        if n == "":
            raise ValueError("name shouldnt be empty")
        if not isinstance(b,date):
            raise TypeError("birth should be a date")
        self.name=n
        self.birth=b

    def initials(self):
        '''returns the users initals'''
        parts = self.name.split()
        init = [part[0].upper() for part in parts]
        return "".join(init)

    def is_birthday(self):
        ''' Checks if it is the person's birthday today'''
        today = date.today()
        return (today.month == self.birth.month and today.day == self.birth.day)
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
