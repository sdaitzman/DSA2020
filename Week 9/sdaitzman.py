#!/usr/bin/env python3

def wildcard_string_compare(s1, s2):
    ''' Compares the strings s1 and s2, where s1 is a normal input string
        and s2 is a wildcard pattern string where some characters may be
        asterisks (*), and can be replaced by any or no character.
    '''

    m = len(s1) # the text we're checking e.g. hello
    n = len(s2) # the wildcard pattern    e.g. h*llo

    # begin at index 0 for implementation clarity
    i = 0;
    j = 0;

    starIndex = -1;
    iIndex = -1;


    # while not at end of text
    while(i < m):

        # if not at end and characters match, move to next
        if(j < n and s2[j] == s1[i]):
            i += 1
            j += 1

        # if not at end and hit wildcard, set pointer to current wildcard and
        # set location in text to current index and iterate through wildcard
        elif(j < n and s2[j] == '*'):
            starIndex = j
            iIndex = i
            j = j + 1

        # if none of these checks have happened and we have some wildcard so far
        # iterate position past wildcard in both strings and continue to next
        # letter in text string we're checking
        elif(starIndex != -1):
            j = starIndex + 1
            i = iIndex + 1
            iIndex += 1

        # if none of these cases are true, under the principle of optimality
        # we must return False, since the strings cannot match
        else: return False
    
    # count up remaining length not covered or accounted for by wildcard
    while(j < n and s2[j] == '*'): j += 1
    
    # return truthy if all letters were accounted for in our DP iterator
    return j == n


s1 = 'hi'
s2 = 'h*'
print(wildcard_string_compare(s1, s2))


s1 = 'hello'
s2 = 'h*llo'
print(wildcard_string_compare(s1, s2))

s1 = 'heeeeello'
s2 = 'h*llo'
print(wildcard_string_compare(s1, s2))

s1 = 'foo'
s2 = 'h*llo'
print(wildcard_string_compare(s1, s2))