"""

Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].

"""

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_loc = 0
        max_loc = 0
        global_minimum = arrays[0][0]
        global_maximum = arrays[0][-1]
        for i in range(len(arrays)):
            if arrays[i][0] < global_minimum:
                global_minimum = arrays[i][0]
                min_loc = i
            if arrays[i][-1] > global_maximum:
                global_maximum = arrays[i][-1]
                max_loc = i
            
        if max_loc == min_loc:
            local_maximum = -10001
            local_minimum = 10001
            for i in range(len(arrays)):
                if arrays[i][0] < local_minimum and i != min_loc:
                    local_minimum = arrays[i][0]
                if arrays[i][-1] > local_maximum and i != max_loc:
                    local_maximum = arrays[i][-1]
            return max(global_maximum-local_minimum, local_maximum-global_minimum)
        return global_maximum - global_minimum
                
            
        