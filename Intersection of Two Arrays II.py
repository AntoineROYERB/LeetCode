class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counter1, counter2 = {},{}
        intersect = []
        #dictionary to count occurrences for each list
        for num in nums1:
           counter1[num] = counter1.get(num,0) + 1
        for num in nums2:
           counter2[num] = counter2.get(num,0) + 1

        for num in counter1.keys():
            if num in counter2:
                for k in range(min(counter1[num], counter2[num])):
                    intersect.append(num)
        return intersect

sol = Solution()
sol.intersect([1,1,2,2],[2,3,1,5,1])