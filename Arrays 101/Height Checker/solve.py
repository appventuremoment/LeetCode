class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        out =  sorted(heights)
        ret = 0
        for i in range(len(heights)): 
            if heights[i] != out[i]: ret += 1
        return ret