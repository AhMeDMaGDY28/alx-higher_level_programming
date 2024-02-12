#!/usr/bin/python3
"""this defines square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this is square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize the Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        "getter for the size"""
        return self.width

    @size.setter
    def size(self, size):
        """setter for the size"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """func for update the variables"""
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        return (
                f"[{type(self).__name__}] ({self.id})"
                f"{self.x}/{self.y} - {self.size}"
                )

    def to_dictionary(self):
        """an dictionary representing of a square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

