import math

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dict of y/x pair and the sum it took to get there
        path_sums = {}
        # index through grid
        for y in range(len(grid)):
            # index through grid[i]
            for x in range(len(grid[y])):
                # check for val directly above index and left of index, take smallest value
                lowest_path_sum = min(path_sums.get((y-1,x),math.inf), path_sums.get((y,x-1),math.inf))
                if y == 0 and x == 0:
                    lowest_path_sum = 0
                # add val to curr_val, store that into dict y/x pair
                path_sums[(y,x)] = lowest_path_sum + grid[y][x]
        
        # return dict y/x
        last_grid_i = len(grid)-1
        return path_sums[(last_grid_i,len(grid[last_grid_i])-1)]