

class MultiSet:
    """ A multiset (or bag) generalizes a set by allowing multiple instances of the multiset's elements. 

    The multiplicity of an element is the number of instances of the element in a specific multiset.

    For example:

        The multiset "a, b"  contains only elements 'a' and 'b', each having multiplicity 1
        In multiset "a, a, b",  'a' has multiplicity 2 and 'b' has multiplicity 1
        In multiset "a, a, a, b, b, b", 'a' and 'b' both have multiplicity 3
    
    Notice order of insertion does not matter, so "a, a, b" and "a, b, a" are the same multiset,
    where 'a' has multiplicity 2 and 'b' has multiplicity 1.


    """
    
    def __init__(self):
        """ Initializes the MultiSet as empty."""
        raise Exception('TODO IMPLEMENT ME !')
    
    def add(self, el):
        """ Adds one instance of element el to the multiset 

            NOTE: MUST work in O(1)        
        """
        raise Exception('TODO IMPLEMENT ME !')
        
    def get(self, el):
        """ RETURN the multiplicity of element el in the multiset. 
            
            - If no instance of el is present, return 0.

            NOTE: MUST work in O(1)        
        """
        raise Exception('TODO IMPLEMENT ME !')

    def removen(self, el, n):
        """ Removes n instances of element el from the multiset (that is, reduces el multiplicity by n)
            
            If n is negative, raises ValueError.            
            If n represents a multiplicity bigger than el current multiplicity, raises LookupError
            
            NOTE: multiset multiplicities are never negative
            NOTE: MUST work in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')