class Solution:
    def myAtoi(self, s: str) -> int:
        int_is_positive = 1
        index = 0
        
        while index < len(s) and s[index] == " ":
            index += 1
        s = s[index:]    

        if s == "":
            return 0
        
        if s[0] == "-" or s[0] == "+":
            
            if s[0] == "-":
                int_is_positive = -1
                s = s[1:] 
            
            elif s[0] == "+":
                s = s[1:]
        
        index = 0
        while index < len(s) and s[index].isdigit():
            index += 1
            

        s = s[:index]
        if not s:
            return 0
        
        s = int_is_positive * int(s)

        if s < -2**31:
            return - (2**31)
        
        if s > 2**31 - 1:
            return 2**31 - 1

        return s
