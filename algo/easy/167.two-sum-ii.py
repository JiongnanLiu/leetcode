#array is already sorted in ascending order

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while (l < r):
            twosum = numbers[l] + numbers[r]
            if twosum == target:
                return [l+1, r+1]
            elif twosum < target:
                l+=1
            else:
                r-=1
        return [-1,-1]