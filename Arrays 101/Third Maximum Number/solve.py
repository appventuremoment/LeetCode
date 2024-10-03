class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3: return max(nums)
        first, second, third = nums[0], -(2 ** 31), -(2 ** 31)
        for i in range(1, len(nums)):
            print(first, second, third)
            if nums[i] > first:
                third = second
                second = first
                first = nums[i]
            elif nums[i] > second:
                third = second
                second = nums[i]
            elif nums[i] > third:
                third = nums[i]
        return third