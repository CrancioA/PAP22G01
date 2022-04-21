"""
Counted List

Create a class for a list like object based on UserList wrapper https://docs.python.org/3/library/collections.html#collections.UserList

That class should have a method to return a Counter that will count how many objects of each type are present in the list. This is actually done directly by counter class below https://docs.python.org/3/library/collections.html#collections.Counter

Counter should be updated automatically for at lest 2 list methods (append, pop), so when an object is removed from the list or added the counter object is updated.
"""
from collections import UserList
from collections import Counter


class Example(UserList):

    def __init__(self, my_list=None):
        UserList.__init__(self, my_list)
        self.data = []
        if my_list is not None:
            if isinstance(my_list, type(self.data)):
                self.data[:] = my_list
            elif isinstance(my_list, UserList):
                self.data[:] = my_list.data[:]
            else:
                self.data = list(my_list)

    def get_counter(self):
        return Counter(self.data)

    def append(self, item):
        self.data.append(item)

    def pop(self, i: str = ...):
        self.data.remove(i)


x = Example(['1', '2', '3'])
print(x.get_counter()) # returns Counter({'1':1, '2':1 '3':1})
x.append('3')
print(x.get_counter()) # returns Counter({'1':1, '2':1, '3':2})
x.pop('2')
print(x.get_counter())# returns Counter({'1':1, '3':2})