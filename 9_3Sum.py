class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        #sorting
        nums.sort()

        for i in range(len(nums)):
            #print("her")
            if(i>0 and (nums[i]==nums[i-1])):
                continue
            target_sum = -1*nums[i]

            l = i+1
            r = len(nums)-1

            while(l<r):
                
                running_sum = nums[l]+nums[r]
                if(running_sum < target_sum):
                    l+=1
                    while(l<len(nums) and nums[l]==nums[l-1]):
                        l+=1
                elif(running_sum > target_sum):
                    r-=1
                    while(r>=0 and nums[r]==nums[r+1]):
                        r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1 # this can be done or r-=1
                    while(l<len(nums) and nums[l]==nums[l-1]):
                        #print("inc")
                        l+=1
                    #break
            
        
        return res
Console
