"""This module provides basic calculator functions."""


def sum(x, y):
    """Calculates the sum of two numbers.

    Args:
        x (int or float): The first number.
        y (int or float): The second number.

    Returns:
        int or float: The sum of x and y.
    """
    return x + y


def average(x, y):
    """Calculates the average of two numbers.

    Args:
        x (int or float): The first number.
        y (int or float): The second number.

    Returns:
        float: The average of x and y.
    """
    return (x + y) / 2


def power(x, y):
    """Raises a number to a power.

    Args:
        x (int or float): The base number.
        y (int or float): The exponent.

    Returns:
        int or float: The result of x raised to the power of y.
    """
    return x ** y
