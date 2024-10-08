#Two sum II => input array is sorted 
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        D={}
        i=0
        while (i<len(numbers)):
            if (target-numbers[i]) not in D.keys():
                D[numbers[i]]=i
                print(D)
            elif (i==len(numbers)):
                return -1
            else:
                return [ D[target - numbers[i]]+1,i+1]
            i+=1
                    
        
