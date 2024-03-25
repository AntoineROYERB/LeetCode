class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dico = {}
        for num in nums:
            dico[num] = dico.get(num,0) + 1

        for num, count in dico.items():
            if count > len(nums)/2:
                return num