import unittest

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
        This is a stripped down version of the LinkedList seen in the lab
        
    """
        
    def __init__(self):
        self._head = None

        
    def __str__(self):
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str(current.get_data()))            
            current = current.get_next()            
        
        return "LinkedList: " + ",".join(strings)
        
        
    def add(self,item):    
        """ Adds item at the beginning of the list """
        
        new_head = Node(item)
        new_head.set_next(self._head)
        self._head = new_head

    def remove(self, item):
        """ Removes first occurrence of item from the list
        
            - If item is not found, raises a LookupError.
        """
        current = self._head        
        prev = None
        
        while (current != None):
            if (current.get_data() == item):
                if prev == None:  # we need to remove the head 
                    self._head = current.get_next()
                else:  
                    prev.set_next(current.get_next())
                    current = current.get_next()                    
                return  # Found, exits the function
            else:
                prev = current
                current = current.get_next() 
        
        raise LookupError("Tried to remove a non existing item! Item was: " + str(item))

            
    
    def rev(self):
        """ Returns a *new* LinkedList, which is the reversed version of this one.

            Function must run in O(n), and try to make this function as fast as possible,
            without using python lists or extra fields.                    
        """
        raise Exception('TODO IMPLEMENT ME !')
        
    def clone(self):
        """ Return a *copy* of this LinkedList
        
            NOTE: since we are making a copy, the output of this function 
            won't contain any Node instance from the original list. Still, new Node 
            instances will point to the same data items of the original list        
            
             in O(n)
        """
        raise Exception('TODO IMPLEMENT ME !')
        
        
    

    def slice(self, start, end):
        """ RETURN a NEW LinkedList created by copying nodes of this list
            from index start INCLUDED to index end EXCLUDED

            - if start is greater or equal than end, returns an empty LinkedList
            - if start is greater than available nodes, returns an empty LinkedList
            - if end is greater than the available nodes, copies all items until the tail without errors
            - if start index is negative, raises ValueError
            - if end index is negative, raises ValueError            

            - IMPORTANT: All nodes in the returned LinkedList MUST be NEW
            - DO *NOT* modify original linked list
            - DO *NOT* add an extra size field
            - MUST execute in O(n), where n is the size of the list
            
        """
        raise Exception('TODO IMPLEMENT ME !')