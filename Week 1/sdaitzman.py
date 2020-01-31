#!/usr/bin/env python3
# DSA 2020
# Data Structures and Algorithms
# Homework 1 Python portion
# Sam Daitzman


def longest(m):
    """
    Returns the longest strictly increasing subsequence in a list m.
    Arguments: m, a list containing numbers.
    """
    currentList = []
    longest = []
    for i in range(len(m)):
        # print(i)
        # print(m[i])
        if(i == 0):
            print("First element in list")
            currentList.append(m[i])
            longest.append(m[i])
    return longest

myList = [1, 2, 0, 4, 8, 9, 3]
print(longest(myList))
    
    