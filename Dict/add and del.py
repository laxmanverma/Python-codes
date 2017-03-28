menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

menu['jh']=54
menu['as']=45
menu['dfg']=12

print "There are " + str(len(menu)) + " items on the menu."
print menu

del menu['jh']
print menu
