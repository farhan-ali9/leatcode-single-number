#First solution
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for i in nums: #0 #1
            result^=i # '^' show xor operation result =0^2=2 # result    =2^2=0   # result=0^1=1
        return result

#second solution
        c=0
        while c<len(nums)-1: #0<3 #2<3
            if nums[c]!=nums[c+1]: #2!=2 # 1!=2
                return nums[c]  #false #true
            c+=2 # c become 2 
        return nums[c] #1
