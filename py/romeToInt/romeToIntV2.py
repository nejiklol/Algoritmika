import time
class Solution:
    
    def romanToInt(self, s: str) -> int:
        number = 0
        sttr = s
        map = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900,
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000       
        }
        while sttr != '':
            for i in map:
                if i in sttr:
                    
                    number += map.get(i,0) * (sttr.count(i))
                    sttr = sttr.replace(i,'')
        return number

            
    
            
b = time.time()        
a = Solution()
ssttr = 'MDCLXLVVVIV'
print(a.romanToInt(ssttr))
print("--- %s seconds ---" % (time.time() - b))
