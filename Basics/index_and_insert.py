animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")  #index() gives the index of duck i.e., 2
print("duck_index=",duck_index)
animals.insert(duck_index,"cobra")  #insert adds cobra at index= duck_indexand moves everything after it in the list by down by 1
print(animals)
