"""
M=[int(n) for n in input().split()]
This reads a line, splits it at white spaces,
and applies int() to every element of the result.
"""
n=input()
a=[input() for i in range(n)]
a.sort()
print a
