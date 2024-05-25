class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.next = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.list = []
        self.i = 0
        self.found = False

    def push(self,station):
        self.list.append(station)
        if self.i == 0:
            node = Node(station,self.i+1,None)
            self.i += 1
        else:
            node = Node(station,self.i+1,self.i-1)
            self.i += 1

    def pop(self):
        if self.list == []:
            raise IndexError("List is empty")
        else:
            return self.list.pop(len(self.list)-1)

    def shift(self):
        return self.list.pop(0)
    def unshift(self,station):
        self.list = [station] + self.list

    def __len__(self):
        return len(self.list)

    def delete(self,station):
        for item in self.list:
            if item == station:
                self.list.remove(item)
                self.found = True

        if self.found == False:
            raise ValueError("Value not found")

'''
ntroduction
You are working on a project to develop a train scheduling system for a busy railway network.

You've been asked to develop a prototype for the train routes in the scheduling system. Each route consists of a sequence of train stations that a given train stops at.

Instructions
Your team has decided to use a doubly linked list to represent each train route in the schedule. Each station along the train's route will be represented by a node in 
the linked list.

You don't need to worry about arrival and departure times at the stations. Each station will simply be represented by a number.

Routes can be extended, adding stations to the beginning or end of a route. They can also be shortened by removing stations from the beginning or the end of a route.

Sometimes a station gets closed down, and in that case the station needs to be removed from the route, even if it is not at the beginning or end of the route.

The size of a route is measured not by how far the train travels, but by how many stations it stops at.


How this Exercise is Structured in Python
While linked lists can be implemented in a variety of ways with a variety of underlying data structures, we ask here that you implement your linked list in an OOP fashion.

In the stub file, you will see the start of a Node class, as well as a LinkedList class. Your Node class should keep track of its value, as well as which other nodes 
preceed or follow. Your push, pop, shift, unshift, and the special method for len should be implemented in the LinkedList class. 
You might also find it useful to implement a special iter method for iteration.

Unlike the core exercise, we will be testing error conditions by calling pop and shift on empty LinkedLists, so you will need to raise errors appropriately.

Finally, we would like you to implement delete in addition to the methods outlined above. delete will take one argument, 
which is the value to be removed from the linked list. If the value appears more than once, only the first occurrence should be removed.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/linked-list/canonical-data.json
