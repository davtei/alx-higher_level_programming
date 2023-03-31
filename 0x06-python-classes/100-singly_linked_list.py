#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """Class for a node in a singly-linked list."""
    def __init__(self, data, next_node=None):
        """Initialize the class, Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the value of the data of the new Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of the private instance, __data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the value of the next node of the linked_list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the value of the private instance, __next_node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly-linked list."""
    def __init__(self):
        """Initialize the SinglyLinkedList class."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList at the
        exact ordered numerical position.
        Args:
            value (int): The new integer to be inserted."""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Define the print() representation of SinglyLinkedList"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
