class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cnt_0,cnt_1,cnt_2=0,0,0
        for x in nums:
            if(x==0):cnt_0+=1
            elif (x==1):cnt_1+=1
            else: cnt_2+=1
        for i in range(cnt_0):
            nums[i]=0
        for i in range(cnt_0,cnt_0+cnt_1):
            nums[i]=1
        for i in range(cnt_0+cnt_1,cnt_0+cnt_1+cnt_2):
            nums[i]=2
        # print(nums)
        

            
            

                
            

