import math
        
class WStack:
    """ A simple stack made only of integer numbers. 
        Can provide quickly the total sum of such numbers with .weight method
    """
    def __init__(self):
        """ Creates a WStack which contains only integers
    
        """
        self._elements = []         
        raise Exception('TODO IMPLEMENT ME !')

    def weight(self):
        """ RETURN the total weight of the stack

            - MUST run in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')

    def size(self):
        """ RETURN the size of the stack

            - Must run in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')
    
    def __str__(self):
        """ Return a string like  
        
                WStack: weight=7 elements=['5', '2']
        """

        raise Exception('TODO IMPLEMENT ME !')


    def is_empty(self):
        """ RETURN True if the stack empty, False otherwise

            - Must run in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')


    def push(self, new_item):
        """ Adds new_item to the top of the stack                        
            
            - Must run in O(1)
            - if item is not an int, raises ValueError
        """        
        raise Exception('TODO IMPLEMENT ME !')

    def peek(self):
        """ RETURN the top element in the stack (without removing it!)
            
            - if stack is empty, raise IndexError
            - Must run in O(1)  

        """
        raise Exception('TODO IMPLEMENT ME !')

    def pop(self):
        """ Removes the top element in the stack and RETURN it.

            - if stack is empty, raise IndexError            
            - Must run in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')



def accumulate(stack1, stack2, min_amount):
    """ Pushes on stack2 elements taken from stack1 until the weight of
        stack2 is equal or exceeds the given min_amount

        - if the given min_amount cannot possibly be reached because 
          stack1 has not enough weight, raises early ValueError without 
          changing stack1.
        - DO NOT access internal fields of stacks, only use class methods.
        - MUST perform in O(n) where n is the size of stack1
        - NOTE: this function is defined *outside* the class !
    """
    raise Exception('TODO IMPLEMENT ME !')
    


