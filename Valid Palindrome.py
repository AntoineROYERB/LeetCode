#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_to_test = ''
        s_reversed = ''
        for index in range(len(s)):
            if s[index].isalnum():
                s_to_test += s[index].lower()
            if s[-(index + 1)].isalnum():
                s_reversed += s[-(index + 1)].lower()
        if s_to_test == s_reversed: return True
        else: return False