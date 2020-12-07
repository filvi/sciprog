DEBUG = True

def debug(msg):
    if DEBUG:
        print("DEBUG: ", str(msg).replace('\n', '\n' + (' '*8)))

class Backpack:
    
    def __init__(self, max_weight):
        """ Creates a Backpack with given max_weight.

            - if max_weight is negative, raises ValueError
        """
        if max_weight < 0:
            raise ValueError("Expected a non-zero weight, got instead: %s "  % max_weight)
        self._elements = []
        self._max_weight = max_weight
        raise Exception('TODO IMPLEMENT ME !')

    def size(self):
        """ RETURN the number of items in the backpack

            - MUST run in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')
    
    def max_weight(self):
        """ Return the maximum allowed weight
        """
        return self._max_weight

    def weight(self):
        """  Return the backpack total current weight

             ************  MUST RUN IN O(1)  ***************
        """
        raise Exception('TODO IMPLEMENT ME !')

    def is_empty(self):
        """ RETURN True if the backpack empty, False otherwise

            - MUST run in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')

    def __str__(self):
        """ Return a string like  
        
                Backpack: weight=8 max_weight=10 elements=[('a',5), ('b',3)]
        """
        raise Exception('TODO IMPLEMENT ME !')


    def peek(self):
        """ RETURN the top element in the stack (without removing it!)
            
            - if stack is empty, raise IndexError
            - Must run in O(1)  

        """
        raise Exception('TODO IMPLEMENT ME !')


    def push(self, item, w):
        """ Adds item of weight w on the top of the backpack.
            
            - if w is negative, raises ValueError
            - if w is heavier than topmost item, raises ValueError
            - if max_weight is exceeded, raises ValueError
            - MUST run in O(1)
            
        """
        raise Exception('TODO IMPLEMENT ME !')

    def pop(self):
        """ Removes the top element in the backpack and RETURN it
            as a tuple (element_id, weight) like ('a', 3)

            - if backpack is empty, raise IndexError
            - MUST run in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')


# NOTE: this function is implemented *outside* the class !

def remove(backpack, el):
    """
        Remove topmost occurrence of el found in the backpack, 
        and RETURN it (as a tuple name, weight)
        
        - if el is not found, raises ValueError        

        - DO *NOT* ACCESS DIRECTLY FIELDS OF BACKPACK !!!
          Instead, just call methods of the class!

        - MUST perform in O(n), where n is the backpack size

        - HINT: To remove el, you need to call Backpack.pop() until
                the top element is what you are looking for. You need 
                to save somewhere the popped items except the one to 
                remove, and  then push them back again.
    
    """
    raise Exception('TODO IMPLEMENT ME !')

