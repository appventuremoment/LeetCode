class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        out = []
        nums1pointer, nums2pointer = 0, 0
        while nums1pointer < m and nums2pointer < n:
            if (nums1[nums1pointer] < nums2[nums2pointer]):
                out.append(nums1[nums1pointer])
                nums1pointer += 1
            else:
                out.append(nums2[nums2pointer])
                nums2pointer += 1
        while nums1pointer < m:
            out.append(nums1[nums1pointer])
            nums1pointer += 1
        while nums2pointer < n:
            out.append(nums2[nums2pointer])
            nums2pointer += 1
        for i in range(m + n):
            nums1[i] = out[i]