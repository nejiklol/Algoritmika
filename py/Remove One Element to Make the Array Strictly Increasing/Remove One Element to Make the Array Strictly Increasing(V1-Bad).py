
def canBeIncreasing(nums):
        i = 1
        while i !=len(nums):
            while nums[i] == nums[i-1]:
                nums.pop(i)
                if len(nums) == 1:
                    return True
            i+=1
            
        if nums == [] or len(nums)==2:
            return True
        save = nums.copy()
        for i in range(len(nums)):
            del nums[i]
            for j in range(1,len(nums)):                
                if (nums[j-1]<nums[j]) and (j == len(nums)-1):
                    return True
                if nums[j-1]>nums[j]:
                    nums = save.copy()
                    break
            if i == len(save)-1:
                return False
   
            

numss = [2,3,1,2]
print(canBeIncreasing(numss))
