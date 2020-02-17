#!/usr/bin/env python3

"""
Doubly Linked List class
Sam Daitzman // DSA 2020
"""

import pytest
import timeit
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self,val=None,next=None,prev=None):
        ''' Constructor for a node '''
        self.val = val
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self):
        ''' Constructor for an empty list '''
        self.first = None
        self.last = None

    def length(self):
        ''' Returns the number of nodes in the list '''
        # TODO: work with empty DLL
        next = self.first.next
        nodes = 1
        while next:
            next = next.next
            nodes += 1
        return nodes
            

    def push(self, val):
        ''' Adds a node with value equal to val to the front of the list '''

        # declare a new node, linked to the first node
        new_node = Node(val=val, next=self.first)

        if self.first:
            self.first.prev = new_node
        else:
            self.last = new_node
        self.first = new_node


    def insert_after(self, prev_node, val):
        ''' Adds a node with value equal to val in the list after prev_node '''
        new_node = Node(val=val, prev=prev_node)

        if prev_node is self.last:
            print("We're at the last node, y'all!")
            self.last = new_node
            new_node.next = None # probably redundant, this kwarg is set by default to None
        else:
            new_node.next = prev_node.next
            prev_node.next.prev = new_node
        prev_node.next = new_node


    def delete(self, node):
        ''' Removes node from the list '''
        if node is not self.last:
            node.next.prev = node.prev
        else:
            self.last = node.prev
            node.prev.next = None

        if node is not self.first:
            node.prev.next = node.next
        else:
            self.first = node.next
            node.next.prev = None


    def index(self, i):
        ''' Returns the node at position i (i<n) '''
        ''' Returns None for empty list '''
        ''' Returns a None node for out-of-bounds index '''
        next = self.first
        current = 0

        # for each node in the chain
        while next:
            # if it's the one we want, return it
            if current == i:
                return next
            # if it's not yet, keep going
            elif next.next:
                current += 1
                next = next.next
            # if we're at the end, return an unlinked node
            else:
                return Node(val=None,next=None,prev=None)
        

    def multiply_all_pairs(self):
        ''' Multiplies all unique pairs of nodes values for nodes i, j (i != j) 
        and returns the sum '''
        i = self.first
        j = self.first

        total = 0

        # O(n^2) is less than ideal, TODO: refactor this
        # maybe calculate as we go, or find a more intelligent recursion
        while i:
            while j:
                if i is not j:
                    total += i.val * j.val
                j = j.next
            i = i.next
            j = self.first
        return total/2





# ------- TESTS -------
def test_dll_exists():
    """ Checks that the DLL actually exists """
    assert DLL() is not None

def test_push():
    """ Checks that pushing onto DLL works correctly """
    dll = DLL()
    dll.push(2)
    dll.push(3)
    dll.push(4)
    assert dll.first.val == 4
    assert dll.first.next.val == 3
    assert dll.first.next.next.val == 2

def test_dll_ends():
    """ Checks that the DLL ends after its last node """
    dll = DLL()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    assert dll.first.next.next.next == None

def test_dll_direction():
    """ Checks that the DLL goes in the expected direction """
    dll = DLL()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    assert dll.first.prev == None
    assert dll.first.next.val == 2

def test_dll_length():
    """ Checks that an initialized DLL has a reasonable length """
    dll = DLL()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    assert dll.length() == 3

def test_index():
    """ Checks that indexing nodes return correct value """
    dll = DLL()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    assert dll.index(0).val == 3
    assert dll.index(1).val == 2
    assert dll.index(2).val == 1

def test_index_overflow():
    """ Checks that indexing beyond final node returns an unlinked None node """
    dll = DLL()
    dll.push(5)
    dll.push(7)
    dll.push(23)
    assert dll.index(3).val == None
    assert dll.index(3).next == None
    assert dll.index(3).prev == None

def test_deletion_first():
    """ Checks that deleting first element works """
    dll = DLL()
    dll.push(2)
    dll.push(3)
    dll.push(4)
    dll.delete(dll.index(0))
    assert dll.length() == 2
    assert dll.index(0).val == 3
    assert dll.index(1).val == 2
    assert dll.index(2).val == None

