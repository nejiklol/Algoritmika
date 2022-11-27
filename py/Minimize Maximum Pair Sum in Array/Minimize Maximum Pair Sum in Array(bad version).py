def minPairSum(nums):
        maxx = 0
        nums = sorted(nums)
        while nums!=[]:
            mi = nums[-1]
            ma = nums[0]
            del nums[-1]
            del nums[0]
            mem = mi+ma
            if maxx<mem:
                maxx = mem
        return maxx