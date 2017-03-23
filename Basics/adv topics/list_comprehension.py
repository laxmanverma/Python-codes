"""List Comprehension Syntax
Here's a simple example of list comprehension syntax:

new_list = [x for x in range(1,6)]
# => [1, 2, 3, 4, 5]
This will create a new_list populated by the numbers one to five. If you want those numbers doubled, you could use:

doubles = [x*2 for x in range(1,6)]
# => [2, 4, 6, 8, 10]
And if you only wanted the doubled numbers that are evenly divisible by three:

doubles_by_3 = [x*2 for x in range(1,6) if (x*2)%3 == 0]
# => [6]
Instructions"""
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

even_squares = [x**2 for x in range(1,11) if(x%2)==0]

print(doubles_by_3)
print(even_squares)

c = ['C' for x in range(5) if x < 3]
print(c)

#Enter no. of elements
n=int(input())
a=[input() for i in range(n)]
print(a)

