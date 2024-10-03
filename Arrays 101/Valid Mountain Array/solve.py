class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        maxi = arr.index(max(arr))
        firsthalf = arr[:maxi + 1]
        secondhalf = arr[maxi:]
        assertion1 = [firsthalf[x] > firsthalf[x - 1] for x in range(1, len(firsthalf))]
        assertion2 = [secondhalf[x] < secondhalf[x - 1] for x in range(1, len(secondhalf))]
        if len(firsthalf) <= 1 or len(secondhalf) <= 1 or False in assertion1 or False in assertion2:
            return False
        else: return True