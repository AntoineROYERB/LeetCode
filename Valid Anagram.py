#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = {}
        counter_t = {}
        for letter in s:
            counter_s[letter] = counter_s.get(letter,0) + 1
        for letter in t:
            counter_t[letter] = counter_t.get(letter,0) + 1
        if counter_s == counter_t: return True
        else: return False