#to reverse a given string
def reverse(str):
    s=''
    for n in str:
        s=n+s
    str=s
    return str

a=reverse('abcd')
print a
