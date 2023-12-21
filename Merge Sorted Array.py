class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums1[0] == 0:
            nums1[:] = nums2
        while nums1[-1] == 0:
            print("dans le while")
            if nums1[i] < nums2[0]:
                i+=1
            if nums1[i] >= nums2[0]:
                nums1.insert(i, nums2.pop(0))
                nums1.pop(-1)
                i+=1         
            if nums1[i] == 0:
                nums1[i:] = nums2