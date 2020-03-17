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
    left_max  = -float("inf")
    right_max = -float("inf")

    for i in range(mid_index, start_index, -1):
        print(i)

def choose_meal(happiness_scores, start_index=0, end_index=None):
    """ Looks in a list for the greatest consecutive sum and returns its indices
    happiness_scores: list of happiness scores
    start_index: start index in overall list
    end_index:     end index in overall list
    """

    # set end index if not set
    end_index = end_index if end_index else len(happiness_scores)-1

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
    if  left_sum  >= right_sum and left_sum >= middle_sum: return (left_start_index , left_end_index , left_sum ) 
    if  right_sum >= left_sum and right_sum >= middle_sum: return (right_start_index, right_end_index, right_sum)
    if middle_sum >= left_sum and middle_sum >= right_sum: return (middle_start_index, middle_end_index, middle_sum)

    return None



options = ["french fries", "brussel sprouts", "chicken sandwiches", "tomato soup", "fruit salad"]
scores = [1, 3, 4, -100, 25]
choose_meal(scores)
choose_meal(scores, 0, 10)