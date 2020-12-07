
class BinaryTree:
    """ A simple binary tree with left and right branches
    """
    
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def data(self):
        return self._data    
    
    def left(self):
        return self._left    
    
    def right(self):
        return self._right
                    
    def __str__(self):
        """ Returns a pretty string of the tree """
        def str_branches(node, branches):
            """ Returns a string with the tree pretty printed. 

                branches: a list of characters representing the parent branches. Characters can be either ` ` or '│'            
            """
            strings = [str(node._data)]

            i = 0           
            if node._left != None or node._right != None:
                for current in [node._left, node._right]:
                    if i == 0:            
                        joint = '├'
                    else:
                        joint = '└' 

                    strings.append('\n')
                    for b in branches:
                        strings.append(b)
                    strings.append(joint)
                    if i == 0:
                        branches.append('│')                    
                    else:
                        branches.append(' ')

                    if current != None:                
                        strings.append(str_branches(current, branches))
                    branches.pop()                
                    i += 1
            return "".join(strings)
        
        return str_branches(self, [])


    def insert_left(self, data):
        """ Takes as input DATA (*NOT* a node !!) and MODIFIES current node this way:
        
            - First creates a new BinaryTree (let's call it B) into which provided data is wrapped.
            - Then:
                - if there is no left node in self, new node B is attached to the left of self
                - if there already is a left node L, it is substituted by new node B, and L becomes the 
                  left node of B
        """
        raise Exception('TODO IMPLEMENT ME !')

    def insert_right(self, data):
        """ Takes as input DATA (*NOT* a node !!) and MODIFIES current node this way:
        
            - First creates a new BinaryTree (let's call it B) into which provided data is wrapped.
            - Then:
                - if there is no right node in self, new node B is attached to the right of self
                - if there already is a right node L, it is substituted by new node B, and L becomes the 
                  right node of B
        """
        raise Exception('TODO IMPLEMENT ME !')

    def sum_rec(self):
        """ Supposing the tree holds integer numbers in all nodes,
            RETURN the sum of the numbers.

            - implement it as a recursive Depth First Search (DFS) traversal
              NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind            
        """ 
   
        raise Exception('TODO IMPLEMENT ME !')      

    def height_rec(self):
        """ RETURN an integer which is the height of the tree

            - implement it as recursive call which does NOT modify the tree
              NOTE: with big trees a recursive solution would surely exceed the call stack,
                    but here we don't mind
            - A tree with only one node has height zero.
            
        """
        raise Exception('TODO IMPLEMENT ME !')
    
    
    

    def depth_rec(self, level):
        """ MODIFIES the tree by putting in the data field the provided value level (which is an integer),
            and recursively calls itself on left and right nodes (if present)  passing level + 1
            
            - implement it as a recursive Depth First Search (DFS) traversal
              NOTE: with big trees a recursive solution would surely exceed the call stack,
                    but here we don't mind
            - The root of a tree has depth zero.
            - does not return anything            
        """
        raise Exception('TODO IMPLEMENT ME !')        

    def contains_rec(self, item):
        """ RETURN True if at least one node in the tree has data equal to item, otherwise RETURN False.

            - implement it as a recursive Depth First Search (DFS) traversal
              NOTE: with big trees a recursive solution would surely exceed the call stack,
                    but here we don't mind            
        """        
        raise Exception('TODO IMPLEMENT ME !')


  

    def join_rec(self):
        """ Supposing the tree nodes hold a character each, RETURN a STRING holding 
            all characters with a IN-ORDER visit

            - implement it as a recursive Depth First Search (DFS) traversal
              NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind            
        """ 
   
        raise Exception('TODO IMPLEMENT ME !')        


    def fun_rec(self):
        """ Supposing the tree nodes hold expressions which can either be
            functions or single variables, RETURN a STRING holding 
            the complete formula with needed parenthesis

            - implement it as a recursive Depth First Search (DFS)
              PRE-ORDER visit
            - NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind            
        """ 
   
        raise Exception('TODO IMPLEMENT ME !')        

    def bin_search_rec(self, m):
        """ Assuming the tree is a binary search tree of integer numbers, 
            RETURN True if m is present in the tree, False otherwise
        
            - MUST EXECUTE IN O(height(t))
            - NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind
        """
        raise Exception('TODO IMPLEMENT ME !')

    def bin_insert_rec(self, m):
        """ Assuming the tree is a binary search tree of integer numbers, 
            MODIFIES the tree by inserting a new node with the value m
            in the appropriate position. Node is always added as a leaf.

            - MUST EXECUTE IN O(height(t))
            - NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind
        """
        raise Exception('TODO IMPLEMENT ME !')

    def univalued_rec(self):
        """ RETURN True if the tree is univalued, otherwise RETURN False. 

            - a tree is univalued when all nodes have the same value as data
            - MUST execute in O(n) where n is the number of nodes of the tree
            - NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind
        """
        raise Exception('TODO IMPLEMENT ME !')

    def same_rec(self, other):
        """ RETURN True if this binary tree is equal to other binary tree,
            otherwise return False.
            
            - MUST execute in O(n) where n is the number of nodes of the tree
            - NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind
            - HINT: defining a helper function 
                    
                    def helper(t1, t2):

                    which recursively calls itself and assumes both of the
                    inputs can be None may reduce the number of ifs to write.
        """
        raise Exception('TODO IMPLEMENT ME !')
        
    def sum_leaves_rec(self):
        """ Supposing the tree holds integer numbers in all nodes,
            RETURN the sum of ONLY the numbers in the leaves.

            - a root with no children is considered a leaf
            - implement it as a recursive Depth First Search (DFS) traversal
              NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind            
        """ 
   
        raise Exception('TODO IMPLEMENT ME !')                  
        
         

    def schedule_rec(self):
        """ RETURN a list of task labels in the order they will be completed.

            - Implement it with recursive calls.
            - MUST run in O(n) where n is the size of the tree
            
            NOTE: with big trees a recursive solution would surely
                  exceed the call stack, but here we don't mind
        """
        raise Exception('TODO IMPLEMENT ME !')
           
    
    def paths_slow_rec(self):
        """ RETURN a list of all paths from this node to the each leaf.
            A path is a list which holds the nodes data found while traversing the tree.
                                    
            - for this slow version, you can only use + operator or .extend() method
              which will bring an O(n^3) complexity
            - implement it as recursive call 
              NOTE: with big trees a recursive solution would surely exceed the call stack,
                    but here we don't mind                          
        """        
        raise Exception('TODO IMPLEMENT ME !')    
    
    def _paths_fast_helper(self):
        """ DO NOT use + operator nor .extend() method         
        """
        raise Exception('TODO IMPLEMENT ME !')
                        
    def paths_fast_rec(self):
        """ RETURN a list of all paths from this node to the each leaf.
            A path is a list which holds the nodes data found while traversing the tree.
                        
            - DO NOT use + operator nor .extend() method 
            - MUST work in O(n^2) where n is the number of nodes in the tree
            - implement it as recursive call 
              NOTE: with big trees a recursive solution would surely exceed the call stack,
                    but here we don't mind                          
        """        
        raise Exception('TODO IMPLEMENT ME !')
        

    def sum_stack(self):
        """ Supposing the tree holds integer numbers in all nodes,
            RETURN the sum of the numbers.
            
            - DO *NOT* use recursion
            - implement it with a while and a stack (as a python list)
            - In the stack place nodes to process
        """ 
   
        raise Exception('TODO IMPLEMENT ME !')      


    def height_stack(self):
        """ RETURN an integer which is the height of the tree

            - A tree with only one node has height zero.
            - DO *NOT* use recursion
            - implement it with a while and a stack (as a python list). 
            - In the stack place *tuples* holding a node *and* its level
            
        """
   
        raise Exception('TODO IMPLEMENT ME !')      
        
    def leaves_stack(self):
        """ RETURN a list holding the *data* of all the leaves  of the tree,
            in left to right order.
            - a root with no children is considered a leaf

            - DO *NOT* use recursion
            - implement it with a while and a stack (as a python list)            
        """        
        raise Exception('TODO IMPLEMENT ME !')      
        
    def add_row(self, elems):
        """ Takes as input a list of data and MODIFIES the tree by adding
            a row of new leaves, each having as data one element of elems,
            in order.
            
            - elems size can be less than 2*|leaves|
            - if elems size is more than 2*|leaves|, raises ValueError
            - for simplicity, you can assume assume self is a perfect 
              binary tree, that is a binary tree in which all interior nodes 
              have two children and all leaves have the same depth
            - MUST execute in O(n+|elems|)  where n is the size of the tree
            - DO *NOT* use recursion
            - implement it with a while and a stack (as a Python list)
        """         raise Exception('TODO IMPLEMENT ME !')   
        
    def prune_rec(self, el):
        """ MODIFIES the tree by cutting all the subtrees that have their 
            root node data equal to el. By 'cutting' we mean they are no longer linked 
            by the tree on which prune is called.

            - if prune is called on a node having data equal to el, raises ValueError
            
            - MUST execute in O(n) where n is the number of nodes of the tree
            - NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind            
        """
        raise Exception('TODO IMPLEMENT ME !')