class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        out = sorted(list(set(nums)))
        for i in range(len(out)):
            nums[i] = out[i]
        for _ in range(len(out), len(nums)):
            nums.pop()