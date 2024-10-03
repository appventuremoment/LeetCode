class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([len(x) for x in "".join(list(map(str, nums))).split('0')])