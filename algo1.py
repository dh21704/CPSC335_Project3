def algo1(R, L):
    r_hash_table = {item: i for i, item in enumerate(R)}
    
    intersection_list = []
    
    print(r_hash_table)
    
    for i in L:
        if i in r_hash_table:
            print(i, ' is in the hash table')
            intersection_list.append(i)
        else:
            print(i, ' is not in the hash table')
            
    return intersection_list
    
    
    
L = [5, 2, 9, 1, 7]
R = [3, 7, 1, 8, 2]


inter_list = algo1(R, L)
print()
print("final answer: ", inter_list)
