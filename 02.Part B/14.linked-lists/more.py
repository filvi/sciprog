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

                        
    def occurrences(self, item):
        """ 
            Returns the number of occurrences of item in the list.

            - MUST execute in O(n) where n is the length of the list.
        """
        raise Exception('TODO IMPLEMENT ME !')
        
    def shrink(self):
        """ 
            Removes from this LinkedList all nodes at odd indeces (1, 3, 5, ...), 
            supposing that the first node has index zero, the second node 
            has index one, and so on. 
            
            So if the LinkedList is 
                'a','b','c','d','e' 
            a call to shrink() will transform the LinkedList into 
                'a','c','e'
            
            - MUST execute in O(n) where 'n' is the length of the list.
            - Does *not* return anything.
        """
        raise Exception('TODO IMPLEMENT ME !')

    def dup_first(self):
        """ Modifies this list by adding a duplicate of first node right after it. 
        
            For example, the list 'a','b','c' should become 'a','a','b','c'.            
            An empty list remains unmodified.            

            ** DOES NOT RETURN ANYTHING !!! **          

        """
        raise Exception('TODO IMPLEMENT ME !')
            
    def dup_all(self):
        """ Modifies this list by adding a duplicate of each node right after it.
        
            For example, the list 'a','b','c' should become 'a','a','b','b','c','c'.
            An empty list remains unmodified.      
            
            ** MUST PERFORM IN O(n) WHERE n is the length of the list. **
            
            ** DOES NOT RETURN ANYTHING !!! **
        """
        raise Exception('TODO IMPLEMENT ME !')

    def norep(self):
        """ MODIFIES this list by removing all the consecutive 
            repetitions from it.
            
            - MUST perform in O(n), where n is the list size.
        
            For example, after calling norep:

            'a','a','b','c','c','c'   will become  'a','b','c'
            
            'a','a','b','a'   will become   'a','b','a'            
            
        """
        raise Exception('TODO IMPLEMENT ME !')
                
    def find_couple(self,a,b):
        """ Search the list for the first two consecutive elements having data equal to 
            provided a and b, respectively. If such elements are found, the position
            of the first one is returned, otherwise raises LookupError.
            
            - MUST run in O(n), where n is the size of the list.
            - Returned index start from 0 included
            
        """
        raise Exception('TODO IMPLEMENT ME !')

    def swap (self, i, j):
        """
            Swap the data of nodes at index i and j. Indeces start from 0 included.
            If any of the indeces is out of bounds, rises IndexError.
            
            NOTE: You MUST implement this function with a single scan of the list.
            
        """
        raise Exception('TODO IMPLEMENT ME !')

    def gaps(self):
        """ Assuming all the data in the linked list is made by numbers,
            finds the gaps in the LinkedList and return them as a Python list.
            
            - we assume empty list and list of one element have zero gaps
            - MUST perform in O(n) where n is the length of the list

            NOTE: gaps to return are *indeces* , *not* data!!!!
        """
        raise Exception('TODO IMPLEMENT ME !')
        
    def flatv(self):
        """ See exercise text for explanation

            - MUST run in O(n) where n is the length of the list

        """
        raise Exception('TODO IMPLEMENT ME !')        
        
    def bubble_sort(self):
        """ Sorts in-place this linked list using the method of bubble sort

            - MUST execute in O(n^2) where n is the length of the linked list
        """
        raise Exception('TODO IMPLEMENT ME !')

    def merge(self,l2):
        """ Assumes this linkedlist and l2 linkedlist contain integer numbers
            sorted in ASCENDING order, and  RETURN a NEW LinkedList with
            all the numbers from this and l2 sorted in DESCENDING order

            IMPORTANT 1: *MUST* EXECUTE IN O(n1+n2) TIME where n1 and n2 are
                         the sizes of this and l2 linked_list, respectively

            IMPORTANT 2: *DO NOT* attempt to convert linked lists to
                         python lists!
        """
        raise Exception('TODO IMPLEMENT ME !')        
        
    def couple_sort(self):
        """MODIFIES the linked list by considering couples of nodes at even indexes
           and their successors: if a node data is lower than its successor data, swaps the nodes *data*.
           
           - ONLY swap *data*, DO NOT change node links.
           - if linked list has odd size, simply ignore the exceeding node.
           - MUST execute in O(n), where n is the size of the list
        """
        raise Exception('TODO IMPLEMENT ME !')
        
        
def mirror(lst):
    """ RETURN a NEW LinkedList having double the nodes of provided lst
        First nodes will have same elements of lst, following nodes will 
        have the same elements but in reversed order.
        
        For example:
            
            >>> mirror(['a'])
            LinkedList: a,a            
            
            >>> mirror(['a','b'])
            LinkedList: a,b,b,a

            >>> mirror(['a','c','b'])
            LinkedList: a,c,b,b,c,a
    
    """
    raise Exception('TODO IMPLEMENT ME !')

