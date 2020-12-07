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
        This is a stripped down version of the LinkedList as previously seen.
        Note it also holds _size and _last attributes.
        
    """
        
    def __init__(self):
        self._head = None
        self._last = None
        self._size = 0

        
    def __str__(self):
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str(current.get_data()))            
            current = current.get_next()            
        
        return "LinkedList: " + ",".join(strings)
        
    def size(self):
        """ Returns the size of the list in O(1) """
        return self._size  

    def is_empty(self):
        return self._head == None


    def last(self):
        """ Returns the last element in the list, in O(1). 
        
            - If list is empty, raises ValueError. Since v2. 
        """
        
        if (self._head == None):
            raise ValueError("Tried to get the last element of an empty list!")
        else:    
            return self._last.get_data()
        
    def add(self,item):    
        """ Adds item at the beginning of the list """

        new_head = Node(item)
        new_head.set_next(self._head)
        if self._last == None:
            self._last = new_head
        self._head = new_head
        self._size += 1

                        
    def rotate(self):
        """ Rotate the list of 1 element, that is, removes last node and
            inserts it as the first one

           - MUST execute in O(n) where n is the length of the list
           - Remember to also update _last pointer
           - WARNING: DO *NOT* try to convert whole linked list to a python list
           - WARNING: DO *NOT* swap node data or create nodes, I want you to
                      change existing node links !!
        """
        raise Exception('TODO IMPLEMENT ME !')

    
    def rotaten(self, k):
        """ Rotate k times the linkedlist
        
            - k can range from 0 to any positive integer number (even greater than list size)
            - if k < 0 raise ValueError
        
            - MUST execute in O( (n-k)%n ) where n is the length of the list
            - WARNING: DO *NOT* call .rotate() k times !!!!
            - WARNING: DO *NOT* try to convert whole linked list to a python list
            - WARNING: DO *NOT* swap node data or create nodes, I want you to
                       change existing node links !!
        """
        raise Exception('TODO IMPLEMENT ME !')
        

    def plus_one(self):
        """ MODIFIES the digi list by summing one to the integer number it represents                    
            - you are allowed to perform multiple scans of the linked list
            - remember the list has a _last pointer
            
            - MUST execute in O(N) where N is the size of the list          
            - DO *NOT* create new nodes EXCEPT for special cases:
                a. empty list ( [] -> [1] )
                b. all nines ( [9,9,9] -> [1,0,0,0] )                     
            - DO *NOT* convert the digi list to a python int            
            - DO *NOT* convert the digi list to a python list            
            - DO *NOT* reverse the digi list            
        """
        raise Exception('TODO IMPLEMENT ME !')
                
