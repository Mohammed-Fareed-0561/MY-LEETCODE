class Solution:
    def reverse(self, x: int) -> int:

        y = str(abs(x))
        r = y[::-1]
        con_num = int(r)    
        if x < 0:
                fin = -con_num
        else: 
                fin = con_num
        if fin < -2**31 or fin > 2**31 - 1:
                return 0
            
        return fin
            