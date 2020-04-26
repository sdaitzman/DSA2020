#!/usr/bin/env python3
import numpy as np
import time
from tabulate import tabulate
import sys
import copy

def read_tsp(filename):
    ''' Reads a TSPLIB instance given by filename and returns the corresponding
    distance matrix C. Assumes that the edge weights are given in lower diagonal row
    form. '''

    f = open(filename,'r')

    n, C = 0, None
    i, j = -1, 0

    for line in f:
        words = line.split()
        if words[0] == 'DIMENSION:':
            n = int(words[1])
            C = np.zeros(shape=(n,n))
        elif words[0] == 'EDGE_WEIGHT_SECTION':
            i = 0 # Start indexing of edges
        elif i >= 0:
            for k in range(len(words)):
                if words[k] == 'EOF':
                    break
                elif words[k] == '0':
                    i += 1 # Continue to next row of the matrix
                    j = 0
                else:
                    C[i,j] = int(words[k])
                    C[j,i] = int(words[k])
                    j += 1

    return C

def nearest_neighbor(C):
    '''
    Follows a nearest-neighbor heuristic to return a short-ish path through a
    matrix of node distances.

    C: an array of distances
    '''
    # track visited state with a hashmap and path with a list
    c = [c for c in range(C.shape[0])]       # cities
    v = {node: (False if node > 0 else True) # visited state: True except first
        for node in range(C.shape[0])}       # for all cities
    p = [0]; d = 0                           # pathway and total distance

    # process all cities
    while len(p) < len(c):
        current_city = p[-1]     # current city
        best_dist = float('inf') # best distance so far
        best_city = None         # best next city so far

        # iterate thru all possible neighbors
        for i in range(C.shape[0]):
            dist = C[current_city][i]
            if dist == 0: continue # skip past self
            if v[i]: continue      # skip past visited
            if dist < best_dist:
                best_dist = dist
                best_city = i
        p.append(best_city)
        v[best_city] = True
        d += best_dist
    return p,d




def swap_2opt(p, i, k):
    '''
    Perform a two-opt swap of nodes in path p around indices i and k
    '''
    n = []
    for j in range(k,i-1,-1): n.append(p[j])   # insert i thru k in reverse
    for j in range(i): n.insert(j,p[j])        # insert 0 thru i
    for j in range(k+1,len(p)): n.append(p[j]) # insert k thru end
    return n

def path_length(C, p):
    '''
    Returns the length of a path given its corresponding distance matrix.

    C: distance matrix
    p: a path through the nodes
    '''
    distances = [C[p[i-1]][p[i]] for i in range(len(p))] # get all distances
    return sum(distances) # return their sum

def optimize_path_2opt(C, p, lim=None, max_iter=None):
    '''
    Attempts to improve an existing traveling salesman solution using the
    two-opt heuristic, which tries swapping all pairs of edges around and takes
    swaps that will reduce the local distance. This local search can reduce the
    number of crossing paths to eliminate some travel distance.

    C: distance matrix
    p: a path through the matrix
    lim: neighborhood distance to explore
    max_iter: max iterations to pursue before terminating and returning best so far
    '''

    # don't limit local neighborhood or iterations if no limits are set
    L = len(p)
    if not lim: lim = L
    if not max_iter: max_iter = float('inf')

    # initialize our value tracking variables
    route = copy.deepcopy(p) # deepcopy route so function is idempotent
    n = 0
    improved = True

    # continue until improvement is detected or we hit max_iter
    while improved and n < max_iter:
        improved = False
        n += 1

        # set current target
        best_dist = path_length(C, route)
        for i in range(L): # for all nodes
           
            # check all neighbors within constraints
            for k in range(i+1, min(i+1+lim, L)):
                alt = swap_2opt(route, i, k)
                dist = path_length(C, alt)

                # if an alternative would be better...
                if dist < best_dist:
                    route = alt      # set best route so far
                    best_dist = dist # set best distance so far
                    improved = True  # flip improvement flag so we repeat again
                    continue
    return route

def just_2opt(C):
    ''' Runs 2-opt on a 0-end default start condition '''
    p = [i for i in range(len(C))]
    return optimize_path_2opt(C, p)

def nn_and_2opt(C):
    ''' Runs nn and then follows up with 2-opt '''
    p, dist = nearest_neighbor(C)
    return optimize_path_2opt(C, p)

# C = read_tsp('TSP/gr48.tsp')
# print(path_length(C, nn_and_2opt(C)))

# print(just_2opt(C))

# p, dist = nearest_neighbor(C)
# print(path_length(C, p), '\t:\t', p)
# p2opt = optimize_path_2opt(C, p, None, None)
# print(path_length(C, p2opt), '\t:\t', p2opt)

def optimality_gap(f, C, optimal):
    result = f(C)[1]
    gap = result - optimal
    return result, gap

def runtime(f, C):
    started = time.time()
    f(C)
    return time.time() - started

# print(optimality_gap(nearest_neighbor, C, 100))
# print(runtime(nearest_neighbor, C))

# print(optimality_gap(just_2opt, C, 100))
# print(runtime(just_2opt, C))

def print_gaps_and_timing(files, functions, optimal):
    for file in files:
        print('File \t\t Function \t\t\t\t\t Result \t gap')
        print('-------------------------------------------------------------------------------------')
        for f in functions:
            C = read_tsp(file)
            t = runtime(f, C)
            result, gap = optimality_gap(f, C, optimal[file])
            print(file, '\t', f, '\t', result, '\t', gap)
        print('\n')


files = ['TSP/gr17.tsp', 'TSP/gr21.tsp', 'TSP/gr24.tsp', 'TSP/gr48.tsp']
functions = [nearest_neighbor, just_2opt, nn_and_2opt]
optimal = {
    "TSP/gr17.tsp": 2085,
    "TSP/gr21.tsp": 2707,
    "TSP/gr24.tsp": 1272,
    "TSP/gr48.tsp": 5046
}
print_gaps_and_timing(files, functions, optimal)
