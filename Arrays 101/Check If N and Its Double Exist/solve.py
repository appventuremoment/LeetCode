class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if 2 * arr[i] in arr and len([x for x in range(len(arr)) if arr[x] == 2 * arr[i] and x != i]) != 0:
                return True
        return False