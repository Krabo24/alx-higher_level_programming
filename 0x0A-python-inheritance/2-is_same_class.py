#!/usr/bin/python3
"""Defines class-checking function"""
def is_same_class(obj, a_class):
    """Checks if object is exactly an instance of the given class

    Args:
        obj (any): object to check
        a_class (type): class to match type of obj to
    Returns:
        If obj is exactly a instance of a_class - True
        Otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
