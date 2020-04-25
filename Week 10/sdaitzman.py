#!/usr/bin/env python3
import numpy as np
import time
from tabulate import tabulate
import sys

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
    # print(tabulate(C))
    # print(C.shape)

    # track visited state with a hashmap and path with a list
    c = [c for c in range(C.shape[0])]       # cities
    v = {node: (False if node > 0 else True) # visited state: True except first
        for node in range(C.shape[0])}       # for all cities
    p = [0]                                  # pathway

    # process all cities
    while len(p) < len(c):
        
        current_city = p[-1]     # current city
        best_dist = float('inf') # best distance so far
        best_city = None         # best next city so far

        # iterate thru all possible neighbors
        for i in range(C.shape[0]):
            dist = C[current_city][i]
            # print(current_city, i, dist, { key:value for (key,value) in v.items() if value})
            if dist == 0: continue # skip past self
            if v[i]: continue      # skip past visited
            if dist < best_dist:
                # print('New Minimum: ', best_dist, ' from ', current_city, ' to ', best_city)
                best_dist = dist
                best_city = i
        p.append(best_city)
        v[best_city] = True
    return p

C = read_tsp('TSP/gr24.tsp')
print(nearest_neighbor(C))

# ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---
#   0  257  187   91  150   80  130  134  243  185  214   70  272  219  293   54  211  290  268  261  175  250  192  121
# 257    0  196  228  112  196  167  154  209   86  223  191  180   83   50  219   74  139   53   43  128   99  228  142
# 187  196    0  158   96   88   59   63  286  124   49  121  315  172  232   92   81   98  138  200   76   89  235   99
#  91  228  158    0  120   77  101  105  159  156  185   27  188  149  264   82  182  261  239  232  146  221  108   84
# 150  112   96  120    0   63   56   34  190   40  123   83  193   79  148  119  105  144  123   98   32  105  119   35
#  80  196   88   77   63    0   25   29  216  124  115   47  245  139  232   31  150  176  207  200   76  189  165   29
# 130  167   59  101   56   25    0   22  229   95   86   64  258  134  203   43  121  164  178  171   47  160  178   42
# 134  154   63  105   34   29   22    0  225   82   90   68  228  112  190   58  108  136  165  131   30  147  154   36
# 243  209  286  159  190  216  229  225    0  207  313  173   29  126  248  238  310  389  367  166  222  349   71  220
# 185   86  124  156   40  124   95   82  207    0  151  119  159   62  122  147   37  116   86   90   56   76  136   70
# 214  223   49  185  123  115   86   90  313  151    0  148  342  199  259   84  160  147  187  227  103  138  262  126
#  70  191  121   27   83   47   64   68  173  119  148    0  209  153  227   53  145  224  202  195  109  184  110   55
# 272  180  315  188  193  245  258  228   29  159  342  209    0   97  219  267  196  275  227  137  225  235   74  249
# 219   83  172  149   79  139  134  112  126   62  199  153   97    0  134  170   99  178  130   69  104  138   96  104
# 293   50  232  264  148  232  203  190  248  122  259  227  219  134    0  255  125  154   68   82  164  114  264  178
#  54  219   92   82  119   31   43   58  238  147   84   53  267  170  255    0  173  190  230  223   99  212  187   60
# 211   74   81  182  105  150  121  108  310   37  160  145  196   99  125  173    0   79   57   90   57   39  182   96
# 290  139   98  261  144  176  164  136  389  116  147  224  275  178  154  190   79    0   86  176  112   40  261  175
# 268   53  138  239  123  207  178  165  367   86  187  202  227  130   68  230   57   86    0   90  114   46  239  153
# 261   43  200  232   98  200  171  131  166   90  227  195  137   69   82  223   90  176   90    0  134  136  165  146
# 175  128   76  146   32   76   47   30  222   56  103  109  225  104  164   99   57  112  114  134    0   96  151   47
# 250   99   89  221  105  189  160  147  349   76  138  184  235  138  114  212   39   40   46  136   96    0  221  135
# 192  228  235  108  119  165  178  154   71  136  262  110   74   96  264  187  182  261  239  165  151  221    0  169
# 121  142   99   84   35   29   42   36  220   70  126   55  249  104  178   60   96  175  153  146   47  135  169    0
# ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---

