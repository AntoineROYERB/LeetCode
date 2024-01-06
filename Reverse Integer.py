class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        x_reversed = ''
        
        #reverse the string letter by letter
        for k in range(len(s)):
            if s[-(k+1)] == '-':
                x_reversed = '-' + x_reversed
            else:
                x_reversed +=  s[-(k+1)]
        x_reversed = int(x_reversed)

        #Check this is a 32-bit integer
        if -2**31 < x_reversed < 2**31 - 1:
            return x_reversed
        else:
            return 0
