class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return [-1]
        bottomup = arr[::-1]
        out = [-1, bottomup[0]]
        for x in range(1, len(arr) - 1):
            if bottomup[x] > out[-1]: out.append(bottomup[x])
            else: out.append(out[-1])
        return out[::-1]