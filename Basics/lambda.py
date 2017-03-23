# fgfdgf
"""lambda x: x % 3 == 0
Is the same as

def by_three(x):
    return x % 3 == 0"""

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

"""When we pass the lambda to filter, filter uses the lambda to determine
what to filter, and the second argument
(my_list, which is just the numbers 0 – 15)
is the list it does the filtering on."""

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message=filter(lambda x: x!="X",garbled)
print message
