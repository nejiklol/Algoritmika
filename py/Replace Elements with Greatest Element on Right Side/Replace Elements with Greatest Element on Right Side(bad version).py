def replaceElements(arr) -> List[int]:
        newarr=[]
        for i in range(1,len(arr)):
            newarr.append(max(arr[i:]))
        newarr.append(-1)
        return newarr
