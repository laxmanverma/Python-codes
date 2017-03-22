#for loop
for i in range(1,5):
    print(i)

a=[1,2,3,4,5]
for i in a:
    print(i)

for ch in 'abacadabra':
    if ch in 'aeiou':
        print ('letter' ,ch, 'is a vowel')
    else:
        print ('letter' ,ch, 'is not a vowel')

"""Multiple lists
It's also common to need to iterate over two lists at once. This is where the built-in zip function comes in handy.
zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
zip can handle three or more lists as well!"""

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a>b:
        print(a)
    else:
        print (b)

#enumerate function works by supplying a corresponding index to each element in the list that you pass it
choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Your choices are:')
for index, item in enumerate(choices):
    print (index+1, item)

#Looping over a dictionary
d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
    if d[key] == 10:
        print( "This dictionary has the value 10! at", key)
