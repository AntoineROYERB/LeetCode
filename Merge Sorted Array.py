#https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # Index de la dernière valeur non nulle de nums1
        j = n - 1  # Index de la dernière valeur de nums2
        k = m + n - 1  # Index du dernier élément de nums1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # S'il reste des éléments dans nums2, ils doivent être copiés
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1