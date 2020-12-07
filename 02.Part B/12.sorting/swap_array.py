
class SwapArray:
    """ A sequence of elements that can only be modified by swapping one element 
        with the successive one.
    """
    
    def __init__(self, python_list):
        """ Initializes the SwapArray with the elements found in python_list. """
        
        self._arr = python_list[:]  # we store a _copy_ of the array
        
    def swap_next(self, i):
        """ Swaps the elements at indeces i and i + 1
        
            If index is negative or greater or equal of the last index, raises 
            an IndexError
        
        """
        if i < 0 or i >= len(self._arr) - 1:
            raise IndexError("Wrong index: " + str(i) )

        tmp = self._arr[i]
        self._arr[i] = self._arr[i + 1]
        self._arr[i + 1] = tmp

    def size(self):
        """ Returns the size of the SwapArray """
        return len(self._arr)
        
    def get(self, i):
        """ Returns the element at index i.
        
            If index is outside the bounds of the array, raises an IndexError        
        """
        return self._arr[i]
        
    def get_last(self):
        """ Returns the last element of the array
                    
            If array is empty, raises an IndexError                            
        """
        
        return self._arr[-1]
    
    def __str__(self):
        return "SwapArray: " + str(self._arr)
        
def is_sorted(sarr):  
    """ Returns True if the provided SwapArray sarr is sorted, False otherwise
    
        NOTE: Here you are a user of SwapArray, so you *MUST NOT* access
              directly the field _arr.
        NOTE: MUST run in O(n) where n is the length of the array
    """
    raise Exception('TODO IMPLEMENT ME !')  
        
def max_to_right(sarr,i):
    """ Modifies the provided SwapArray sarr so that its biggest element
        in the subarray from 0 to i is moved at index i.
        Elements *after* i are *not* considered.
        
        The order in which the other elements will be after a call
        to this function is left unspecified (so it could be any).
        
        NOTE: Here you are a user of SwapArray, so you *MUST NOT* access
              directly the field _arr. To do changes, you can only use 
              the method swap_next(self, i).   
        NOTE: does *not* return anything!  
        NOTE: MUST run in O(n) where n is the length of the array
                     
    """
    raise Exception('TODO IMPLEMENT ME !')


def swapsort(sarr):
    """ Sorts in-place provided SwapArray. To implement it, you can use 
        previously defined functions. 

        NOTE: Here you are a user of SwapArray, so you *MUST NOT* access
              directly the field _arr. To do changes, you can only use 
              the method swap_next(self, i).      
        NOTE: does *not* return anything! 
        NOTE: MUST execute in O(n^2), where n is the length of the array
    """
    raise Exception('TODO IMPLEMENT ME !')