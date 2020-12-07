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
    raise Exception('TODO IMPLEMENT ME !')
    
def quicksort(A, first, last):
    """
        Sorts in-place the slice of the array A with indeces between first included
        and last included.
    """
    raise Exception('TODO IMPLEMENT ME !')

def qs(A):
    """
        Sorts in-place the array A by calling quicksort function on the full array.
    """
    raise Exception('TODO IMPLEMENT ME !')