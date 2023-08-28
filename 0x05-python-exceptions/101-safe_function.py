#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """executes function safely

    Args:
        fct: function to execute
        args: arguments for fct

    Returns:
        If error occurs - None
        Otherwise - result of call to fct
    """

    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
