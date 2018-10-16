def main():
    
    # List of string 
    list1 = ['Hi' ,  'hello', 'at', 'this', 'there', 'from']
    
    # List of string
    list2 = ['there' , 'hello', 'Hi']
    
    '''    
        check if list1 contains all elements in list2
    '''
    result =  all(elem in list1  for elem in list2)
    
    if result:
        print("Yes, list1 contains all elements in list2")    
    else :
        print("No, list1 does not contains all elements in list2")    
        
    
    '''    
        check if list1 contains any elements of list2
    '''
    result =  any(elem in list1  for elem in list2)
    
    if result:
        print("Yes, list1 contains any elements of list2")    
    else :
        print("No, list1 contains any elements of list2")        

        
if __name__ == '__main__':
    main()