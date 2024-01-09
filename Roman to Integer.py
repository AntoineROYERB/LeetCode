class Solution:
    def romanToInt(self, s: str) -> int:
        dico = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000, "IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        theInt = 0
        index = 0

        while index < len(s) - 1:
            if dico[s[index]] >= dico[s[index + 1]]:
                theInt += dico[s[index]]
                index += 1
            elif dico[s[index]] < dico[s[index + 1]]: 
                theInt += dico[s[index] + s[index + 1]]
                index += 2

        if index == len(s):
            return theInt
        else: 
            theInt += dico[s[index]]
            return theInt
            