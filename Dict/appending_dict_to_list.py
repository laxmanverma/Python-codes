dict = {}
list = []
for x in range(0,100):
    dict[1] = x
    list.append(dict)
    #list.append(dict.copy())
 
print list

'''
You would assume the result would be [{1:1}, {1:2}, {1:3}... {1:98}, {1:99}] but instead it is:

[{1: 99}, {1: 99}, {1: 99}, {1: 99}, {1: 99}, {1: 99}, {1: 99}, {1: 99}...., {1: 99}]

You need to append a copy, otherwise you are just adding references to the same dictionary over and over again:
list.append(dict.copy())
'''
