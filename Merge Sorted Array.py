class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        numberOfValuesPopped = 0
        if n != 0:
            for k in range(m):
                    if nums1[k] > nums2[0]:
                        nums1.insert(k + numberOfValuesPopped, nums2.pop(0))
                        del nums1[-1]
                        numberOfValuesPopped += 1

        if len(nums2) != 0:
            print(nums1, nums2)
            if nums2[0] <= nums1[0]:
                for k in range(len(nums2)):
                        del nums1[-1]
                        nums1.insert(0, nums2[k])
                        
            if nums2[0] > nums1[0]:
                nums1[-len(nums2):] = nums2