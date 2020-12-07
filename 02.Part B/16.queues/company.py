
from collections import deque

DEBUG = True

def debug(msg):
    if DEBUG:
        print("DEBUG: %s" % str(msg))

class Company:

    def __init__(self):
        self._employees = []   # a list of dictionaries


    def __str__(self):
        """
            name  rank  tasks
              x    9:    []
              y    6:    []
              z    2:    []
        """
        import textwrap

        f = '  %-6s%-6s%-6s'
        s = textwrap.dedent("""
                                Company:
                                """ + f % ("name","rank","tasks") + "\n")

        for i in range(len(self._employees)):
            e = self._employees[i]
            s +=  f % (e['name'], e['rank'], str(e['tasks'])) + "\n"

        return s
    
    def __repr__(self):
        return self.__str__()


    def add_employee(self, name, rank):
        """
            Adds employee with name and rank to the company, maintaining 
            the _employees list sorted by rank (higher rank comes first)

            Represent the employee as a dictionary with keys 'name', 'rank' 
            and 'tasks' (a Python deque)

            - here we don't mind about complexity, feel free to use a linear scan and .insert 
            - If an employee of the same rank already exists, raise ValueError
            - if an employee of the same name already exists, raise ValueError
        """   
        raise Exception('TODO IMPLEMENT ME !')

    def add_task(self, task_name, task_rank, employee_name):
        """ Append the task as a (name, rank) tuple to the tasks of 
            given employee

            - If employee does not exist, raise ValueError
        """
        raise Exception('TODO IMPLEMENT ME !')

    def work(self):
        """ Performs a work step and RETURN a list of performed task names.

            For each employee, dequeue its current task from the left and:
            - if the task rank is greater than the rank of the
            current employee, append the task to his supervisor queue 
            (the highest ranking employee must execute the task)
            - if the task rank is lower or equal to the rank of the
            next lower ranking employee, append the task to that employee queue
            - otherwise, add the task name to the list of
              performed tasks to return
        """
        raise Exception('TODO IMPLEMENT ME !')
