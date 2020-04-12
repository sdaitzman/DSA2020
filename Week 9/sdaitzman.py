#!/usr/bin/env python3

def wildcard_string_compare(s1, s2):
    ''' Compares the strings s1 and s2, where s1 is a normal input string
        and s2 is a wildcard pattern string where some characters may be
        asterisks (*), and can be replaced by any or no character.
    '''

    m = len(s1) # the text we're checking e.g. hello
    n = len(s2) # the wildcard pattern    e.g. h*llo


    # https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
    # extra row and column for base case/final answer fitting
    W = [[False for i in range(n + 1)] for j in range(m + 1)]

    # a base case here is that for no text or wildcard, things match
    W[0][0] = True

    # iterate through loop
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if we're at a matching wildcard or if things are identical
            if(s2[j - 1] == "*" or s1[i-1] == s2[j-1]):
                W[i][j] = W[i-1][j-1]
            else:
                W[i][j] = False
    return W[m][n]

s1 = 'hi'
s2 = 'h*'
print(wildcard_string_compare(s1, s2))


s1 = 'hello'
s2 = 'h*llo'
print(wildcard_string_compare(s1, s2))