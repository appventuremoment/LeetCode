class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        point1, point2 = 0, len(nums) - 1
        i = point2
        while 0 <= i:
            if abs(nums[point1]) > abs(nums[point2]):
                out[i] = nums[point1] ** 2
                point1 += 1
            else:
                out[i] = nums[point2] ** 2
                point2 -= 1
            i -= 1
        return out