
# Create a function that takes a skyline (2-D list of 0's and 1's)
# and returns the height of the tallest skyscraper.



def tallest_skyscraper(lst):
    nrow = len(lst)
    ncol = len(lst[0]) 
    for i in range(nrow):
        for j in range(ncol):
            if lst[i][j] == 1:
                indx = i
                return nrow - indx

    



				
print( "the tallest building should be at index", 
    tallest_skyscraper([
    [0, 0, 0, 0, 0, 0], # i = 0
    [0, 0, 0, 0, 1, 0], # i = 1
    [0, 0, 1, 0, 1, 0], # i = 2
    [0, 1, 1, 1, 1, 0], # i = 3
    [1, 1, 1, 1, 1, 1]])
    
)