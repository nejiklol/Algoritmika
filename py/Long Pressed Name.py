def isLongPressedName(name: str, typed: str) -> bool:
        longName = len(name)
        longTyped = len(typed)
        if longName>longTyped:
            return False
        elif longName==longTyped and name!=typed:
            return False
        else:
            while typed and name:
                newChar = name[0]
                i,j = 0,0
               
                if newChar == typed[0]:
                    
                    while name and newChar == name[0]:
                        name=name[1:]
                        i+=1
                    while typed and newChar == typed[0] :
                        typed=typed[1:]
                        j+=1
                else:
                    print(name,'---',typed)
                    return False
                if i>j:
                    return False
                        
            print(name,'---',typed)
            if typed != name:
                return False
        return True