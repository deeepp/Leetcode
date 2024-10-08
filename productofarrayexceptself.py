#Product of Array except Self
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=1
        s=1
        prev=[1]
        succ=[1]
        result=[]
        for i in range(len(nums)-1):
            p*=nums[i]
            prev.append(p)
        for i in range(len(nums)-1):
            s*=nums[len(nums)-i-1]
            succ.insert(0,s)
        print(prev)
        print(succ)
        for i in range(len(nums)):
            result.append(prev[i]*succ[i])
        return result 

