#!/usr/bin/python3
"""Defines class and inherited class-checking function"""

def is_kind_of_class(obj, a_class):
    """Checks if object is instance or inherited instance of a class

    Args:
        obj (any): The object to check
        a_class (type): class to match the type of obj to
    Returns:
        If obj is an instance or inherited instance of a_class - True
        Otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
