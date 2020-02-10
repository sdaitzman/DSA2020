#!/usr/bin/env python3

"""
Doubly Linked List class
Sam Daitzman // DSA 2020
"""

import pytest
import timeit
import random

class Node:
    def __init__(self,val=None,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self):
        ''' Constructor for an empty list '''

    def length(self):
        ''' Returns the number of nodes in the list '''

    def push(self, val):
        ''' Adds a node with value equal to val to the front of the list '''

    def insert_after(self, prev_node, val):
        ''' Adds a node with value equal to val in the list after prev_node '''
    
    def delete(self, node):
        ''' Removes node from the list '''

    def index(self, i):
        ''' Returns the node at position i (i<n) '''

    def multiply_all_pairs(self):
        ''' Multiplies all unique pairs of nodes values for nodes i, j (i != j) 
        and returns the sum '''


