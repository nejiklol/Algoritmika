def minPairSum(nums):
        maxx = 0
        nums = sorted(nums)
        for i in range(0,len(nums)//2):
            mi = nums[-(i+1)]
            ma = nums[i]
            mem = mi+ma
            if maxx<mem:
                maxx = mem
        return maxx