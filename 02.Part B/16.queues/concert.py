DEBUG = True

def debug(msg):
    if DEBUG:
        print("DEBUG: ", msg.replace('\n', '\n' + (' '*8)))

from collections import deque

class Person:
    def __init__(self, name, group, ticket):
        self.name = name
        self.group = group
        self.ticket = ticket

    def __str__(self):
        return "Person(%s,%s,%s)" % (self.name, self.group, self.ticket)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        
        return self.name == other.name and self.group == other.group and self.ticket == other.ticket
        
class Concert:

    def __init__(self):
        self._cash = deque()
        self._entrance = deque()

    def enqc(self, person):        
        """ Enqueues at the cash from the right """

        self._cash.append(person)
        
    def enqe(self, person):
        """ Enqueues at the entrance from the right """

        self._entrance.append(person)
    
    def __str__(self):
        return "Concert: \n      cash: " \
            + str(self._cash).replace('), Person','),\n                   Person') \
            + "\n  entrance: " \
            + str(self._entrance).replace('), Person','),\n                   Person')

    def __repr__(self):
        return self.__str__()

    def dequeue(self):
        """ RETURN the names of people admitted to concert  

            Dequeuing for the whole queue system is done in groups, that is, 
            with a _single_ call to dequeue, these steps happen, in order:

            1. entrance queue: all people belonging to the same group at 
               the front of entrance queue who have the ticket exit the queue 
               and are admitted to concert. People in the group without the 
               ticket are sent to cash.
            2. cash queue: all people belonging to the same group at the front 
               of cash queue are given a ticket, and are queued at the entrance queue

        """
        raise Exception('TODO IMPLEMENT ME !') 