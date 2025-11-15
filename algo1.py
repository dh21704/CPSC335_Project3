#input: two lists holding integers
#output: one lists that contains numbers that are in both list one and two from input
def algo1(R, L):
    r_hash_table = set(R) #convert R list into hash table
    
    intersection_list = [] #create empty list
    
    print(r_hash_table) #testing
    
    for i in L: #iterate through the left list
        if i in r_hash_table: #if element is in hash table
            print(i, ' is in the hash table') #testing
            intersection_list.append(i) #append the element to the intersection list
        else: #else
            print(i, ' is not in the hash table') #telling the user / testing
            
    return intersection_list #return the intersected list
    
    
#two list creation    
L = [5, 2, 9, 1, 7]
R = [3, 7, 1, 8, 2]

#call algo and print
inter_list = algo1(R, L)
print()
print("final answer: ", inter_list)
