class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index in range(len(s)):
            s_without_current_letter = s[0:index] + s[index+1:]
            if s[index] not in s_without_current_letter:
                return index
        return -1