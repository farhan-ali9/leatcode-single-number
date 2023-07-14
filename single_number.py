#second solution
        c=0
        while c<len(nums)-1: #0<3
            if nums[c]!=nums[c+1]: #2!=2
                return nums[c]  #false
            c+=2 # c become 2
        return nums[c]
