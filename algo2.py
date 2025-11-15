import random

#input: recieve a list with integers
#output: recursive algorithm that eventually returns a list in ascending order
def algo2(l):
    
    if len(l) <= 1: #if list is less than or equal to 1
        return l #return list
    
    #select a pivot randomly from the list 
    num = random.randint(0, len(l)-1)
    pivot = l[num]
    
    #create list for pivot<, pivot>, and pivot==    
    less_than = []
    greater_than = []
    equal_than = []

    #iterate through the list
    for i in l:
        if i < pivot: #if i is less than pivot
            less_than.append(i)
        elif i > pivot: #if i is greater than pivot
            greater_than.append(i) 
        else: #if i is == then
            equal_than.append(i)

    #recursive
    return algo2(less_than) + equal_than + algo2(greater_than)
    
    
    
    
#create list, call algo, and then print    
x = [5, 3, 8, 4, 2, 7, 1, 10]
re = algo2(x)
print(re)
