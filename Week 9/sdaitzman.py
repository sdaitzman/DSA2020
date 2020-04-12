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


    while(i < m):
        if(j < n and s2[j] == s1[i]):
            i += 1
            j += 1
        elif(j < n and s2[j] == '*'):
            starIndex = j
            iIndex = i
            j = j + 1
        elif(starIndex != -1):
            j = starIndex + 1
            i = iIndex + 1
            iIndex += 1
        else: return False
    
    while(j < n and s2[j] == '*'):
        j += 1
    
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