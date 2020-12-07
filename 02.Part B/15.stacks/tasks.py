
DEBUG = True

def debug(msg):
    if DEBUG:
        print("DEBUG: ", str(msg).replace('\n', '\n' + (' '*8)))


class Stack:
    """ A simple Stack supporting push, pop, and is_empty operations
    """

    def __init__(self):
        """ Creates a Stack.
        
        """        
        self._elements = []
        
    def size(self):
        return len(self._elements)
        
    def is_empty(self):
        return len(self._elements) == 0


    def pop(self):
        """ Removes the element at the top of the stack and returns it.
            
            If the stack is empty, raises an IndexError
        """
        if (self.is_empty()):
            raise IndexError("Stack is empty!")
              
        return self._elements.pop()                
        
    def push(self, item):        
        """ Inserts a task in the stack                      
        """   
        self._elements.append(item)
            
    def __str__(self):
        return "Stack:  " + " elements=" + str(self._elements) 

def do(task, subtasks):
    """ Takes a task to perform and a dictionary of subtasks, 
        and RETURN a list of performed tasks
         
        - To implement it, use a Stack and a while cycle. 
        - DO *NOT* use a recursive function
        - Inside the function, you can use a print like "I'm doing task a', 
          but that is only to help yourself in debugging, only the
          list returned by the function will be considered in the evaluation!
    """
    raise Exception('TODO IMPLEMENT ME !')


def do_level(task, subtasks):
    """ Takes a task to perform and a dictionary of subtasks, 
        and RETURN a list of performed tasks as tuples (task label, level)
         
        - To implement it, use a Stack and a while cycle
        - DO *NOT* use a recursive function
        - Inside the function, you can use a print like "I'm doing task a', 
          but that is only to help yourself in debugging, only the
          list returned by the function will be considered in the evaluation
    """
    raise Exception('TODO IMPLEMENT ME !')

