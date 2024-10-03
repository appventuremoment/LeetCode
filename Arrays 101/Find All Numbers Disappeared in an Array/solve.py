class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums: 
            if nums[abs(x) - 1] > 0: nums[abs(x) - 1] *= -1
        return [x + 1 for x in range(len(nums)) if nums[x] >= 1]