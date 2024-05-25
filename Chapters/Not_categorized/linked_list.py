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