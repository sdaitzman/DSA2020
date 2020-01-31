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
    last = 0
    for i in range(len(m)):
        # print(i)
        # print(m[i])
        if(i == 0):
            # print("First element in list")
            currentList.append(m[i])
            longest.append(m[i])
        else:
            if m[i] > last:
                # print(m[i], "IS GREATER THAN", last)
                currentList.append(m[i])
            else:
                currentList = [m[i]]
            if len(currentList) > len(longest):
                longest = currentList
        last = m[i]
    return longest

def test_longest(longest):
    """
    Tests the longest() function above in the following situations:
    - An empty list should return an empty list
    - A descending list should return a list with the first element
    - A completely increasing list should return the same list
    - Additional test: A list of all the same number should return one item only
    - Additional test: A negative-0-positive increasing list should be returned
    """
    assert longest([]) == []
    assert longest([5,4,3,2,1]) == [5]
    assert longest([0,1,2,3,4,5,6,7,8]) == [0,1,2,3,4,5,6,7,8]
    assert longest([1,1,1,1,1,1,1,1]) == [1]
    assert longest([-3,-2,-1,0,1,2,3,4,5]) == [-3,-2,-1,0,1,2,3,4,5]

# Declare a list and find its longest increasing subsequence
myList = [1, 2, 0, 4, 8, 9, 3]
print(longest(myList))

# Run assertions
test_longest(longest) # returns no errors!
    
    