class Node:
    """ A Node of an LinkedList. Holds data provided by the user. """
    
    def __init__(self,initdata):
        self._data = initdata
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self,newdata):
        self._data = newdata

    def set_next(self,newnext):
        self._next = newnext


class LinkedList:
    """
        LinkedList v1 - slow basic LinkedList
        
        This class is similar to 'UnorderedList' in the book, with these differences:
            - has more pythonic names
            - tries to mimic more closely the behaviour of default Python list, raising exceptions on 
              boundary conditions like removing non exisiting elements.
    """
        
    def __init__(self):
        self._head = None
        
    def __str__(self):
        """ For potentially complex data structures like this one, having a __str__ method is essential to 
            quickly inspect the data by printing it. 
        """
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str(current.get_data()))            
            current = current.get_next()            
        
        return "LinkedList: " + ",".join(strings)
        
        
    def is_empty(self):
        """ Return True if the list is empty, False otherwise
        
            - MUST execute in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')

    def add(self,item):            
        """ Adds item at the beginning of the list 
        
            - MUST execute in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')

    def size(self):
        """ Returns the size of the list         
        """
        raise Exception('TODO IMPLEMENT ME !')

    def search(self,item):
        """ Returns True if item is present in list, False otherwise              
        """
        raise Exception('TODO IMPLEMENT ME !')


    def append(self, e):
        """ Appends element e to the end of the list.           
        """                
        raise Exception('TODO IMPLEMENT ME !')

    def index(self, e):
        """ Return the index in the list of the first item whose value is x. 
        
            - If item is not found, raises a LookupError.
        """
        raise Exception('TODO IMPLEMENT ME !')
        
        
    def pop(self):
        """ Remove the last item of the list, and return it. 
            
            - If the list is empty, ValueError is raised. 
        """
        raise Exception('TODO IMPLEMENT ME !')

        
    def remove(self, item):
        """ Removes first occurrence of item from the list
        
            If item is not found, raises an LookupError.                        
        """
        raise Exception('TODO IMPLEMENT ME !')
        
    def insert(self, i, e):
        """ Insert an item at a given position. 

            The first argument is the index of the element before which to insert, 
            so list.insert(0, e) inserts at the front of the list, and 
            list.insert(list.size(), e) is equivalent to list.append(e).
            
            - If i is negative or i > list.size(), raises an IndexError (default Python list
              appends instead to the end :-/ )           
        """    
        raise Exception('TODO IMPLEMENT ME !')
        
        
                