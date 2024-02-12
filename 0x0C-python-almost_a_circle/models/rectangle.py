#!/usr/bin/python3
"""this defines a class named rectangle"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle implements Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validator(self, name, value):
        """validates the value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0 and (name == "width" or name == "height"):
            raise ValueError(f"{name} must be > 0")
        if value < 0 and (name == "x" or name == "y"):
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """adding width the getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        self.validator("width", width)
        self.__width = width

    @property
    def height(self):
        """getter for the height"""
        return self.__height

    @height.setter
    def height(self, height):
        self.validator("height", height)
        self.__height = height

    @property
    def x(self):
        "getter for x"
        return self.__x

    @x.setter
    def x(self, x):
        self.validator("x", x)
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        self.validator("y", y)
        self.__y = y

    def area(self):
        """returns the area value"""
        return self.__width * self.__height

    def display(self):
        """dispaly the rectangle in stdout"""
        if self.__y != 0:
            print("\n" * self.__y, end="")
        for height in range(0, self.__height):
            print(" " * self.__x, end="")
            for width in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """returns  task 6"""
        return (
            f"[{type(self).__name__}] ({self.id}) {self.__x}/{self.__y}"
            f" - {self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """adding the new values to variables"""
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """returns dicitionary represention"""
        return {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width,
        }
