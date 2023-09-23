#!/usr/bin/python3

"""Define text file insertion function"""

def append_after(filename="", search_string="", new_string=""):
    """Insert the text after each line containing the given string in a file

    Args:
        filename (str): Name of file
        search_string (str): String to search for within file
        new_string (str): String to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
