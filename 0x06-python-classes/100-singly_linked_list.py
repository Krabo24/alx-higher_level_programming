#!/usr/bin/python3

"""define classes for singly-linked list"""

class Node:
    """represent node in singly-linked list"""

    def __init__(self, data, next_node=None):
        """initialize new Node

        Args:
            data (int): data of new Node
            next_node (Node): next node of new Node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get/set data of the Node"""
        return (self.__data)

    @data.setter
    def data(self, value):

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get or set next_node of Node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """represent singly-linked list"""

    def __init__(self):
        """initalize new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """insert new Node to SinglyLinkedList

        node is inserted into list at the correct ordered
        numerical position

        Args:
            value (Node): new Node to be inserted
        """

        new = Node(value)
        if self.__head is None:

            new.next_node = None
            self.__head = new

        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """define the print() representation of SinglyLinkedList"""
        values = []
        tmp = self__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
