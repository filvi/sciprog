from linked_chal import *
import unittest


def to_py(linked_list):
    """ Returns linked_list as a regular Python list - very handy for testing.
    """
    python_list = []
    current = linked_list._head        
    
    while (current != None):
        python_list.append(current.get_data())
        current = current.get_next()                       
    return python_list    

def to_ll(python_list):
    """ Creates a LinkedList from a regular Python list - very handy for testing.
    """
    ret = LinkedList()
    
    for el in reversed(python_list):
        ret.add(el)
    return ret


        
    
class RShiftTest(unittest.TestCase):
    
    def test_01_empty(self):
        ll = LinkedList()
        with self.assertRaises(ValueError):
            ll.rshift('z')
            
    def test_02_a_b(self):
        ll = LinkedList()
        ll.add('a')
        self.assertEqual('a', ll.rshift('b'))
        self.assertEqual(to_py(ll), ['b'])
        self.assertEqual('b', ll.rshift('c'))
        self.assertEqual(to_py(ll), ['c'])

    def test_03_ab_cd(self):
        ll = LinkedList()
        ll.add('a')
        ll.add('b')
        self.assertEqual('a', ll.rshift('c'))
        self.assertEqual(to_py(ll), ['c','b'])
        self.assertEqual('b', ll.rshift('d'))
        self.assertEqual(to_py(ll), ['d','c'])
        

    def test_04_complex(self):
        ll = LinkedList()
        ll.add('a')
        ll.add('d')
        ll.add('a')
        ll.add('c')
        ll.add('b')
        ll.add('d')        
        ll.add('e')
        self.assertEqual('a', ll.rshift('p'))
        self.assertEqual(to_py(ll), ['p','e','d','b','c','a','d'])
        self.assertEqual('d', ll.rshift('q'))
        self.assertEqual(to_py(ll), ['q','p','e','d','b','c','a'])
        self.assertEqual('a', ll.rshift('r'))
        self.assertEqual('c', ll.rshift('s'))
        self.assertEqual('b', ll.rshift('t'))
        self.assertEqual('d', ll.rshift('u'))
        self.assertEqual('e', ll.rshift('v'))
        self.assertEqual('p', ll.rshift('z'))       
        
        
class LShiftTest(unittest.TestCase):
    
    def test_01_empty(self):
        ll = LinkedList()
        with self.assertRaises(ValueError):
            ll.lshift('z')
            
    def test_02_a_b(self):
        ll = LinkedList()
        ll.add('a')
        self.assertEqual('a', ll.lshift('b'))
        self.assertEqual(to_py(ll), ['b'])
        self.assertEqual('b', ll.lshift('c'))
        self.assertEqual(to_py(ll), ['c'])

    def test_03_ab_cd(self):
        ll = LinkedList()
        ll.add('a')
        ll.add('b')
        self.assertEqual('b', ll.lshift('c'))
        self.assertEqual(to_py(ll), ['a','c'])
        self.assertEqual('a', ll.lshift('d'))
        self.assertEqual(to_py(ll), ['c','d'])
        

    def test_04_complex(self):
        ll = LinkedList()
        ll.add('a')
        ll.add('d')
        ll.add('a')
        ll.add('c')
        ll.add('b')
        ll.add('d')        
        ll.add('e')
        self.assertEqual('e', ll.lshift('p'))
        self.assertEqual(to_py(ll), ['d','b','c','a','d','a','p'])
        self.assertEqual('d', ll.lshift('q'))
        self.assertEqual(to_py(ll), ['b','c','a','d','a','p','q'])
        self.assertEqual('b', ll.lshift('r'))
        self.assertEqual('c', ll.lshift('s'))
        self.assertEqual('a', ll.lshift('t'))
        self.assertEqual('d', ll.lshift('u'))
        self.assertEqual('a', ll.lshift('v'))
        self.assertEqual('p', ll.lshift('z'))               
