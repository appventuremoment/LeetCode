class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        out = [x for x in nums if x != val]
        for i in range(len(out)):
            nums[i] = out[i]
        for _ in range(len(out), len(nums)):
            nums.pop()