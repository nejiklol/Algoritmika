def replaceElements(arr) -> List[int]:
        flag = True
        newarr=[]
        maxx = 0
        newarr.append(-1)
        for i in reversed(arr):
            if flag == True:
                if maxx<i:
                    maxx = i
                flag = False
                continue
            
            newarr.append(maxx)
            if maxx<i:
                maxx = i
        
        return reversed(newarr)
        