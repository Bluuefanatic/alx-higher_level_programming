#!/usr/bin/python3

class Square:
    """
    This is the Square class.

    Attributes:
        __size (float or int): Private instance attribute representing the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (float or int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Parameters:
            value (float or int): The size to set.

        Raises:
            TypeError: If the size is not a number (float or integer).
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison for Square instances based on area.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area() if isinstance(other, Square) else False

    def __ne__(self, other):
        """
        Inequality comparison for Square instances based on area.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area() if isinstance(other, Square) else True

    def __gt__(self, other):
        """
        Greater than comparison for Square instances based on area.

        Returns:
            bool: True if area is greater, False otherwise.
        """
        return self.area() > other.area() if isinstance(other, Square) else False

    def __ge__(self, other):
        """
        Greater than or equal to comparison for Square instances based on area.

        Returns:
            bool: True if area is greater or equal, False otherwise.
        """
        return self.area() >= other.area() if isinstance(other, Square) else False

    def __lt__(self, other):
        """
        Less than comparison for Square instances based on area.

        Returns:
            bool: True if area is less, False otherwise.
        """
        return self.area() < other.area() if isinstance(other, Square) else False

    def __le__(self, other):
        """
        Less than or equal to comparison for Square instances based on area.

        Returns:
            bool: True if area is less or equal, False otherwise.
        """
        return self.area() <= other.area() if isinstance(other, Square) else False
