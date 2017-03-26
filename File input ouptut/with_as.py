with open("text.txt","w") as my_file:
    my_file.write("Yo bro! successfully wrote to text.txt.")

""" file objects contain a special pair of built-in methods: __enter__()
and __exit__().
when a file object's __exit__() method is invoked, it automatically closes
the file. How do we invoke this method? With with and as.

The syntax looks like this:

with open("file", "mode") as variable:
    variable.write(" data")
    
"""
