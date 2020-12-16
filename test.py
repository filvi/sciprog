def rec(el, lst, i):       
    
    if i == 0:
        return False    
    
    if el == lst[i - 1]:
        return True
    
    else:
        return rec(el, lst, i - 1)
    
    
def search(el, lst):
    return find_rec(el, lst, len(lst))

assert rec(6, [], 0) == False
assert rec(5, [5], 0) == False
assert rec(5, [5], 1) == True
assert rec(2, [2,9], 0) == False
assert rec(2, [2,9], 1) == True
assert rec(2, [2,9], 2) == True
assert rec(5, [9,5], 2) == True
assert rec('c', [5,'r',6,'c'], 4) == True
assert rec(2, [4,'z',8,3,2], 5) == True
assert rec(7, [4,9,8,'x',2], 5) == False

