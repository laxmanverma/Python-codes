#1
print("#1")
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

import numpy as np

np_baseball= np.array(baseball)
print(np_baseball)
print(type(np_baseball))

#2
print("#2")
# Create a Numpy array from baseball
np_height=np.array(baseball)
np_height = np_height*0.0254
print(np_height)

newarr= np.array([10,9,8])
print("newarr=",newarr)

#3
print("#3")
#Create a null vector of size 10
Z = np.zeros(10)
print(Z)
Z[4]=1
print(Z)

#4
print("#4")
low=np.array(np_baseball< 200)  #a new numpy array low is created which stores
print(low)                      #the values as true or false acc. to condition
print(np_baseball[low])

#5
print("#5")
""" Numpy arrays cannot contain elements with different types. If you try to
build such a list, some of the elments' types are changed to end up with a
homogenous list. This is known as type coercion."""

print(np.array([True, 1, 2]) + np.array([3, 4, False]))

