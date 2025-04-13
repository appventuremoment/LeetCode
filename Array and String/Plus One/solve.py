class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        curr = len(digits) - 1
        while curr > 0:
            if digits[curr] == 10:
                digits[curr] = 0
                curr -= 1
                digits[curr] += 1
            else: break
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits