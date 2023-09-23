#!/usr/bin/python3
"""Define file-appending function"""

def append_write(filename="", text=""):
    """Appends the string to end of UTF8 text file

    Args:
        filename (str): Name of file to append to
        text (str): String to append to file
    Returns:
        Number of characters being appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
