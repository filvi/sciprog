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
        

        if self._head == None or self._head.get_next() == None:
            return
        else:
            current = self._head
            while current != None:
                if current.get_next() != None and current.get_next().get_next() == None:
                    removed = current.get_next()
                    self._last = current
                    current.set_next(None)                    
                    removed.set_next(self._head)
                    self._head = removed
                    return

                current = current.get_next()
        

    
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
        
        
        if k < 0:
            raise ValueError
        
        if self._size > 1:
            m = k % self._size

            if m > 0 and m < self._size:
                current = self._head
                for i in range(self._size - m - 1):
                    current = current.get_next()
                chain_b = current.get_next()
                old_head = self._head
                old_last = self._last
                self._last = current
                self._last.set_next(None)
                self._head = chain_b
                old_last.set_next(old_head)

        
        

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
        

        if self._last == None:
            self.add(1)
        
        else:
            if self._last.get_data() < 9:
                self._last.set_data(self._last.get_data() + 1)
                return
            else:

                inc_node = None
                current = self._head                
                
                while current != None:
                    if current.get_data() < 9:
                        inc_node = current

                    current = current.get_next()
                
                if inc_node == None:
                    self.add(0)
                    inc_node = self._head
                
                inc_node.set_data(inc_node.get_data() + 1)
                current = inc_node.get_next()
                while current != None:
                    current.set_data(0)
                    current = current.get_next()
            
        
                
