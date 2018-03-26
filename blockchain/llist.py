#!/usr/bin/env pythonw

import sys
import gzip

class Node(object):
    def __init__(self, data, prev=None):
        self.prev = prev
        self.data = data

    def __repr__(self):
        return "Node(%s, %s)" % (self.data, hex(id(self.prev)))

    def __str__(self):
        return self.__repr__()

class List(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item, self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.prev

        return count

my_list = List()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.add(5)
my_list.add(6)