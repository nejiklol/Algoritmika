def canBeIncreasing(nums):
        flag = 0
        i = 1
        if len(nums) == 2:
            return True
        while i != len(nums):
            
            if nums[i-1]>=nums[i]and flag == 0:
                if nums[i-2]>nums[i] and i-2>-1:
                        del nums[i]
                        if i == 1:
                            flag = 1
                            continue
                        i=i-1
                        flag = 1
                        continue
                del nums[i-1]
                if i == 1:
                    flag = 1
                    continue       
                i=i-1
                flag = 1
            
            elif nums[i-1]>=nums[i] and flag == 1:
                return False
            elif nums[i-1]<nums[i] and i == len(nums):
                break
            else:
                i+=1
        return True
   
            

numss = [1,2,1]
print(canBeIncreasing(numss))
