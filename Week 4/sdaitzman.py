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

def test_choose_meals():
    """ Test the choose_meals function on sample data """

    # Basic right-hand situation
    scores = [1, 3, 4, -100, 25]
    assert choose_meal(scores) == (4, 4, 25)

    # A case where the middle should exclude the right
    scores = [25, 1, -8, 3, 4]
    assert choose_meal(scores) == (0, 1, 26)

    # A case where all values should be included
    scores = [1, 3, 4, 25]
    assert choose_meal(scores) == (0, 3, 33)

    # A case where only one value is positive
    scores = [-1, -3, -4, 25]
    assert choose_meal(scores) == (3, 3, 25)

    # Some cases where no values are positive
    assert choose_meal([-1, -3, -4, -25]) == (0, 0, -1)
    assert choose_meal([-3, -1, -4, -25]) == (1, 1, -1)

def random_uniform(samples, n, bounds):

    # adds one to upper bound because randint is exclusive there
    lists = np.random.randint(bounds[0], bounds[1] + 1, size=[samples,n])
    lengths = []
    max_values = []

    for i in lists:
        meal = choose_meal(i)
        lengths.append(meal[1] - meal[0])
        max_values.append(meal[2])

    print('UNIFORM:')
    print('Mean length of interval: ', np.mean(lengths))
    print('Mean max value found across interval: ', np.mean(max_values))

def random_nonuniform():

    thing = 0

    # adds one to upper bound because randint is exclusive there
    lists = np.random.normal(loc=6, scale=1, size=[100,100])
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if np.random.rand() > 0.7:
                lists[i][j] = np.random.normal(loc=-7, scale=0.5)


    lengths = []
    max_values = []

    for i in lists:
        meal = choose_meal(i)
        lengths.append(meal[1] - meal[0])
        max_values.append(meal[2])

    print('NONUNIFORM:')
    print('Mean length of interval: ', np.mean(lengths))
    print('Mean max value found across interval: ', np.mean(max_values))


random_uniform(100,100, (-10, 10));print()
random_nonuniform()
