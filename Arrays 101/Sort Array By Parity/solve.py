class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        pointer1, pointer2 = 0, len(nums) - 1
        while pointer2 > pointer1:
            while nums[pointer1] % 2 == 0 and pointer1 < len(nums) - 1: pointer1 += 1
            while nums[pointer2] % 2 == 1 and pointer2 > 0: pointer2 -= 1
            if pointer2 <= pointer1: break
            nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
        return nums