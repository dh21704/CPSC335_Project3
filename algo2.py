import random

def algo2(l):
    
    if len(l) <= 1:
        return l
    
    #select a pivot randomly from the list 
    num = random.randint(0, len(l)-1)
    pivot = l[num]
    
    
    less_than = []
    greater_than = []
    equal_than = []
    
    for i in l:
        if i < pivot:
            less_than.append(i)
        elif i > pivot:
            greater_than.append(i)
        else:
            equal_than.append(i)
    
    return algo2(less_than) + [pivot] + algo2(greater_than)
    
    
    
    
    
x = [5, 3, 8, 4, 2, 7, 1, 10]
re = algo2(x)
print(re)
