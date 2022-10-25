class Solution:
    def romanToInt(self, s: str) -> int:
        array = []
        number = 0
        
        for i in s:
            array.append(self.strTOint(i))
        i = 0
        while i != len(array):
            if i+1<len(array):
                if array[i] < array[i+1]:
                    number+= array[i+1] - array[i]
                    i+=2
                else:
                    number+= array[i]
                    i+=1
        
        return  number

            
    def strTOint(self, s: str) -> int:
        sttr = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        innt = [ 1,   5,   10,  50,  100, 500, 1000]
        for i in range(len(sttr)):
            if s == sttr[i]:
                return(innt[i])
            
            
