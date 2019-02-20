import copy

list_1 = [[1, 2, 3], [4, 5, 6], 7]
list_2 = list_1
print(id(list_1))
print(id(list_2))

list_2[0] = 'a'
print(list_1)
print(list_2)
print("************************")
'''
The difference between shallow and deep copying is only relevant for compound objects 
(objects that contain other objects, like lists or class instances):

A shallow copy constructs a new compound object and then (to the extent possible) 
inserts references into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively, inserts copies 
into it of the objects found in the original
'''
#shallow copy it only copies the object nested elements are still referenced
list_3 = [[1, 2, 3], [4, 5, 6], 7]
list_4 = copy.copy(list_3)
print(id(list_3))
print(id(list_4))
list_3[0][1] = 'c'
print((list_3))
print((list_4))
list_3[1] = 'AA'
print(list_3)
print(list_4)
print("************************")

#deepcopy it completely copies the object and its nested elements recursively
list_3 = [[1, 2, 3], [4, 5, 6], 7]
list_4 = copy.deepcopy(list_3)
print(id(list_3))
print(id(list_4))
list_3[0][1] = 'c'
print((list_3))
print((list_4))
list_3[1] = 'AA'
print(list_3)
print(list_4)
