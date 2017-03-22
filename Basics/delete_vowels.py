#delete vowel from given string
def anti_vowel(text):
    j=0
    s=''
    for n in text:
        if(n not in "aeiouAEIOU"):
            s=s+n
    return s

x=anti_vowel('asddiou snxcz')
print(x)
