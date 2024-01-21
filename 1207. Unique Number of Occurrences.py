#https://leetcode.com/problems/unique-number-of-occurrences/
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        my_dict = {}
        for num in arr:
            my_dict[num] = my_dict.get(num, 0) + 1
        if len(my_dict.values()) == len(set(my_dict.values())):
            return True
        return False