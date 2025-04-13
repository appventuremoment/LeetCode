class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ind = nums.index(max(nums))
        largest = nums.pop(nums.index(max(nums)))
        if 2 * max(nums) > largest: return -1
        else: return ind