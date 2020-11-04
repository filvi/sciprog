# Create a function that takes a skyline (2-D list of 0's and 1's)
# and returns the height of the tallest skyscraper.

def tallest_skyscraper(lst):
	nrow = len(lst)
	ncol = len(lst[0]) 
	max_sth = dict()
	for i in range(nrow):
		for j in range(ncol):
			if lst[i][j] == 1:
				max_sth[j] += 1
			else:
				max_sth[j] += 0
	return max(max_sth)
				
				


tallest_skyscraper(
    [[0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1]]
)