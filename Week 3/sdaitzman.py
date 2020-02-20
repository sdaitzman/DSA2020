#!/usr/bin/env python3

"""
Queue class supporting O(1) find_min()
Implemented using Stacks
Sam Daitzman // DSA 2020
"""

import pytest

class Stack:
    def __init__(self):
        ''' Constructor for a Stack '''
        self.items = []
        self.min = []

    def push(self, new):
        ''' Adds a new item to the top of the stack '''
        ''' Treats the end of the list as the top of the stack '''

        # add to end of list
        self.items.append(new)
        if self.min:
            # min list exists
            if new < self.min[-1]:
                # new item is < min, so append it
                self.min.append(new)
            else:
                # new item is ≥ min, so repeat min
                self.min.append(self.min[-1])
        else:
            # min list does not exist
            self.min.append(new)
    
    def pop(self):
        ''' Removes most recently added item in queue and returns it '''
        self.min.pop()
        return self.items.pop()

class Queue:
    ''' A queue class '''
    def __init__(self):
        # make the enqueue stack and the dequeue stack
        self.ins = Stack()
        self.outs = Stack()
    
    def enqueue(self, new):
        ''' Add to end of queue '''
        self.ins.push(new)

    def dequeue(self):
        ''' Return and remove first-added queue item '''
        if not self.outs.items:
            # dequeue stack is empty, so flip the other
            while self.ins.items:
                self.outs.push(self.ins.pop())

        # return the oldest item in the dequeue stack
        return self.outs.pop()
    
    def find_min(self):
        ''' Return the minimum value currently anywhere in the queue '''
    
        # find minimums for each stack, if they exist; otherwise, get None
        ins_min = self.ins.min[-1] if self.ins.min else None
        outs_min = self.outs.min[-1] if self.outs.min else None
        
        # if only one stack exists, return its min
        if ins_min and not outs_min: return ins_min
        if outs_min and not ins_min: return outs_min

        # if both stacks exist, return the lower minimum
        return min(ins_min, outs_min)
    
# TESTING
def test_stack():
    ''' Test basic pop and push in a stack '''
    ''' Also tests finding the minimum '''
    stack = Stack()
    assert stack.items == []
    assert stack.min == []
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    assert stack.items == stack.min == [5,4,3,2,1]
    assert stack.pop() == 1
    assert stack.pop() == 2
    assert stack.items == stack.min == [5,4,3]

def test_queue_basic():
    ''' Tests basic enqueue and dequeue in queue '''
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.ins.items == [1,2,3]
    assert queue.dequeue() == 1
    queue.enqueue(4)
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4

def test_queue_min():
    ''' Tests finding minimum in a queue '''
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.find_min() == 1
    assert queue.dequeue() == 1
    assert queue.find_min() == 2
    assert queue.dequeue() == 2
    queue.enqueue(-10)
    assert queue.find_min() == -10