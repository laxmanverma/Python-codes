my_list = [i**2 for i in range(1,11)]

"""f = open("output.txt", "w")
This told Python to open output.txt in "w" mode ("w" stands for "write").
We stored the result of this operation in a file object, f."""

my_file = open("output.txt", "r+")
# "r+"  will allow both read and write
# second argument will be "w" if we only want to open the file for writing and
# will be "r" for reading

for i in my_list:
    my_file.write(str(i) + '\n')
     #The write() function takes a string argument


#print my_file.read()
"""if we make this( print my_file.read() ) a python statement i.e., remove #
from front of it then the statement "my_file.write(str(i) + '\n')" will write
anything in addition to what we have to write in output.txt because we have
called another function before closing the file.""" 

my_file.close()
"""You must close the file.
If you don't close your file, Python won't write to it properly."""

my_file = open("output.txt", "r")
print(my_file.read())
my_file.close()



"""Why we always need to close our files
after we're done writing to them?

During the I/O process, data is buffered: this means that it is held in a
temporary location before being written to the file.
Python doesn't flush the buffer—that is, write data to the file—until
it's sure you're done writing. One way to do this is to close the file.
If you write to a file without closing,
the data won't make it to the target file."""