def test_deletion_middle():
    """ Checks that deleting middle element works """
    dll = DLL()
    dll.push(2)
    dll.push(3)
    dll.push(4)
    dll.delete(dll.index(1))
    assert dll.length() == 2
    assert dll.index(0).val == 4
    assert dll.index(1).val == 2
    assert dll.index(2).val == None

def test_deletion_middle():
    """ Checks that deleting last element works """
    dll = DLL()
    dll.push(2)
    dll.push(3)
    dll.push(4)
    dll.delete(dll.index(2))
    assert dll.length() == 2
    assert dll.index(0).val == 4
    assert dll.index(1).val == 3
    assert dll.index(2).val == None

def test_insertion_middle():
    """ Checks basic insertion """
    dll = DLL()
    dll.push(2)
    dll.push(3)
    dll.push(4)
    dll.insert_after(dll.index(1), 5)
    assert dll.last.prev.val == 5
    assert dll.length() == 4

def test_insertion_end():
    """ Checks basic insertion """
    dll = DLL()
    dll.push(2)
    dll.push(3)
    dll.push(4)
    dll.insert_after(dll.index(2), 5)
    assert dll.first.next.next.next.val == 5
    assert dll.index(3).val == 5
    assert dll.last.val == 5
    assert dll.length() == 4

def test_multiply():
    """ Checks multiplication works as expected across all pairs """
    dll = DLL()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    assert dll.multiply_all_pairs() == 11

def test_multiply_ones():
    """ Checks multiplication returns the expected value for a pair """
    dll = DLL()
    dll.push(1)
    dll.push(1)
    assert dll.multiply_all_pairs() == 1








# ------- TIMING -------
def index_dll_plot():
    """ Indexes my DLL and benchmarks at a variety of sizes """
    results = []
    max_n = 10000
    plot_range = range(1,max_n,100)
    # TODO: make this a concentric loop
    for list_size in plot_range:
        print("Currently {}% complete.".format(list_size/max_n*100))
        l = DLL()
        for i in range(0,list_size):
            l.push(i)
        t = timeit.Timer('l.index(random.randrange(list_size))', 'import random', globals=locals())
        results.append(t.timeit(50))
    plt.plot(plot_range, results, 'r*', label="Time to index a random key")
    plt.title("Time to Index DLL")
    plt.xlabel("Size of doubly linked list (items)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    fig = plt.gcf()
    plt.show()
    plt.draw()
    fig.savefig('index_plot_dll.png', dpi=150)

def index_pylist_plot():
    """ Indexes a Python builtin list and benchmarks at a range of sizes """
    results = []
    max_n = 10000
    plot_range = range(1,max_n,100)
    for list_size in plot_range:
        print("Currently {}% complete.".format(list_size/max_n*100))
        l = []
        for i in range(0,list_size):
            l.append(i)
        t = timeit.Timer('l[random.randrange(list_size)]', 'import random', globals=locals())
        results.append(t.timeit(50))

    plt.plot(plot_range, results, 'b*', label="Time to index a random key")
    plt.title("Time to Index Python List")
    plt.xlabel("Size of Python List (items)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    fig = plt.gcf()
    plt.show()
    plt.draw()
    fig.savefig('index_plot_python_list.png', dpi=150)

def multiply_dll_plot():
    """ Multiplies all unique number combinations in my DLL """
    """ benchmarks at a variety of sizes """
    results = []
    max_n = 10000
    plot_range = range(1,max_n,500)
    # TODO: make this a concentric loop
    for list_size in plot_range:
        print("Currently {}% complete.".format(list_size/max_n*100))
        l = DLL()
        for i in range(0,list_size):
            l.push(i)
        t = timeit.Timer('l.multiply_all_pairs()', globals=locals())
        results.append(t.timeit(1))
    plt.plot(plot_range, results, 'g*', label="Time to multiply unique node combinations")
    plt.title("Time to Multiply Across DLL")
    plt.xlabel("Size of doubly linked list (items)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    fig = plt.gcf()
    plt.show()
    plt.draw()
    fig.savefig('multiply_all_plot_dll.png', dpi=150)

# index_dll_plot()
# index_pylist_plot()
# multiply_dll_plot()