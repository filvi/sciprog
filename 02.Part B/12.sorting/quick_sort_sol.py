import unittest


def swap(A, x, y):
    """
        MODIFIES the array A by swapping the elements at indeces x and y
    """
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def pivot(A, first, last):
    """ MODIFIES in-place the slice of the array A with indeces between first included
        and last included. RETURN the new pivot index.
        
    """
    
    p = A[first]
    j = first
    for i in range(first + 1, last + 1):
        if A[i] < p:
            j += 1
            swap(A, i, j)
    A[first] = A[j]
    A[j] = p
    return j
    
    
def quicksort(A, first, last):
    """
        Sorts in-place the slice of the array A with indeces between first included
        and last included.
    """
    
    if first < last:
        j = pivot(A, first, last)
        quicksort(A, first, j - 1)
        quicksort(A, j + 1, last)
    

def qs(A):
    """
        Sorts in-place the array A by calling quicksort function on the full array.
    """
    
    if len(A) > 0:
        quicksort(A, 0, len(A) - 1)
    