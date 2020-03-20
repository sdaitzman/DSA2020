#!/usr/bin/env python3
import pytest
from hypothesis import given
import hypothesis.strategies as st
import copy
import numpy as np

class Heap:
    def heapify(self, position):
        ''' Recursively converts a list to a heap in O(n)
        Based on NIST heapify: https://xlinux.nist.gov/dads/HTML/heapify.html
        Algoritm modified to start at bottom of tree
        '''

        left_index  = position * 2 + 1
        right_index = position * 2 + 2
        smallest    = position # checked later

        # if a left child exists in the heap
        if left_index < self.length:
            # if it is less than its parent, record that
            if self.heap[left_index] < self.heap[position]:
                smallest = left_index

        # if a right child exists in the heap
        if right_index < self.length:
            # if it is less than current smallest, record that
            if self.heap[right_index] < self.heap[smallest]:
                smallest = right_index
        
        # swap parent with child if parent is not smallest
        if position != smallest:
            temp = self.heap[smallest]
            self.heap[smallest] = self.heap[position]
            self.heap[position] = temp

            # run heapify again on the smaller value
            self.heapify(smallest)

    def __init__(self, oglist=[], create_deepcopy=True):
        ''' Initialize heap from a (possibly empty) list. '''

        # initialize starter list, deepcopying/creating if needed
        starter_list = copy.deepcopy(oglist) if create_deepcopy else oglist
        self.heap = starter_list if len(starter_list) > 0 else []
        self.length = len(starter_list)

        # repeatedly fix heap structure from end to start
        for i in range(self.length-1, -1, -1):
            self.heapify(i)
            # print(self.heap)

    def get_length(self):
        ''' Return length of the heap. '''
        return self.length

    def insert(self, value):
        ''' Insert value into the heap. '''

        # append as final leaf of existing heap
        self.heap.append(value)

        position = self.length
        while position > 0:
            # get parent position
            parent = (position - 1) // 2

            if self.heap[position] < self.heap[parent]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[position]
                self.heap[position] = temp
            
            position = parent

        # increase list length tracker
        self.length += 1

        return self.heap


    def delete_min(self):
        ''' Remove the min (root) from heap. '''
        # print("length", self.length, "heap", self.heap)
        if self.length > 1:
            ret = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.length -= 1
            self.heapify(0)
            return ret
        elif self.length == 1:
            self.length = 0
            return self.heap.pop()
        else: return None # if list is empty
        
        

    def find_min(self):
        ''' Return min value in the heap. '''
        return self.heap[0]

    def sorted_list(self):
        ''' Return a sorted list of all heap elements. '''
        ret = []

        # deep copy the list so this is nondestructive
        c = copy.deepcopy(self)
        
        # repeatedly delete the new min and append it to our list
        # this operation is O(log n) and takes place O(n) times
        # so this is O(n log n)!
        for i in range(c.length): ret.append(c.delete_min())
        return ret

# ---------- TESTS ----------

@given(st.lists(st.integers()))
def test_heap_len(l):
    ''' A sample test that checks heap length works as expected '''
    h = Heap(l)
    assert len(l) == h.get_length()
    assert len(l) == len(h.heap)

@given(st.lists(st.integers()))
def test_heap_insert_delete(l):
    ''' A sample test that checks heap insertion and deletion work as expected '''
    h = Heap([])

    # test that the heap begins empty with length 0
    assert h.heap == []
    assert h.get_length() == 0

    heap_size = 0
    for i in range(len(l)):
        h.insert(l[i])
        heap_size += 1

        # check that the heap size grows appropriately
        assert heap_size == h.get_length()

        # check that the value we added is in the heap
        assert l[i] in h.heap

        # check that every value before the one we added is also in the heap
        for j in range(i): assert l[j] in h.heap
    
    # test that the heap length remains accurate after these inserts
    assert len(l) == h.get_length()
    assert len(l) == len(h.heap)

    for i in range(len(l)):
        # check that the minimum in the heap was the minimum in the list at each 
        assert h.delete_min() == min(l)

        # strip current minimum of test list
        l.remove(min(l))

        # check that the list lengths match
        assert len(l) == h.get_length()
    
    # check that deletions on emptied heap return a None
    for i in range(3): assert h.delete_min() == None

@given(st.lists(st.integers()))
def test_heap_init_delete(l):
    ''' A sample test that checks heap initialization and deletion work as expected '''
    h = Heap(l)

    # check that the value we added is in the heap
    for i in range(len(l)): assert l[i] in h.heap

    # test that the heap length is accurate
    assert len(l) == h.get_length()
    assert len(l) == len(h.heap)

    for i in range(len(l)):
        # check that the minimum in the heap was the minimum in the list at each step
        assert h.delete_min() == min(l)

        # strip current minimum from test list
        l.remove(min(l))

        # check that the list lengths match
        assert len(l) == h.get_length()

    # check that deletions on emptied heap return a None
    for i in range(3): assert h.delete_min() == None

@given(st.lists(st.integers()))
def test_heap_sorted_list(l):
    ''' A sample test that checks heap list sorting works as expected '''
    h = Heap(l)

    # check that list is sorted
    assert h.sorted_list() == sorted(l)

    # check that the heap is still the same as before
    assert Heap(l).heap == h.heap

# test_heap_sorted_list()


# a_heap = Heap(oglist=[0])
# print(a_heap.heap)
# print(a_heap.length)
# print(len(a_heap.heap))
# print(a_heap.get_length())


# a_heap = Heap(oglist=[])
# print(a_heap.heap)
# print(a_heap.length)
# print(a_heap.get_length())


# a_heap = Heap(oglist=[3, 2, 8, 1, 4, 6, 11])
# print(a_heap.heap)
# print(a_heap.get_length())
# print(a_heap.find_min())

# print(a_heap.insert(-10))
# print(a_heap.insert(1.5))

# another_heap = Heap(oglist=[3, 2, 8, 1, 4, 6, 11])
# print(another_heap.delete_min())
# print(another_heap.delete_min())
# print(another_heap.delete_min())
# print(another_heap.delete_min())
# print(another_heap.delete_min())
# print(another_heap.delete_min())
# print(another_heap.delete_min())
# print(another_heap.delete_min())
# print(another_heap.delete_min())

# another_heap = Heap(oglist=[3, 2, 8, 1, 4, 6, 11])
# print(another_heap.heap)
# print(another_heap.sorted_list())
