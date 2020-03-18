#!/usr/bin/env python3

"""
Dining hall happiness problem
AKA: maximum subarray problem
Sam Daitzman // DSA 2020
"""

import numpy as np

def search_cross_subarray(happiness_scores, start_index, mid_index, end_index):
    """ Finds the greatest consecutive list across the middle and returns it
    happiness_scores: list of happiness scores for all items
    start_index: start bound of range we are searching for a middle-crossing max
    mid_index: middle division of range
    end_index: end division of range we're searching
    """

    # set our initial max to -∞
    # this allows the algorithm to work with negative numbers
    curr_max    = -float("inf")
    current_sum = 0
    end_index  += 1

    # iterate from middle to start
    for i in range(mid_index, start_index-1, -1):
        current_sum += happiness_scores[i]
        if current_sum > curr_max:
            start_index = i
            curr_max = current_sum

    # iterate from middle to end
    for i in range(mid_index+1, end_index):
        current_sum += happiness_scores[i]
        if current_sum > curr_max:
            end_index = i
            curr_max = current_sum
    
    # yay, a tuple!
    return (start_index, end_index, curr_max)


   

def choose_meal(happiness_scores, start_index=0, end_index=None):
    """ Looks in a list for the greatest consecutive sum and returns its indices
    happiness_scores: list of happiness scores
    start_index: start index in overall list (default at top of tree = 0)
    end_index: end index in overall list (default at top of tree = list length)
    """

    # set end index if not set
    if end_index == None: end_index = len(happiness_scores) - 1

    # return list at base case
    if start_index == end_index:
        if happiness_scores[start_index] < 0:
            # returning an empty list breaks things here, so I return -∞
            return (start_index, end_index, -float("inf"))
        return (start_index, end_index, happiness_scores[start_index])

    # find the middle of the list
    middle_index = int((start_index + end_index) / 2)

    # search for solutions across the middle of the list
    (middle_start_index, middle_end_index, middle_sum) = search_cross_subarray(happiness_scores, start_index, middle_index, end_index)

    # recursively search left and right sections of the list
    (left_start_index , left_end_index , left_sum)  = choose_meal(happiness_scores, start_index, middle_index)
    (right_start_index, right_end_index, right_sum) = choose_meal(happiness_scores, middle_index+1, end_index)

    # return greatest value
    if  left_sum  >= right_sum and left_sum >= middle_sum:
        # print('left', left_sum)
        return (left_start_index , left_end_index , left_sum ) 
    if  right_sum >= left_sum and right_sum >= middle_sum:
        # print('right', right_sum)
        return (right_start_index, right_end_index, right_sum)
    if middle_sum >= left_sum and middle_sum >= right_sum:
        # print('middle', middle_sum)
        return (middle_start_index, middle_end_index, middle_sum)

options = ["french fries", "brussel sprouts", "chicken sandwiches", "tomato soup", "fruit salad"]

scores = [1, 3, 4, -100, 25]
print(scores, " → ", choose_meal(scores))

scores = [25, 1, -8, 3, 4]
print(scores, " → ", choose_meal(scores))

scores = [1, 3, 4, 25]
print(scores, " → ", choose_meal(scores))

scores = [-1, -3, -4, 25]
print(scores, " → ", choose_meal(scores))

