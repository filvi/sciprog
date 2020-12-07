       
class CappedStack:
    
    def __init__(self, cap):
        """ Creates a CappedStack capped at provided cap. 
        
            - if cap <= 0, throws a ValueError
        """
        raise Exception('TODO IMPLEMENT ME !')

    def cap(self):
        """ RETURN the cap of the stack 

            - Must run in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')

    def size(self):
        """ RETURN the size of the stack

            - Must run in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')
    
    def __str__(self):
        """ Return a string like  
        
                CappedStack: cap=4 elements=['a', 'b']
        """

        raise Exception('TODO IMPLEMENT ME !')


    def is_empty(self):
        """ RETURN True if the stack empty, False otherwise

            - MUST run in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')


    def push(self, new_item):
        """ Adds item to the top of the stack, if current size is within cap.
            
            - If stack size is already at cap value, new item is silently discarded
            
            - MUST run in O(1)
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


    def peekn(self, n):
        """
            RETURN a list with the n top elements, in the order in which they
            were pushed. For example, if the stack is the following: 
            
                e
                d
                c
                b
                a
                
            peekn(3) will return the list ['c','d','e']

            - If there aren't enough element to peek, raises IndexError
            - If n is negative, raises an IndexError
        """
        raise Exception('TODO IMPLEMENT ME !')

    def popn(self, n):
        """ Pops the top n elements, and RETURN them as a list, in the order in 
            which they where pushed. For example, with the following stack:
            
                e
                d
                c
                b
                a
            
            popn(3)
            
            will give back ['c','d','e'], and stack will become:
            
                b
                a
            
            - If there aren't enough element to pop, raises an IndexError
            - If n is negative, raises an IndexError
        """
        raise Exception('TODO IMPLEMENT ME !')

    def set_cap(self, cap):
        """ MODIFIES the cap setting its value to the provided cap. 
        
            If the cap is less then the stack size, all the elements above 
            the cap are removed from the stack.
            
            If cap < 1, raises an IndexError
            Does *not* return anything!
        
            For example, with the following stack, and cap at position 7:
            
            cap ->  7
                    6
                    5  e
                    4  d
                    3  c
                    2  b
                    1  a
                    
            
            calling method set_cap(3) will change the stack to this:
            
            cap ->  3  c
                    2  b
                    1  a                                
            
        """
        raise Exception('TODO IMPLEMENT ME !')
        
