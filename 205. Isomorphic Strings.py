class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

# set(zip(s, t)): This creates a set of tuples, where each tuple contains a pair of characters (s[i], t[i]) 
# from the corresponding positions in the strings s and t. Since sets only contain unique elements, 
# this operation effectively removes duplicates.
# len(set(zip(s, t))): This calculates the number of unique character mappings between the strings s and t. 
# If the strings are isomorphic, this count should be equal to the number of unique characters in s and t.