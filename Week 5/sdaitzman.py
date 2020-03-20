#!/usr/bin/env python3
import pytest
from hypothesis import given
import hypothesis.strategies as st

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

    def __init__(self, oglist=[]):
        ''' Initialize heap from a (possibly empty) list. '''

        self.heap = oglist if len(oglist) > 0 else []
        self.length = len(oglist)

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
        print("length", self.length, "heap", self.heap)
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

    
# a_heap = Heap(oglist=[3, 2, 8, 1, 4, 6, 11])
# print(a_heap.heap)
# print(a_heap.get_length())
# print(a_heap.find_min())

# print(a_heap.insert(-10))
# print(a_heap.insert(1.5))

another_heap = Heap(oglist=[3, 2, 8, 1, 4, 6, 11])
print(another_heap.delete_min())
print(another_heap.delete_min())
print(another_heap.delete_min())
print(another_heap.delete_min())
print(another_heap.delete_min())
print(another_heap.delete_min())
print(another_heap.delete_min())
print(another_heap.delete_min())
print(another_heap.delete_min())
