class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        curr_sum = nums[0]
        max_sum = nums[0]
        
        for i in nums[1:]:
            curr_sum = max(i , curr_sum + i)
            max_sum = max(curr_sum, max_sum)
        
        return max_sum