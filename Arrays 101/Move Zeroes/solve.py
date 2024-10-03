class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        out = [x for x in nums if x != 0]
        out += [0] * (len(nums) - len(out))
        for i in range(len(nums)): nums[i] = out[i]