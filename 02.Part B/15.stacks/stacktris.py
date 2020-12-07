DEBUG = True

def debug(msg):
    if DEBUG:
        print("DEBUG: ", str(msg).replace('\n', '\n' + (' '*8)))
        
class Stacktris:

    def __init__(self):
        """ Creates a Stacktris
        """
        self._stack = []


    def __str__(self):
        if len(self._stack) == 0:
            s = "EMPTY"
        else:
            s = ""
            for row in reversed(self._stack):
                s = s + '|' + "".join((str(x) if x > 0 else ' ' for x in row)) + '|\n'         

        return "Stacktris: \n%s" % s
        
    def __repr__(self):
        return self.__str__()


    def is_empty(self):
        """ RETURN True if the Stacktris empty, False otherwise
        """
        return len(self._stack) == 0

    def _shorten(self):      
        """ Scans the Stacktris from top to bottom searching for a completely filled line:
            - If it finds it, removes it from the Stacktris and return it as a list.
            - if it doesn't find it, return an empty list.
        """
        raise Exception('TODO IMPLEMENT ME !')          


    def drop1(self, j):
        """ Drops a 1-block on column j. 
        
             - If another block is found,  place the 1-block on top of that block,
               otherwise place it on the ground.

            - If, after the 1-block is placed, a row results completely filled, removes 
              the row and RETURN it. Otherwise, RETURN an empty list.

            - if index `j` is outside bounds, raises ValueError
        """        
        raise Exception('TODO IMPLEMENT ME !')


    def drop2h(self, j):
        """ Drops a 2-block horizontally with left block on column j, 

             - If another block is found,  place the 2-block on top of that block,
               otherwise place it on the ground.

            - If, after the 2-block is placed, a row results completely filled, 
              removes the row and RETURN it. Otherwise, RETURN an empty list.        
        
            - if index `j` is outside bounds, raises ValueError
        """        
        raise Exception('TODO IMPLEMENT ME !')



