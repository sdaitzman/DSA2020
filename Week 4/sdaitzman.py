#!/usr/bin/env python3

"""
Dining hall happiness problem
AKA: maximum subarray problem
Sam Daitzman // DSA 2020
"""

import numpy as np

def search_cross_subarray(happiness_scores, start_index, mid_index, end_index):
    """ Finds the greatest consecutive list across the middle and returns it

    """

    # set our initial maxes to infinitely negative floats
    # this allows the algorithm to work with negative numbers
    left_max    = -float("inf")
    right_max   = -float("inf")
    current_sum = 0

    # go from middle to start
    for i in range(mid_index, start_index-1, -1):
        current_sum += happiness_scores[i]
        if current_sum > left_max:
            start_index = i
            left_max = current_sum

    # go from middle to end
    for i in range(mid_index+1, end_index):
        current_sum += happiness_scores[i]
        if current_sum > right_max:
            end_index = i
            right_max = current_sum
    
    # yay, a tuple!
    return (start_index, end_index, left_max + right_max)


   

def choose_meal(happiness_scores, start_index=0, end_index=None):
    """ Looks in a list for the greatest consecutive sum and returns its indices
    happiness_scores: list of happiness scores
    start_index: start index in overall list
    end_index:     end index in overall list
    """

    print(start_index, end_index)

    # set end index if not set
    if end_index == None: end_index = len(happiness_scores)-1

    # return list at base case
    if start_index == end_index: return (start_index, end_index, happiness_scores[start_index])

    # find the middle of the list
    middle_index = int((start_index + end_index) / 2)

    # search for solutions across the middle of the list
    (middle_start_index, middle_end_index, middle_sum) = search_cross_subarray(happiness_scores, start_index, middle_index, end_index)

    # recursively search left and right sections of the list
    (left_start_index , left_end_index , left_sum)  = choose_meal(happiness_scores, start_index, middle_index)
    (right_start_index, right_end_index, right_sum) = choose_meal(happiness_scores, middle_index+1, end_index)

    # return greatest value
    if  left_sum  >= right_sum and left_sum >= middle_sum:
        print('left')
        return (left_start_index , left_end_index , left_sum ) 
    if  right_sum >= left_sum and right_sum >= middle_sum:
        print('right')
        return (right_start_index, right_end_index, right_sum)
    if middle_sum >= left_sum and middle_sum >= right_sum:
        print('middle')
        return (middle_start_index, middle_end_index, middle_sum)

options = ["french fries", "brussel sprouts", "chicken sandwiches", "tomato soup", "fruit salad"]

scores = [1, 3, 4, -100, 25]
# print(choose_meal(scores))

scores = [1, 3, 4, 25]
print(choose_meal(scores))


scores = [25, 1, -8, 3, 4]
# print(choose_meal(scores))