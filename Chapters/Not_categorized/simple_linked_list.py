class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self._count = 0

        for item in values:
            self.push(item)

    def __len__(self):
        return self._count

    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")

        return self._head

    def push(self, value):
        self._head = Node(value, self._head)
        self._count += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        value = self._head.value()
        self._head = self._head.next()
        self._count -= 1

        return value

    def reversed(self):
        return LinkedList(self)

    def __iter__(self):
        node = self._head
        while node is not None:
            yield node.value()
            node = node.next()


class EmptyListException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

'''
Introduction
You work for a music streaming company.

You've been tasked with creating a playlist feature for your music player application.

Instructions
Write a prototype of the music player application.

For the prototype, each song will simply be represented by a number. Given a range of numbers (the song IDs), create a singly linked list.

Given a singly linked list, you should be able to reverse the list to play the songs in the opposite order.
'''
#No link to text cases available
