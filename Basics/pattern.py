#print pattern
a=int(input('enter'))
for i in range(a):
    j=0
    for j in range(i):
        print('#')

#for printing in same line
for i in range(a):
    j=0
    #print('\n')
    for j in range(i):
        print('#',end="")
    print ('')
    
#using single loop
for i in range(a):
    print('#'*i)

#using while loop
i=0
while i<a:
    print('#'*i)
    i=i+1
